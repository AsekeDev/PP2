def unique_elements(lst):
    unique_list = []
    for i in lst:  
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

print(unique_elements([1, 2, 2, 3, 4, 4, 5, 6, 6, 6]))