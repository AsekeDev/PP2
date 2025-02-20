import re

strings = ["Hello, world", "a b", "Python", "ACB", ",Test."]

pattern = r"[ ,.]"

replacement = ":"

for string in strings:
    new_string = re.sub(pattern, replacement, string)
    print(f"Before: {string} | After: {new_string}")