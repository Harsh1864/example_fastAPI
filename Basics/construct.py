# class details:
#     def __init__(self):
#         print("Hello world!")

# obj = details()


class details:
    def __init__(self,n1,n2):
          self.n1 = n1
          self.n2 = n2
    
    def detail(self):
         print(f"{self.n1} + {self.n2} = {self.n1+self.n2}")

n1 = int(input("Enter a number:"))
n2 = int(input("Enter a number:"))
obj = details(n1,n2)
obj.detail()

    
