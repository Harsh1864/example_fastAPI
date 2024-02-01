class employee:
    # def __init__(self,name):
    #     self.name = name
    name = "harsh"
    def __len__(self):
        i=0
        for c in self.name:
         i = i + 1
        return i
    # def __str__(self):
    #     return f"my name is {self.name} str"
    
    # def __repr__(self):
    #     return f"my name is {self.name} repr"
    
e = employee()
print(len(e))
