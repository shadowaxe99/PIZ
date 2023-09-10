```python
from EmailAgent import EmailAgent

class EmailSystem:
    def __init__(self):
        self.email_agent = EmailAgent()

    def process_email(self, deck):
        self.email_agent.retrieve_deck(deck)
        self.email_agent.send_email()
```