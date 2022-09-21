import random, time, os

class Character_Base:
    race_list = {
        "human": {"strength": 20, "max_HP": 50},
        "ork": {"strength": 100, "max_HP": 130},
        "elf": {"strength": 30, "max_HP": 80},
        "dwarf": {"strength": 150, "max_HP": 130},
    }

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
        self._race = random.choice(list(self.race_list))
        self._max_HP = self.race_list[self._race]["max_HP"]
        self._current_HP = self._max_HP
        self._strength = self.race_list[self._race]["strength"]
        self._name = self.get_fantasy_name()
    
    def buy(self, item):
        if self._golds < item.price:
            print(f"You don't have enough gold to buy a {item}")
            print(f"{item} price: {item.price}")
            print(f"My golds: {self._golds}")
            time.sleep(3)
            return

        if self.inventory_weight + item.weight > self._strength:
            print("Inventory is heavy :(")
            print(f"Inventory weight: {self.inventory_weight}")
            time.sleep(3)
            return

        print(f"{self._name} bought {item}")
        time.sleep(1)
        self._inventory.append(item)
        self._golds -= item.price
        print(f"You have {self._golds} golds left in your pocket.")
        time.sleep(1)

    def add_to_inventory(self, item):
        if self.inventory_weight + item.weight > self._strength:
            print("Inventory is heavy :(")
            print(f"Inventory weight: {self.inventory_weight}")
            time.sleep(3)
            return
        
        print(f"{self} take {item}")
        self._inventory.append(item)

    def attack(self, other):
        self._clear_screen()
        print(f"{self} attacks {other}")
        time.sleep(1)
        attack_strength = random.randint(0, self._strength)

        # TODO add weapon strength if we are holding eny

        if not attack_strength:
            print(f"{self} misses... :((")
            time.sleep(2)
        else:
            if attack_strength == self._strength:
                print(f"{self} deals a critical hit to {other}!!!")
            else:
                print(f"{self} hits {other} with {attack_strength} strength.")

            time.sleep(2)
            other.take_damage(attack_strength)
    
    def take_damage(self, damage):
        # TODO reduce damage if we have shield in our left hand
        self._current_HP -= damage

        if self._current_HP <= 0:
            self._clear_screen()
            print(f"RIP {self}")
            time.sleep(5)

    def _clear_screen(self):
        os.system("cls")

    @property
    def is_alive(self):
        return self._current_HP > 0

    @property
    def inventory_weight(self):
        return sum([item.weight for item in self._inventory])

    @staticmethod
    def get_fantasy_name():
        FIRST = ['A', 'Ag', 'Ar', 'Ara', 'Anu', 'Bal', 'Bil', 'Boro', 'Bern', 'Bra', 'Cas', 'Cere', 'Co', 'Con',
                 'Cor', 'Dag', 'Doo', 'Elen', 'El', 'En', 'Eo', 'Faf', 'Fan', 'Fara', 'Fre', 'Fro', 'Ga', 'Gala', 'Has',
                 'He', 'Heim', 'Ho', 'Isil', 'In', 'Ini', 'Is', 'Ka', 'Kuo', 'Lance', 'Lo', 'Ma', 'Mag', 'Mi', 'Mo',
                 'Moon', 'Mor', 'Mora', 'Nin', 'O', 'Obi', 'Og', 'Pelli', 'Por', 'Ran', 'Rud', 'Sam', 'She', 'Sheel',
                 'Shin', 'Shog', 'Son', 'Sur', 'Theo', 'Tho', 'Tris', 'U', 'Uh', 'Ul', 'Vap', 'Vish', 'Ya', 'Yo', 'Yyr']

        SECOND = ['ba', 'bis', 'bo', 'bus', 'da', 'dal', 'dagz', 'den', 'di', 'dil', 'din', 'do', 'dor', 'dra',
                  'dur', 'gi', 'gauble', 'gen', 'glum', 'go', 'gorn', 'goth', 'had', 'hard', 'is', 'ki', 'koon', 'ku',
                  'lad', 'ler', 'li', 'lot', 'ma', 'man', 'mir', 'mus', 'nan', 'ni', 'nor', 'nu', 'pian', 'ra', 'rak',
                  'ric', 'rin', 'rum', 'rus', 'rut', 'sek', 'sha', 'thos', 'thur', 'toa', 'tu', 'tur', 'tred', 'varl',
                  'wain', 'wan', 'win', 'wise', 'ya']

        return f"{random.choice(FIRST)}{random.choice(SECOND)}"

    @property
    def stats(self):
        print("-"*25, f"{self._name}", "-"*25,)
        print(f"Race: {self._race}")

        print("-"*25, "Inventory", "-"*25,)

        print(f"Golds: {self._golds}")
        print(f"Inventory: {self._inventory}")
        print(f"Weight: {self.inventory_weight}")
        print(f"Left Hand: {self._left_hand}")
        print(f"Right Hand: {self._right_hand}")

        print("-"*25, "Combat Stats", "-"*25,)

        print(f"Strength: {self._strength}")
        print(f"Initiative: {self._initiative}")
        print(f"Max HP: {self._max_HP}")
        print(f"Current HP: {self._current_HP}")

    def __str__(self) -> str:
        return self._name

    def __repr__(self):
        return self._name


class Player(Character_Base):
    def _create(self):
        self._name = "Robert"
        self._race = "human"

        while not self._race in self.race_list:
            print("Wrong race. Try again.")
            self._race = input(f"What is your race: {list(self.race_list)}")
        
        self._max_HP = self.race_list[self._race]["max_HP"]
        self._current_HP = self._max_HP
        self._strength = self.race_list[self._race]["strength"]

class AIPlayer(Character_Base):
    pass


if __name__ == "__main__":
    player = Player()
    enemy = AIPlayer()

    winner = None
    while True:        
        # enemy attacks player
        enemy.attack(player)
        if not player.is_alive:
            winner = enemy
            break
        
        # player attacks enemy
        player.attack(enemy)
        if not enemy.is_alive:
            winner = player
            break
    
    os.system("cls")
    print(f"{winner} wins the fight")