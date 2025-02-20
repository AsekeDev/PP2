import re

strings = ["hello", "a_b", "Python", "ACB", "alj!@#$%^&*KHL*b"]

pattern = r"^[a].*[b]$"

for string in strings:
    if re.fullmatch(pattern, string):
        print(f"{string} matches with the pattern")
    else:
        print(f"{string} doesn't matches with the pattern")