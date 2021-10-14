import requests
URL = 'https://www.googleapis.com/books/v1/volumes'
DATA = {'q': 'Hobbit'}
r = requests.get(URL, DATA)
print(r.json())
