```python
from NudgeOnce import nudge

def handle_no_response(response):
    if response['type'] == 'No':
        nudge(response['email'])
```