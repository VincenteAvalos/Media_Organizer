import os
import sys
import time


# class count:
#     amount = 0
#     def FoldersMade(amount):
#         return amount
#     def FilesMoved(amount):
#         return amount


def Folder_Made(count):
    return count


def MoveFiles(file, folder_name):
    os.system('cls')
    print("Files Transfering...")
    path = os.getcwd()
    os.rename(f"{path}\\{file}", f"{path}\\{folder_name}\\{file}")


def MakeFolder(file_type, file, folder_name):  # Creates the folder with exception rule
    count = 0
    try:
        count += 1
        os.mkdir(folder_name)
        os.system('cls')
        print(f"Folder(s) made ({Folder_Made(count)}) ")  # How many folders created
        file_type.append(file)
    except FileExistsError:
        MoveFiles(file, folder_name)  # Moves files into correct folder
        file_type.append(file)


def ArangeFiles():
    files = os.listdir()
    png = []
    jpg = []
    mp4 = []
    mov = []
    ect = []
    for file in files:  # Creates folders for each file type
        if ".PNG" in file:
            MakeFolder(png, file, "PNG_")
        elif ".JPG" in file:
            MakeFolder(jpg, file, "JPG_")
        elif ".MP4" in file:
            MakeFolder(mp4, file, "MP4_")
        elif ".MOV" in file:
            MakeFolder(mov, file, "MOV_")
        elif ".JPEG" in file:
            MakeFolder(jpg, file, "JPEG_")
        elif ".AAE" in file:
            os.remove(file)
            print(f"{file} deleted *")
        elif "." in file:  # If file type is not recognized create a new folder
            while True:
                answer = input(
                    f"'{file}' is not recognized...Create a new folder? (y/n)"
                )
                if answer == "y":
                    folder_name = input("Enter the name for the folder: \n").lower()
                    MakeFolder(ect, file, folder_name)
                    break
                elif answer == "n":
                    print(" >> Action Cancelled...\n >> No Folder was created...\n\n")
                    break
                print("Please choose an option: (y/n)\n")
        else:
            # print(f"{file} is folder?")
            None


def OrganizeFolder(folder_path):  # Changes new working directory to inside folder
    folder_dir = os.getcwd()
    print(f"'{folder_path}' contents:\n")
    os.chdir(f"{folder_dir}\\{folder_path}")
    print(f"{os.listdir()}\n")
    ArangeFiles()  # Aranges file types in new funtion


def Work_Dir():  # Changes Working Directory
    file_path = input("Please Paste in the directory: \n\n")
    os.chdir(file_path)
    folder = os.listdir()
    print(os.listdir())
    print("Changing path...\n")
    for folders in folder:  # Gets list of folders in Directory and scans each one
        try:
            OrganizeFolder(folders)  # Calls new function to Organize the files
            os.chdir(file_path)
        except NotADirectoryError:
            print(f"-- '{folders}': Is not a directory --\n")


# Calls funtion to change to directory
if __name__ == "__main__":
    while True:
        try:
            Work_Dir()
            print("*Process Finished*\n__________")
            break
        except FileNotFoundError:
            print(os.getcwd())
            print("--Not a directory--\nTry again...\n")
            break
