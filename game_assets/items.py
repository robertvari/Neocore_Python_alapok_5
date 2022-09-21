class Item_Base:
    def __init__(self, name, price, weight, modifier=10):
        self._name = name
        self._price = price
        self._weight = weight
        self._modifier = modifier
        self._item_type = None

    def use(self, character):
        print("USE CALLED IN BASE CLASS. OVERIDE THIS")

    @property
    def price(self):
        return self._price

    @property
    def item_type(self):
        return self._item_type

    @property
    def weight(self):
        return self._weight

    @property
    def stats(self):
        print(f"Name: {self._name}")
        print(f"Price: {self._price}")
        print(f"Weight: {self._weight}")

    def __str__(self):
        return self._name

    def __repr__(self):
        return self._name


class CommonItem(Item_Base):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price, weight)
        self._item_type = "common"

    def use(self, character):
        print(f"{character} eats {self}")
        character.heal(self._modifier)

class ArmorItem(Item_Base):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price, weight)
        self._item_type = "armor"
    
    def use(self, character):
        print(f"{character} parry {self._modifier} damage with {self}")

class WeaponItem(Item_Base):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price, weight)
        self._item_type = "weapon"
    
    def use(self, owner, enemy):
        print(f"{owner} attacks {enemy} with {self}")
        enemy.take_damage(owner.attack_strength + self._modifier)
