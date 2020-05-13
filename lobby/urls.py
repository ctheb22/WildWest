from django.urls import path
from . import views

app_name = 'WestLobby'
urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.roomList, name='roomList'),
    path('<int:game_id>/', views.gameRoom, name='gameRoom'),
    path('createRoom/', views.createRoom, name='createRoom'),
    path('<int:game_id/table/', views.takeASeat, name='takeASeat'),
]
