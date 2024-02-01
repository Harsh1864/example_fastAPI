import asyncio
import requests

async def function1():
  print("Fun1")
  URL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcReoXuej2Zduv7Z-JonPgTDhX-R8J2DPh15PeE4dom-nQ&s"
  response = requests.get(URL)
  open("instagram.ico", "wb").write(response.content)


async def function2():
  print("Fun2")
  URL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcReoXuej2Zduv7Z-JonPgTDhX-R8J2DPh15PeE4dom-nQ&s"
  response = requests.get(URL)
  open("instagram.ico", "wb").write(response.content)


async def function3():
  print("Fun3")
  URL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcReoXuej2Zduv7Z-JonPgTDhX-R8J2DPh15PeE4dom-nQ&s"
  response = requests.get(URL)
  open("instagram.ico", "wb").write(response.content)

async def main():
   l = await asyncio.gather(
     function1(),
     function2(),
     function3(),
   )
   print(l)

asyncio.run(main())
