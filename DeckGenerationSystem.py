import DeckMaker

class DeckGenerationSystem:
    def __init__(self):
        self.deck_maker = DeckMaker()

    def generate_deck(self):
        deck = self.deck_maker.generate_deck()
        return deck