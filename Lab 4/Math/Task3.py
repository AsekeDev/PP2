import math
def regular_polygon_area(n, length):
    return int((n * length **2)/(4 * math.tan(math.pi/n)))

n = int(input("Input number of sides: "))

length = int(input("Input the length of a side: "))

print(regular_polygon_area(n, length))