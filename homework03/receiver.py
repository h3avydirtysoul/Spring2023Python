import time
import requests
from datetime import datetime

def print_messages(message):
    t = message['time']
    dt = datetime.fromtimestamp(t)
    dt = dt.strftime('%H:%M:%S')
    print(dt, message['name'])
    print(message['text'])
    print()

after = 0

while True:
    response = requests.get('http://127.0.0.1:5000/messages', params={'after': after})
    messages = response.json()['messages']
    for message in messages:
        print_messages(message)
        after = message['time']

    time.sleep(1)