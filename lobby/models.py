from django.db import models
from django.db import models
from django.utils import timezone

class GameRoom(models.Model):
    room_name = models.CharField(max_length=100)
    create_date = models.DateTimeField('date created')
    room_code = models.CharField(max_length=8)
    private = models.BooleanField()
    def __str__(self):
        return self.room_name

    def is_private(self):
        return self.private