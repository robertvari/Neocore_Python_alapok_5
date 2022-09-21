from game_assets.items import WeaponItem, ArmorItem, CommonItem
from game_assets.characters import Player, AIPlayer


player = Player()
enemy = AIPlayer()

# create items
cheese = CommonItem("Cheese", 1, 1)

shield = ArmorItem("Shield", 1, 1)
magic_shield = ArmorItem("Magic Shield", 1, 1)
sword = WeaponItem("Sword", 1, 1)
hammer = WeaponItem("Hammer", 1, 1)

player.add_to_inventory(sword)
player.attack(enemy)