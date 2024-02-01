import requests
from bs4 import BeautifulSoup

# responce = requests.get('http://www.google.com')
# print(responce.text)

# soup = BeautifulSoup(responce.text, 'html.parser')
# print(soup.prettify())

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": 'harry',
    "body": 'bhai',
    "userId": 12,

    
  } 
headers =  {
    'Content-type': 'application/json; charset=UTF-8',
  }
response = requests.post(url, headers=headers, json=data)

print(response.text)
print(response.content)