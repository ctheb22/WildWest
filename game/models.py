from django.db import models
from django.utils import timezone

class Card(models.Model):
    card_value = models.CharField(max_length=20)
    deck_name = models.CharField(max_length=50)
    def __str__(self):
        return self.card_value
#An instance of a card. Referenced by many other tables
#since they're generic and don't have anything specific
#stored for a session.

class GameSession(models.Model):
    session_key = models.CharField(max_length=10, primary_key=True)
    def __str__(self):
        return self.table_key
#A model instance of a game session. Stores the card pool
#and maybe more information in the future.

class CardPool(models.Model):
    card_pool_key = models.CharField(max_length=10)
    session = models.ForeignKey(
        GameSession,
        related_name = 'session_pools',
        on_delete=models.CASCADE,
    )
    #Represents each individual location where a card can be.
    #Draw, Discard, Aside, Play Area are special pools that
    #are automatically added everytime a game is created.
    #Each "hand" also has it's own card pool.

class SessionCardPool(models.Model):
    session_key = models.ForeignKey(
        GameSession,
        related_name = 'session_cards',
        on_delete=models.CASCADE,
    )
    card = models.ForeignKey(
        Card,
        on_delete=models.CASCADE,
    )
    pool_location = models.ForeignKey(
        CardPool,
        related_name = 'cards',
        on_delete=models.CASCADE,
    )
    #All cards for a given game session.
    #Every card in the SessionCardPool must have a
    #pool location that tracks "where" the card is
    #in the game.
