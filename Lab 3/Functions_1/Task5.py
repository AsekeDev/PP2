from itertools import permutations 
def permutation(s):
    permutation_list = permutations(s)
    for perm in permutation_list:
        print("".join(perm))
        
s = input("Write a string:") 
permutation(s)