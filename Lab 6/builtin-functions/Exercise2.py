def count_letters(text):
    up_count = sum(1 for char in text if char.isupper())
    low_count = sum(1 for char in text if char.islower())
    print(f"Count of uppercase letters: {up_count}")
    print(f"Count of lowercase letters: {low_count}")
    
text = input()
count_letters(text)