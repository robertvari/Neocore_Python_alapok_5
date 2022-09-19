import random, os, time
from characters import AIPlayer

class Location_Base:
    def __init__(self, name) -> None:
        self._name = name
        self._player = None
        self._ai_players = []

        self._create()
    
    def _create(self):
        for _ in range(random.randint(0, 10)):
            self._ai_players.append(AIPlayer())

    def enter(self, player):
        self._clear_screen()
        self._player = player

    def _clear_screen(self):
        os.system("cls")

class Tavern(Location_Base):
    def enter(self, player):
        super().enter(player)

        print(f"Wellcome {player} in the {self._name} tavern.")
        time.sleep(1)

        print("If you have gold you can buy a dring")
        print("1 Buy a dring")
        print("2 Exit tavern")

        response = input()

        if response == "2":
            print("See you later. Safe travel!")
        else:
            print("You bought a cup of beer.")

class Village(Location_Base):
    def enter(self, player):
        super().enter(player)

        print(f"Wellcome {player} in {self._name} willage.")
        time.sleep(1)

        print("There is a neerby tavern.")
        print("1 Go to the tavern")
        print("2 Go back to the forest")

        response = input()

        if response == "2":
            print("See you later. Safe travel!")
        else:
            print("You enter the forest.")

class Forest(Location_Base):
    def enter(self, player):
        super().enter(player)

        print("You entered into a dark forest.")
        time.sleep(1)
        print("You hear something from a nearby bush.")
        time.sleep(3)

        print("Something attacks yout...")


if __name__ == "__main__":
    from characters import Player
    player = Player()

    location = Forest("Dark Forest")
    location.enter(player)