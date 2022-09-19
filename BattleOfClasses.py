import os

class BattleOfClasses:
    def __init__(self) -> None:
        self.clear_screen()
        self.intor()
    
    def intor(self):
        print("="*50, "BATTLE OF CLASSES", "="*50)

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

BattleOfClasses()