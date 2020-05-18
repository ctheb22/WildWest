# chat/views.py
from django.shortcuts import render, get_object_or_404
from lobby.models import GameRoom

def index(request):
    return render(request, 'game/index.html')

def table(request, table_code):

    room = get_object_or_404(GameRoom, pk=game_id)
    #Check game model for an existing session.

    #if it doesn't exist,
        #Get Deck cards,
        #Create game session, set session card pool null
        #Create default cardpools for the session
        #create new session card pool records with the deck and new cardpools
        #tableCode, index, card, CardPool
        #add the new SessionCardPool to the new GameSession.
    #else it already exists
        #Just render the table.html
    return render(request, 'game/table.html', {
        'table_code': table_code
    })
