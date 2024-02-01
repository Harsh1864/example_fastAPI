# class myClass:
#     def __init__(self,value):
#        self._value= value

#     def show(self):
#         print(f"value is:{self._value}")

#     @property
#     def ten_value(self):
#         return 10*self._value
    
#     @ten_value.setter
#     def ten_value(self, new_value):
#         self._value = new_value/10
#         print("set:", self._value)
    
# obj = myClass(10)
# obj.ten_value = 23 
# print(obj._value)
# print(obj.ten_value)
# obj.show()


class MyClass:
    def __init__(self,value):
        self._value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self,new_value):
        self._value = new_value / 10

m1 = MyClass(10)
m1.value = 20
print(m1._value)
print(m1.value)