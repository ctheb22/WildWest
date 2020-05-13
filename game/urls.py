# chat/urls.py
from django.urls import path

from . import views

app_name = 'game'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:table_code>/', views.table, name='table'),
]
