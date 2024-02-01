class animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("axakjksvjhvavdhfhsdfkajdkfasdkjfb")

class dog(animal):
    def __init__(self,name,breed):
        animal.__init__(self,name,species="dog")
        self.breed = breed

    def make_sound(self):
        print("asdbasdasda")

d = dog("dog","asdssd")
print(d.name)
print()
d.make_sound()