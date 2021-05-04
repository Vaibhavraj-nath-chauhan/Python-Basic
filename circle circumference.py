class Circle:
    radius = 0
    def __init__(self):
        self.radius = int(input("Enter Radius-->"))
    def getArea(self):
        return ((3.14)*(self.radius**2))
    def getCircumference(self):
        return (2*3.14*self.radius)
    
c1 = Circle()
print("Area is:-->",c1.getArea())
print("Circumference is:-->%.2f"%c1.getCircumference())