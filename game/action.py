import json

class action() :
    #needs to return the json for the action.
    other_action_dict =
    {
        'draw' : drawOther,
        'discard' : discardOther,
        'setAside' : setAsideOther,
        'shuffle' : shuffleOther,
        'distodraw' : disToDrawOther,
        'play' : playOther,
    }

    me_action_dict =
    {
        'draw' : drawMe,
        'discard' : discardMe,
        'setAside' : setAsideMe,
        'shuffle' : shuffleMe,
        'distodraw' : disToDrawMe,
        'play' : playMe,
    }

    def performOther(self, action, initiaitor, args):
        return other_action_dict[action](initiator, args)
        #Actions performed by others are processed differently for me.

    def performMe(self, action, args):
        return me_action_dict[action](args)
        #Actions performed by me are processed differently for others.

    def drawMe(args): #Draw -> My Hand
        #This function needs to update the database (draw cards)
        #and then return JSON with all information regarding that
        #action, so that others can update their client.

    def discardMe(args): #Any -> Discard
        #This function needs to update the database (draw cards)
        #and then return JSON with all information regarding that
        #action, so that others can update their client.

    def shuffleMe(args): #Reorder randomly the Draw.

    def disToDrawMe (args): #All Discard -> Draw

    def playMe(args): #Hand -> Play Area

#Other Versions of Me functions

    def playOther(initiator, args):

    def shuffleOther(initiator, args):

    def disToDrawOther (initiator, args):

    def setAsideMe(args): #Any -> aside

    def drawOther(initiator, args):

    def discardOther(initiator, args):

    def setAsideOther(initiator, args):

#Generic Helper Functions
    def move (card, source, destination):
