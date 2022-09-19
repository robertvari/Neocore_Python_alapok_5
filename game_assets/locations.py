from pkgutil import iter_modules
import random, os, time
from game_assets.characters import AIPlayer
from game_assets.items import CommonItem, WeaponItem


class Location_Base:
    def __init__(self, name, game_instance) -> None:
        self._game_instance = game_instance
        self._name = name
        self._player = game_instance.player
        self._ai_players = []

        self._create()
    
    def _create(self):
        for _ in range(random.randint(0, 10)):
            self._ai_players.append(AIPlayer())

    def enter(self):
        self._clear_screen()

    def _clear_screen(self):
        os.system("cls")

class Tavern(Location_Base):
    item_list = [
        {"name": "Cheese", "price": 10, "weight": 5, "item_type": CommonItem},
        {"name": "Beer", "price": 13, "weight": 3, "item_type": CommonItem},
        {"name": "Sword", "price": 45, "weight": 14, "item_type": WeaponItem},
        {"name": "Hammer", "price": 65, "weight": 35, "item_type": WeaponItem},
    ]

    def __init__(self, name, game_instance):
        # attributes can be created only in __init__
        self._shop_list = []

        super().__init__(name, game_instance)

    def _create(self):
        for item_data in self.item_list:
            item_object = item_data["item_type"](item_data["name"], item_data["price"], item_data["weight"])
            self._shop_list.append(item_object)

    def enter(self):
        super().enter()

        print(f"Wellcome {self._player} in the {self._name} tavern.")
        time.sleep(1)

        print("If you have gold you can buy a dring")
        print("1 Buy a dring")
        print("2 Exit tavern")

        response = input()

        if response == "1":
            print("You buy a drink")
            input()
        else:
            self._game_instance.village.enter()

class Village(Location_Base):
    def enter(self):
        super().enter()

        print(f"Wellcome {self._player} in {self._name} willage.")
        time.sleep(1)

        print("There is a neerby tavern.")
        print("1 Go to the tavern")
        print("2 Go back to the forest")
        print("3 Exit game")

        response = input()

        if response == "1":
            print("You enter the tavern.")
            time.sleep(2)
            self._game_instance.tavern.enter()
        elif response == "2":
            print("You enter the forest")
            time.sleep(2)
            self._game_instance.forest.enter()
        else:
            print("Exit game")

class Forest(Location_Base):
    def enter(self):
        super().enter()

        print("You entered into a dark forest.")
        time.sleep(1)
        print("You hear something from a nearby bush.")
        time.sleep(3)

        print("Something attacks yout. What do you do?")
        print("1. You run back to the village")
        print("2. Fight for your life")

        response = input()

        if response == "1":
            self._game_instance.village.enter()
        elif response == "2":
            print("Fight!!!")
            input()