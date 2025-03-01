import os
def list_directories(path):
    return[d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
def list_files(path):
    return[f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
def list_all(path):
    return os.listdir(path)

path = input("Enter a path: ")

print("Directories: ", list_directories(path))
print("Files: ", list_files(path))
print("All elements: ", list_all(path))
