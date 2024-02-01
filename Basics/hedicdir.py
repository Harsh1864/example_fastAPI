# x = [1,2,3]
# print(dir(x))

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p = person("harsh",18)
print(p.__dict__)

help(p)