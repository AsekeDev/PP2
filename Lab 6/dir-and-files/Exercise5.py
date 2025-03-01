my_list = ["Python", "C++", "Java", "C#", "JavaScript"]

with open("result.txt", "w", encoding="utf-8") as file:
    for item in my_list:
        file.write(item + "\n")
        
with open("result.txt", "r",encoding="utf-8") as file:
    elements = file.read()
    print(elements)
    