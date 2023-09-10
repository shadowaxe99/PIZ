```python
from ResponseYes import schedule
from ResponseNo import nudge
from ResponseNone import follow_up

class ResponseHandler:
    def __init__(self):
        self.response = None

    def handle_response(self, response):
        self.response = response
        if self.response == "Yes":
            schedule()
        elif self.response == "No":
            nudge()
        else:
            follow_up()
```