import random
from game_assets.characters import AIPlayer

class Location_Base:
    def __init__(self, name) -> None:
        self._name = name
        self._player = None
        self._ai_players = []

        self._create()
    
    def _create(self):
        for _ in random.range(0, 10):
            self._ai_players.append(AIPlayer())

    def enter(self, player):
        self._player = player


class Tavern(Location_Base):
    pass

class Village(Location_Base):
    pass

class Forest(Location_Base):
    pass