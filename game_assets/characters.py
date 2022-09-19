import random

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

        self._name = ""
    
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