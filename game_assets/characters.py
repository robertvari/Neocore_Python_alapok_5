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

    @property
    def stats(self):
        print("-"*25, f"{self._name}", "-"*25,)
        print(f"Race: {self._race}")

        print("-"*25, "Inventory", "-"*25,)

        print(f"Golds: {self._golds}")
        print(f"Inventory: {self._inventory}")
        print(f"Left Hand: {self._left_hand}")
        print(f"Right Hand: {self._right_hand}")

        print("-"*25, "Combat Stats", "-"*25,)

        print(f"Strength: {self._strength}")
        print(f"Initiative: {self._initiative}")
        print(f"Max HP: {self._max_HP}")
        print(f"Current HP: {self._current_HP}")

    def __repr__(self):
        return self._name


class Player(Character_Base):
    pass

class AIPlayer(Character_Base):
    pass


if __name__ == "__main__":
    ai_player = AIPlayer()
    ai_player.stats