from game_assets.locations import Tavern

class DummyGame:
    def __init__(self):
        self.player = None

tavern = Tavern("Black Horse", DummyGame())