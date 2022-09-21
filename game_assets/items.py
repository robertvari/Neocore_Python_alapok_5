class Item_Base:
    def __init__(self, name, price, weight) -> None:
        self._name = name
        self._price = price
        self._weight = weight
        self._item_type = None

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

class ArmorItem(Item_Base):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price, weight)
        self._item_type = "armor"

class WeaponItem(Item_Base):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price, weight)
        self._item_type = "weapon"

