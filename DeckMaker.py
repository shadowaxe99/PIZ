```python
class DeckMaker:
    def __init__(self):
        self.deck = None
        self.DeckSchema = None

    def generate_deck(self):
        # Implement the logic to generate the deck
        # This is a placeholder for the actual implementation
        self.deck = "Generated Deck"

        # After generating the deck, store it in Google Drive
        self.store_deck()

    def store_deck(self):
        # Import the GoogleDrive class from the GoogleDrive.py file
        from GoogleDrive import GoogleDrive

        # Create an instance of the GoogleDrive class
        google_drive = GoogleDrive()

        # Call the store_deck function of the GoogleDrive class
        google_drive.store_deck(self.deck, self.DeckSchema)
```
This code defines a class `DeckMaker` with two methods: `generate_deck` and `store_deck`. The `generate_deck` method generates a deck and stores it in Google Drive by calling the `store_deck` method. The `store_deck` method imports the `GoogleDrive` class from the `GoogleDrive.py` file, creates an instance of the `GoogleDrive` class, and calls the `store_deck` method of the `GoogleDrive` class.