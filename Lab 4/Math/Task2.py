def area_of_trapezoid(a, b, h):
    return ((a+b)/2)*h
a = int(input("Base, first value: " ))
b = int(input("Base, second value: " ))
h = int(input("Height: "))

print(area_of_trapezoid(a,b,h))