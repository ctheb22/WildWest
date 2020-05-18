import JSON

class message():
    #needs to return the json for the action.
    action_dict =
    {
        'draw' : draw,
        'discard' : discard,
        'setAside' : setAside,
        'shuffle' : shuffle,
        'distodraw' : disToDraw,
        'play' : play,
        'sweep': sweep,
    }

    def generate(event_dict):
        return action_dict[event_dict['action_type']](me, initiator, event_dict)

    def draw(event_dict): #initiator draw
        if event_dict['facing'] == 'down' && event_dict['initiator'] != 'me':
            return chatify(faceDown(event_dict))
        else:
            return chatify(event_dict)

    def discard(event_dict): #initiator discard
        if event_dict['facing'] == 'down' && event_dict['initiator'] != 'me':
            return chatify(faceDown(event_dict))
        else:
            return chatify(event_dict)

    def setAside(event_dict): #initiator setAside
        return chatify(event_dict)
        #definitely more work/thought here.

    def shuffle(event_dict): #any shuffle
        return chatify(event_dict)

    def disToDraw(event_dict): #any disToDraw
        return chatify(event_dict)

    def play(event_dict): #initiator play
        if event_dict['facing'] == 'down' && event_dict['initiator'] != 'me':
            return chatify(faceDown(event_dict))
        else:
            return chatify(event_dict)

    def sweep(event_dict):
        return chatify(event_dict)
        
    #helper methods

    def faceDown(event_dict):
        #for card in event_dict['cards'] flip face down
        return event_dict

    def chatify(messages):
        for item in messages.items()
            message += (item + "/n")

        return {
            'message': message,
            'name': messages['initiator']
        }
