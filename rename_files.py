import os
def rename_files():
    file_path = "D:\Desktop\Secret"
    file_list = os.listdir(file_path)
    print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directoy is "+saved_path)
    os.chdir(file_path)
    for file_name in file_list:
        print(file_name)
        new_file_name = ""
        numbers = "0123456789"
        for char in file_name:
            if char not in numbers:
                new_file_name += char
        os.rename(file_name, new_file_name)

    os.chdir(saved_path)

rename_files()
    
    
