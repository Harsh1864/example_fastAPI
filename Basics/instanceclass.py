class abc:
    company = "volvo"
    def __init__(self,name):
      self.name = name

    def show(self):
       print(f"my name is : {self.name} my company is : {self.company}")

n = input("Enter name:")
a = abc(n)
b= abc(n)
a.company = "mahindra"
a.show()
b.show()
