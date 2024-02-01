# class parent:
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id

# class child(parent):
#     def emp(self):
#         super().__init__(self.name,self.id)
#         pass

# c = child("bhautik",19)
# # p = parent("harsh",20)
# print(len(c.name))
# # print(c.id)


class ParentClass:
    def parent_method(self):
        print("This is the parent method.")

class ChildClass(ParentClass):
    def child_method(self):
        print("This is the child method.")
        super().parent_method()

child_object = ChildClass()
child_object.child_method()