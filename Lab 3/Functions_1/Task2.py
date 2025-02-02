def F_to_C(F):
    C = (5 / 9) * (F - 32)
    print(f"Equivalent temperature in Celsius: {C}°С")
F = float(input("Enter temperature in Fahrenheit: "))
F_to_C(F)