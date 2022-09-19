from game_assets.items import CommonItem, WeaponItem
from game_assets.characters import Player

player = Player()

beer = CommonItem("Beer", 10, 10)
cheese = CommonItem("Cheese", 34, 5)
Sword = CommonItem("Sword", 65, 4)

player.buy(beer)
player.buy(cheese)
player.buy(Sword)