def reversed_sentence(s):
    words = s.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

s = input("Write a sentence:")
Result = reversed_sentence(s)
print(Result)
