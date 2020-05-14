from django.db import models
from django.utils import timezone

class GameAction(models.Model):
    action = models.CharField(max_length=15)
    def __str__(self):
        return self.action
#Stores any possible action literals.

class Deck(models.Model):
    deck_name = models.CharField(max_length=50)
    deck_key = models.OneToManyField(
        Card,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    def __str__(self):
        return self.deck_name
#Used to track what cards are in a "deck"
#Leveraged to load a SessionCardPool

class Card(models.Model):
    card_value = models.CharField(max_length=20)
    def __str__(self):
        return self.card_value
#An instance of a card. Referenced by many other tables
#since they're generic and don't have anything specific
#stored for a session.

class GameSession(models.Model):
    session_key = models.CharField(max_length=10, primary_key=True)
    session_card_pool = models.OneToManyField(
        CardPool,
        on_delete=models.CASCADE,
        primary_key=False
    )
    def __str__(self):
        return self.table_key
#A model instance of a game session. Stores the card pool
#and maybe more information in the future.

class SessionCardPool(models.Model)
    session_key = models.ForeignKey(
        GameSession,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    card_index = models.IntegerField(primary_key=True)
    card = models.OneToManyField(
        Card,
        on_delete=models.CASCADE,
        primary_key=False
    )
    pool_location = models.OneToOneField(
        CardPool,
        on_delete=models.CASCADE,
        primary_key=True,
        nullable = False,
    )
    #All cards for a given game session.
    #Every card in the SessionCardPool must have a
    #pool location that tracks "where" the card is
    #in the game.

class CardPool(models.Model):
    card_pool_key = models.CharField(max_length=10, primary_key=True)
    session_key = models.ForeignKey(
        GameSession,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    #Represents each individual location where a card can be.
    #Draw, Discard, Aside, Play Area are special pools that
    #are automatically added everytime a game is created.
    #Each "hand" also has it's own card pool.
