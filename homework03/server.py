import time
import requests
import json

from flask import Flask, request, abort

app = Flask(__name__)

db = [
    {
        'time': time.time(),
        'name': 'Тимур',
        'text': 'Привет! Меня зовут Тимур, я владелец этого чата! Очень рад видеть тебя здесь. Если хочешь получить анекдот(на английском), напиши /anecdote',
    },
]

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/status")
def status():
    users = []
    for message in db:
        if message['name'] not in users:
            users.append(message['name'])
    return {
        'name': 'Messenger',
        'status': True,
        'time': time.asctime(),
        'Number of messages': len(db),
        'Number of users': len(users),
        'Users': users
    }

@app.route("/send", methods=['POST'])
def send_message():
    data = request.json
    if not isinstance(data, dict):
        return abort(400)
    if 'name' not in data or 'text' not in data:
        return abort(400)

    name = data['name']
    text = data['text']

    if not isinstance(name, str) or not isinstance(text, str) or name == '' or text == '':
        return abort(400)

#   Шутки на английском языке! Чтобы их перевести, нужен API ключ, с этим я не стал разбираться
    if text == '/anecdote':
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        joke = json.loads(response.content)

        message = {
            'time': time.time(),
            'name': 'Bot',
            'text': f"{joke['setup']} {joke['punchline']}",
        }
    else:
        message = {
            'time': time.time(),
            'name': name,
            'text': text,
        }
    db.append(message)
    return {'ok': True}

@app.route("/messages")
def get_messages():
    """messages from db after given timestamp"""
    try:
        after = float(request.args['after'])
    except:
        return abort(400)
    result = []
    for message in db:
        if message['time'] > after:
            result.append(message)
            if len(result) >= 100:
                break

    return {'messages': result}

app.run()
