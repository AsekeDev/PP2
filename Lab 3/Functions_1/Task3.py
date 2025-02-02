def solve(numheads, numlegs):
    R = numheads - 1
    C = 1
    while(R + C == numheads and (R * 4 + C * 2) != numlegs):
        R -= 1
        C += 1
    print(f"Chicken: {C}" )
    print(f"Rabbits: {R}" )
        
numheads = int(input("Number of heads: "))
numlegs = int(input("Number of legs: "))
solve(numheads, numlegs)