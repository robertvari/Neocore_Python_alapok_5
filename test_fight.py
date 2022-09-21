from game_assets.items import WeaponItem, ArmorItem, CommonItem
from game_assets.characters import Player, AIPlayer


player = Player()
enemy = AIPlayer()

# create items
cheese = CommonItem("Cheese", 1, 10)
shield = ArmorItem("Shield", 1, 5)
sword = WeaponItem("Sword", 1, 30)

player.add_to_inventory(cheese)
player.add_to_inventory(shield)
player.add_to_inventory(sword)