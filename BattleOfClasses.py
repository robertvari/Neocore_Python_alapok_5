import os, time
from game_assets.characters import Player
from game_assets.locations import Tavern, Forest, Village


class BattleOfClasses:
    def __init__(self) -> None:
        self.clear_screen()
        self.intor()
        time.sleep(3)

        self.player = Player()

        self.village = Village("Whiterun", self)
        self.tavern = Tavern("Black Horse", self)
        self.forest = Forest("Dark Forest", self)
        
        self.village.enter(self.player)
    
    def intor(self):
        print("="*50, "BATTLE OF CLASSES", "="*50)

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

BattleOfClasses()