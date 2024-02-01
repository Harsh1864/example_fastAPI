class Emp:
    company = "apple"
    def show(self):
        print(f"my name is {self.name} and my company name is {self.company}")
    
    @classmethod
    def changecompany(cls,newcom):
        cls.company = newcom

e = Emp()
e.name = "harsh"
e.show()
e.changecompany("amazon")
e.show()