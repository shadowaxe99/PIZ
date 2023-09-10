```python
# NudgeOnce.py

class NudgeOnce:
    def __init__(self):
        self.response = None

    def nudge(self, response):
        self.response = response
        print("Nudging once for response: ", self.response)
```