import re

strings = ["a_b", "f-c", "A-C", "hello_world"]

pattern = r"^[a-z]+_[a-z]+$"

for string in strings:
    if re.fullmatch(pattern, string):
        print(f"{string} matches with the pattern")
    else:
        print(f"{string} doesn't matches with the pattern")