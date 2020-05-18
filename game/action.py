import json

class action() :

    action_dict =
    {
        'draw' : draw,
        'discard' : discard,
        'setAside' : setAside,
        'shuffle' : shuffle,
        'distodraw' : disToDraw,
        'play' : play,
        'sweep' : sweep,
    }

    def performAction(initiator, json_data):
        return action_dict[json_data['action_type']](initiator, json_data)
        #Actions performed by me are processed differently for others.

    def draw(initiator, json_data): #Draw -> My Hand
        #This function needs to update the database (draw cards)
        #and then return JSON with all information regarding that
        #action, so that others can update their client.

    def discard(initiator, json_data): #Any -> Discard
        #This function needs to update the database (draw cards)
        #and then return JSON with all information regarding that
        #action, so that others can update their client.

    def shuffle(initiator, json_data): #Reorder randomly the Draw.
        return ''

    def disToDraw(initiator, json_data): #All Discard -> Draw

    def play(initiator, json_data): #Hand -> Play Area

    def setAside(initiator, json_data):

    def sweep(initiator, json_data):

#Generic Helper Functions
    def move (card, source, destination):
