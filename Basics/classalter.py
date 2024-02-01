# class emp:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def fromstr(cls,string):
#         return cls(string.split("-")[0],string.split("-")[1])
# e = emp("harsh",18)
# print(f"{e.name} and {e.age}")

# string = "harsddssdh-18"
# e1 = emp.fromstr(string)
# print(e1.name)
# print(e1.age)

class Person:
    # Class variable
    total_people = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.total_people += 1

    # Class method as an alternative constructor
    @classmethod
    def create_person(cls, name_and_age):
        name, age = name_and_age.split(',')
        return cls(name, int(age))

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating instances using the regular constructor
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Creating an instance using the class method as an alternative constructor
person3 = Person.create_person("Charlie,35")

# Displaying information for all instances
person1.display_info()
person2.display_info()
person3.display_info()

# Displaying the total number of people
print(f"Total People: {Person.total_people}")
