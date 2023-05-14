import random
import datetime
import time

d = {
    'time': '12-02-2023',
    'name': 'Timur'
}

db = [
    {
        'time': time.time(),
        'name': 'Timur',
        'text': 'Привет!',
    },
    {
        'time': time.time(),
        'name': 'Mary',
        'text': 'Привет! Как дела?',
    }
]

# send message
# get message

def send_message(name, text):
    message = {
        'time': time.time(),
        'name': name,
        'text': text,
    }
    db.append(message)

def get_messages(after):
    """messages from db after given timestamp"""
    result = []
    for message in db:
        if message['time'] > after:
            result.append(message)
    return result

print(db)
t1 = db[-1]['time']
print(get_messages(t1))

send_message('123', '123')
send_message('123', '456')
print(get_messages(t1))

# print('-' * 50)

# for message in db:
#     print(message['time'], message['name'])
#     print(message['text'])
#     print()
#
# print(db)