# -*- coding = utf-8 -*-
# Worker : HAN XIA
# Motto : Practice makes perfect.
# Time : 23/8/2023 9:36 am


#Sort files based on their different types (extensions)

import os
import shutil

#Create a folder that is named after the extension of the file passed in
def create_folder(path: str, extension: str) -> str:
    folder_name: str = extension[1:] # pass the dot.
    folder_path: str = os.path.join(path, folder_name)
    #The os.path.join function provides a way to construct paths in a platform-independent manner(Linux: / Windows:\)
    #and combines these two strings into a full path that points to the desired folder within the directory

    if not os.path.exists(folder_path):
    # It's checking if the directory path stored in folder_path exists or not.
        os.makedirs(folder_path)

    return folder_path

def sort_files(source_path: str):
    #Sorted files based on a given path.
    for root_dir, sub_dir, filenames in os.walk(source_path):
        #os.walk() generates a 3-tuple for each directory it visits:
        # root_dir : The name of the directory. (string)
        # sub_dir: A list of the names of the subdirectories in that directory.
        # filename: A list of the filenames in that directory.
        for filename in filenames:
            file_path: str = os.path.join(root_dir, filename)
            #Create a new file in the current dir(root_dir) and filename from filenames.
            extension: str = os.path.splitext(filename)[1]
            #The function os.path.splitext() splits the filename into a tuple with two parts:
            # the base name and the extension.
            # [1] gets the extension part.

            if extension:
                target_folder: str = create_folder(source_path, extension)
                target_path: str = os.path.join(target_folder, filename)

                shutil.move(file_path, target_path)


#Removes all empty folders:
def remove_empty_folders(source_path: str):
    for root_dir, sub_dir, filenames in os.walk(source_path, topdown=False):
        #topdown=false means os will reverse the process, checking sub_dir firstly, then root_dir
        for current_dir in sub_dir:
            folder_path: str = os.path.join(root_dir,current_dir)

            if not os.listdir(folder_path):
                os.remove(folder_path)


def main():
    user_input: str = input("Please provide a file path to sort: ")
    if os.path.exists(path=user_input):
        sort_files(user_input)
        remove_empty_folders(user_input)
        print('Files sorted successfully')
    else:
        print('Invalid path, please provide a valid file path')


if __name__ == '__main__':
    main()


