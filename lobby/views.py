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
        return render(request, 'lobby/roomList.html', context)

def gameRoom (request, game_id):
        room = get_object_or_404(GameRoom, pk=game_id)
        context = {'room': room}
        return render(request, 'lobby/gameRoom.html', context)

def createRoom (request):
        roomCode = generateCode()
        newRoom = GameRoom(create_date=timezone.now(), room_name=request.POST['roomName'], private=True, room_code=roomCode)
        newRoom.save()
        return HttpResponseRedirect(reverse('lobby:gameRoom', args=(newRoom.id,)))