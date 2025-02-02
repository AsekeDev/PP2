def spy_game(nums):
    counter = 0 
    for num in nums:  
        if num == 0 and counter < 2: 
            counter += 1
        elif num == 7 and counter == 2:  
            return True  
    return False  

print(spy_game([1,2,0,1,0,1,0]))