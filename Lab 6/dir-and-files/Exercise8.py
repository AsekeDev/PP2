import os
def delete_file(file_path):
    if os.path.exists(file_path):
         os.remove(file_path)
    else:
        print("The file is not exists.")
        
file_path = input("Enter a path of file: ")
delete_file(file_path)