import time 
import math

def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms/1000)
    sqrt_number = math.sqrt(number)
    print(f"Square root of {number} after {delay_ms} miliseconds is {sqrt_number}")
    
number = int(input("Enter a number: "))
ms = int(input("Enter a miliseconds: "))
delayed_sqrt(number, ms)
    