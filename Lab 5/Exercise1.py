import re

strings = ["ab", "cb", "abbb", "abb", "ba"]

pattern = r"ab*"

for string in strings:
    if re.fullmatch(pattern, string):
        print(f"{string} matches with the pattern")
    else:
        print(f"{string} doesn't matches with the pattern")


