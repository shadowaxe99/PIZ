```python
from ResponseHandler import handle_response

class ResponseManagementSystem:
    def __init__(self):
        self.response = None

    def capture_response(self, response):
        self.response = response
        handle_response(self.response)
```