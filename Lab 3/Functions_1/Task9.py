import math
number_pi = math.pi
def volume_of_sphere(r):
    print(4/3*number_pi*(r**3))

r = int(input("Write a radius of sphere: "))
volume_of_sphere(r)