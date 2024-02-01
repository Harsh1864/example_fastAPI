class cal:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def area(self):
        return self.x*self.y
    
class cir(cal):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        super().__init__(self.radius,self.radius)
        return 3.14 * super().area()
        
c = cir(6)
a =c.area()
print(a)