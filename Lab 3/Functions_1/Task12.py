def histogram(lst):
    for i in lst:
        for j in range(0, i):
            print("*",end = "") 
        print()  
print(histogram([1, 2, 5]))
    