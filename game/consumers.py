import json
from channels.generic.websocket import WebsocketConsumer
from . import action
from . import message

class TableConsumer(WebsocketConsumer):
    def connect(self):
        self.table_code = self.scope['url_route']['kwargs']['table_code']
        action.initiate(self.table_code)

        self.table_group_code = 'table_%s' % self.table_code

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.table_group_code,
            self.channel_name
        )
        name = self.channel_name

        #Create a hand cardpool for this channel and session.
        self.accept()

        self.send(text_data=json.dumps({
            'message': 'You are \"name\".',
            'name' : 'System',
        }))

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.table_group_code,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        #deduce what type of message was sent,
        #route and act on it accordingly.

        type = text_data_json['type']

        if type == 'chat' :
            message = text_data_json['message']
            name = self.channel_name

            async_to_sync(self.channel_layer.group_send)(
                self.table_group_code,
                {
                    'type': 'text_message',
                    'message': message,
                    'name' : name,
                }
            )

        elif type == 'action' :
            initiator = self.channel_name
            action_type = text_data_json['action_type']

            #Perform the action, then send the result to all
            #channels in the group to be update the client.
            message_generate_dict = {
                'type': 'generate_message',
                'action_type': action_type,
                'initiator': initiator,
            }
            #Add the rest of the message from the perform.
            message_generate_dict.update(action.performAction(initiator, text_data_json))

            async_to_sync(self.channel_layer.group_send)(
                self.table_group_code,
                message_generate_dict
            )
        #else :
            #unsupported Action

    # Receive message from room group
    def text_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'name' : name,
        }))

    #Perform a client game update based on messages
    #recieved from the group.
    def generate_message(self, event):
        if event['initiator'] == self.channel_name:
            event['initiator'] = 'me'
        #Message.generate needs to return a dict, which will be converted here
        #to json.
        self.send(
            text_data=json.dumps(message.generate(event))
        )
