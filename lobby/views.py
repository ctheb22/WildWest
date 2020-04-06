from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from lobby.GameRoomUtil import generateCode
from .models import GameRoom

def index (request):
        return render(request, 'lobby/index.html')

def roomList (request):
        rooms = GameRoom.objects.order_by('-create_date')[:5]
        context = {'rooms': rooms}
        #In template, add way to join room by code.
        return render(request, 'lobby/roomList.html', context)

def gameRoom (request, game_id):
        room = get_object_or_404(GameRoom, pk=game_id)
        context = {'room': room}
        return render(request, 'lobby/gameRoom.html', context)

def createRoom (request):
        #Check that code doesn't already exist.
        roomCode = generateCode()
        newRoom = GameRoom(create_date=timezone.now(), room_name=request.POST['roomName'], private=True, room_code=roomCode)
        newRoom.save()
        #In template, allow user to set options.
        return HttpResponseRedirect(reverse('lobby:gameRoom', args=(newRoom.id,)))

def takeASeat (request):
    #Create the Table if it doesn't exist
    #Associate the table with the room id from the url.
    #Add player
    #Set up WebSocket
    return render(request, 'table.html')
