import random

class Character_Base:
    def __init__(self) -> None:
        self._name = None
        self._race = None

        self._golds = random.randint(0, 100)
        self._inventory = []
        self._right_hand = None
        self._left_hand = None

        self._strength = 0
        self._initiative = random.randint(1, 10)
        self._current_HP = 0
        self._max_HP = 0

        self._create()

    def _create(self):
        pass


class Player(Character_Base):
    pass

class AIPlayer(Character_Base):
    pass