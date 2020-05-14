import json
from channels.generic.websocket import WebsocketConsumer
from . import action

class TableConsumer(WebsocketConsumer):
    def connect(self):
        self.table_code = self.scope['url_route']['kwargs']['table_code']
        self.table_group_code = 'table_%s' % self.table_code

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.table_group_code,
            self.channel_name
        )

        self.accept()

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
            name = text_data_json['name']

            async_to_sync(self.channel_layer.group_send)(
                self.table_group_code,
                {
                    'type': 'chat_message',
                    'message': message,
                    'name' : name,
                }
            )

        elif type == 'action' :
            initiator = self.channel_name
            action_type = text_data_json['action_type']
            args = text_data_json['args']

            self.send(
                text_data=action.performMe(action_type, json.loads(event['args']))
            )

            async_to_sync(self.channel_layer.group_send)(
                self.table_group_code,
                {
                    'type': 'perform_action',
                    'action_type': action_type,
                    'args': args,
                    'initiator': initiator,
                }
            )
        #else :
            #unsupported Action

    # Receive message from room group
    def table_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))

    #Perform a client game update based on messages
    #recieved from the group.
    def perform_action(self, event):
        initiator = event['initiator']

        if initiator != self.channel_name:
            action = event['action_type']
            args = json.loads(event['args'])
            self.send(
                text_data=action.performOther(action, initiator, args)
            )
        #if we initiated this perform_action, we've already handled
        #the event.
