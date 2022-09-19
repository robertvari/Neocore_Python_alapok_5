class Item_Base:
    def __init__(self, name, price, weight) -> None:
        self._name = name
        self._price = price
        self._weight = weight

    @property
    def price(self):
        return self._price

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

    def __rept__(self):
        return self._name

class CommonItem(Item_Base):
    pass

class WeaponItem(Item_Base):
    pass

