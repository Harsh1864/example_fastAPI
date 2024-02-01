class father:
    def __init__(self,name,city):
        self.name = name
        self.city = city

    

class mother(father):
    def __init__(self,name,city,mname,hobby):
        father.__init__(self,name,city)
        self.mname = mname
        self.hobby = hobby

    def view(self):
        print(f"My father name is {self.name} and my city is {self.city} mother name is {self.mname} and her hobby is {self.hobby}")

name = input("Father name: ")
city = input("city: ")
mname = input("mother name: ")
hobby = input("mother hobby: ")
m = mother(name,city,mname,hobby)
m.view()