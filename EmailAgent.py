```python
import SendEmail
from GoogleDrive import retrieve_deck

class EmailAgent:
    def __init__(self):
        self.email = None
        self.deck = None

    def retrieve_deck(self):
        self.deck = retrieve_deck()

    def prepare_email(self, recipient, subject, body):
        self.email = {
            "recipient": recipient,
            "subject": subject,
            "body": body,
            "attachment": self.deck
        }

    def send_email(self):
        SendEmail.send_email(self.email)
```