import os
def check_path(path):
    if not os.path.exists(path):
        print("The path is not exist")
        return

    print("The path is exist")
    
    if os.access(path, os.R_OK):
        print("Readability: Yes")
    else:
        print("Readability: No")
        
    if os.access(path, os.W_OK):
        print("Writability: Yes")
    else:
        print("Writability: No")
   
    if os.access(path, os.X_OK):
        print("Executability: Yes")
    else:
        print("Executability: No")
    
path = input("Enter a path: ")
check_path(path)