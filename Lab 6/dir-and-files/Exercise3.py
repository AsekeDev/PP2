import os

def check_path(path):
    if os.path.exists(path):
        print("The path is exists.")
    
        file_name = os.path.basename(path)
        print(f"Name of file: {file_name}")
        
        directory = os.path.dirname(path)
        print(f"Name of directory: {directory}")
    else:
        print("The path is not exists.")
        
path = input("Enter a path: ")
check_path(path)