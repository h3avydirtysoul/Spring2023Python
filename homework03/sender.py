import requests

# response = requests.get('http://127.0.0.1:5000/status')
# print(response.status_code)
# print(response.text)
# print(response.json()['status'])
#
#
# data = {
#     'name': 'Nick',
#     'text': 'Привет'
# }

name = input('Введите имя: ')

while True:
    text = input('Введите сообщение: ')
    response = requests.post('http://127.0.0.1:5000/send',
    json={
        'name': name,
        'text': text,
    }
)