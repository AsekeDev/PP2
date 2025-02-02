class Shape:
    def Area(self):
        return 0
    
class square(Shape):
    def __init__(self, length):
        self.length = length
    def Area(self):
        return self.length ** 2
    
n = float(input("n="))
myshape = Shape()
mysquare = square(n)
print("Square Area: ", mysquare.Area())
print("Other: ", myshape.Area())