try:
   n = int(input("Enter a number: "))
   for i in range(11):
      
      print(f"{n} X {i} = {n*i}")
except ValueError:
   print("value error")
  

