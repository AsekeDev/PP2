def is_prime(n):
    if n < 2:
        return False 
    for i in range(2, int(n ** 0.5) + 1): 
        if n % i == 0:
            return False
    return True     
def filter_prime(list):
    return [num for num in list if is_prime(num)]
list_of_numbers = list(map(int, input("Write numbers with spaces: ").split()))
filtered_list = filter_prime(list_of_numbers)
print(filtered_list)