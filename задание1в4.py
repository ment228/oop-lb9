class rectangle:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def get_area(self):
        return self.a*self.b

class square:
    def __init__(self,a):
        self.a = a
    def get_area(self):
        return self.a**2

class circle:
    def __init__(self,r):
        self.r = r
    def get_area(self):
        return 3.14*self.r**2

rect1 = rectangle(3,4)
rect2 = rectangle(12,3)
print(rect1.get_area(),rect2.get_area())
sq1 = square(2)
print(sq1.get_area())
cirl = circle(3)
figure = [rect1,rect2,sq1,cirl]
for figure in figure:
    print(figure.get_area())