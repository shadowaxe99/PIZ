```python
import datetime
import pytz

class SchedulingAgent:
    def __init__(self):
        self.timezone = pytz.timezone('UTC')

    def schedule(self, response):
        if response['action'] == 'schedule':
            schedule_time = datetime.datetime.now(self.timezone) + datetime.timedelta(days=1)
            return {
                'action': 'scheduled',
                'schedule_time': schedule_time.strftime('%Y-%m-%d %H:%M:%S %Z%z'),
                'message': 'The event has been scheduled for ' + schedule_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')
            }
        else:
            return {
                'action': 'error',
                'message': 'Invalid action for scheduling agent'
            }
```