with open("File1.txt", "r", encoding="utf-8") as file:
    global contents
    contents = file.read()
    
with open("File2.txt","w", encoding="utf-8") as file:
    file.write(contents)