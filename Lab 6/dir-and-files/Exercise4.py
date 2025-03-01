file_path = input("Enter a path: ")

with open(file_path, 'r', encoding='utf-8') as file:
    print("Number of lines:", len(file.readlines()))