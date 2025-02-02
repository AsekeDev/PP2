def palindrome(s):
    letters = list(s)
    reversed_letters = letters[::-1]
    if(letters == reversed_letters):
        return True
    else:
        return False
s = input("Write a word: ")
print(palindrome(s))