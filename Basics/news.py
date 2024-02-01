import requests
import json
# from bs4 import BeautifulSoup
# query = input("what type of news you read:")
response = requests.get(f'https://pokeapi.co/api/v2/pokemon/ditto')
news = json.loads(response.text)
# i=1
# print(news['subcategory'])
# for article in news["recordList"]:
#     print(article['category'])
#     if article['category']== "Food":
#         print(article['subcategory'])
    # if article['subcategory']:
    #   print(f"{i}" , article['subcategory'])
    #   i = i+1
    # else:
    #    print(f"{i} data is empty")
    #    i = i+1

print(news)