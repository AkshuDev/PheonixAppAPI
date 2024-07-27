#    _____              .___       __________            _____   __           .__          ___.   .__
#   /     \ _____     __| _/____   \______   \___.__.   /  _  \ |  | __  _____|  |__   ____\_ |__ |  |__ ___.__._____
#  /  \ /  \\__  \   / __ |/ __ \   |    |  _<   |  |  /  /_\  \|  |/ / /  ___/  |  \ /  _ \| __ \|  |  <   |  |\__  \
# /    Y    \/ __ \_/ /_/ \  ___/   |    |   \\___  | /    |    \    <  \___ \|   Y  (  <_> ) \_\ \   Y  \___  | / __ \_
# \____|__  (____  /\____ |\___  >  |______  // ____| \____|__  /__|_ \/____  >___|  /\____/|___  /___|  / ____|(____  /
#         \/     \/      \/    \/          \/ \/              \/     \/     \/     \/           \/     \/\/          \/
#     ___ ___________                      .___             ___
#    /  / \_   _____/___  __ __  ____    __| _/___________  \  \
#   /  /   |    __)/  _ \|  |  \/    \  / __ |/ __ \_  __ \  \  \
#  (  (    |     \(  <_> )  |  /   |  \/ /_/ \  ___/|  | \/   )  )
#   \  \   \___  / \____/|____/|___|  /\____ |\___  >__|     /  /
#    \__\      \/                   \/      \/    \/        /__/






# __________.__                        .__           _________ __            .___.__
# \______   \  |__   ____  ____   ____ |__|__  ___  /   _____//  |_ __ __  __| _/|__| ____  ______
#  |     ___/  |  \_/ __ \/  _ \ /    \|  \  \/  /  \_____  \\   __\  |  \/ __ | |  |/  _ \/  ___/
#  |    |   |   Y  \  ___(  <_> )   |  \  |>    <   /        \|  | |  |  / /_/ | |  (  <_> )___ \
#  |____|   |___|  /\___  >____/|___|  /__/__/\_ \ /_______  /|__| |____/\____ | |__|\____/____  >
#                \/     \/           \/         \/         \/                 \/               \/

import os
import shutil
import sys
import json
import pathlib
from typing import *
from PheonixAppAPI.bin_worker import BIN

class Large_File_Management_System():
    """A System for managing large amounts of Files.

    Args:
            path (Union[str, list, pathlib.Path, pathlib.PurePath, pathlib.PurePosixPath, pathlib.PosixPath, pathlib.PureWindowsPath, pathlib.WindowsPath]): The Path/Paths of File/Files/Folder/Folders.
            path2 (Union[str, list, pathlib.Path, pathlib.PurePath, pathlib.PurePosixPath, pathlib.PosixPath, pathlib.PureWindowsPath, pathlib.WindowsPath], optional): The second Path/Paths of File/Files/Folder/Folders. Defaults to [].
            content (list, optional): The content of File/Files. Defaults to [''].
            isFile (bool, optional): If the Paths represent Files/File. Defaults to False.
            name (list, optional): The name/names of the Folders/Folder/Files/File. Defaults to [''].
            include_name (bool, optional): To be set to False if the name of the Folders are present in the list else True. Defaults to False.
    """
    def __init__(self, path:Union[list, pathlib.Path, pathlib.PurePath, pathlib.PurePosixPath, pathlib.PosixPath, pathlib.PureWindowsPath, pathlib.WindowsPath], path2:Union[list, pathlib.Path, pathlib.PurePath, pathlib.PurePosixPath, pathlib.PosixPath, pathlib.PureWindowsPath, pathlib.WindowsPath]=[], content:list=[""], isFile:bool=False, name:list=[""], include_name:bool=False) -> None:
        """The initialization of this class.

        Args:
            path (Union[list, pathlib.Path, pathlib.PurePath, pathlib.PurePosixPath, pathlib.PosixPath, pathlib.PureWindowsPath, pathlib.WindowsPath]): The Path/Paths of File/Files/Folder/Folders.
            path2 (Union[str, list, pathlib.Path, pathlib.PurePath, pathlib.PurePosixPath, pathlib.PosixPath, pathlib.PureWindowsPath, pathlib.WindowsPath], optional): The second Path/Paths of File/Files/Folder/Folders. Defaults to [].
            content (list, optional): The content of File/Files. Defaults to [''].
            isFile (bool, optional): If the Paths represent Files/File. Defaults to False.
            name (list, optional): The name/names of the Folders/Folder/Files/File. Defaults to [''].
            include_name[bool, optional]: To be set to False if the name of the Folders are present in the list else True. Defaults to False.
        """

        self.path = path
        self.path2 = path2
        self.content = content
        self.isFile = isFile
        self.name = name
        self.include_name = include_name

        if include_name:
            if len(path) != len(name):
                raise ValueError("The length of [path] must match the length of [name]. [Large_File_Management_System]")
            else:
                for i, v in enumerate(path):
                    path[i] = os.path.join(v, name[i])

        if isFile:
            if len(path) != len(content):
                raise ValueError("The length of [path] must match the length of [content]. [Large_File_Management_System]")
            else:
                pass

    def Make_Folder(self, index:int=0) -> bool:
        """This function will make a Folder on the specified index of the list. If no index is given it will use the first index of the list.

        Args:
            index (int, optional): The index of the path inside the list of paths where the Folder must be created. Defaults to 0.

        Returns:
            bool: True if the operation was successful, False otherwise.
        """

        try:
            os.mkdir(self.path[index])
            return True
        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")
            return False

    def Make_Folders(self, indexes:tuple[int, Union[int, str]]=(0, "max")) -> bool:
        """This function will create Folders in the provided paths inside the provided list.

        Args:
            indexes (tuple[int, Union[int, str]], optional): This defines the number of Folders to create. The first value of the tuple must define from where the Folders should be created and the second value must define till where the Folders should be created (second value can be 'max' to define [till all]). (0, "max").

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        try:
            index_from = indexes[0]
            index_to = str(indexes[1])

            if index_to.isalpha():
                if index_to.lower() == "max":
                    index_to = len(self.path)
                else:
                    print(f"\nWARNING: Invalid [indexes][{indexes[1]}]. Setting it to [{index_from}].[Large_File_Management_System]\n")
                    index_to = index_from

            index_to = int(index_to)

            for i, v in enumerate(self.path):
                if i >= index_from and i <= index_to:
                    self.Make_Folder(i)

            return True
        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")
            return False

    def Make_File(self, index:int=0, mode:str="w") -> bool:
        """This function will make a File on the specified index of the list. If no index is given it will use the first index of the list.

        Args:
            index (int, optional): The index of the path inside the list of paths where the File must be created. Defaults to 0.
            mode (str, optional): The mode in which the File shall be opened. Defaults to 'w'.

        Returns:
            bool: True if the operation was successful, False otherwise.
        """

        if not self.isFile:
            print("Not a File. Defined in [isFile]. [Large_File_Management_System]")
            return False

        try:
            with open(self.path[index], mode) as file:
                file.write(self.content[index])
            return True
        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")
            return False

    def Make_Empty_File(self, index:int=0, mode:str="w") -> bool:
        """This function will make a File with no content on the specified index of the list. If no index is given it will use the first index of the list.

        Args:
            index (int, optional): The index of the path inside the list of paths where the File must be created. Defaults to 0.
            mode (str, optional): The mode in which the File shall be opened. Defaults to 'w'.

        Returns:
            bool: True if the operation was successful, False otherwise.
        """

        if not self.isFile:
            print("Not a File. Defined in [isFile]. [Large_File_Management_System]")
            return False

        try:
            with open(self.path[index], mode) as file:
                file.write('')
            return True
        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")
            return False

    def Make_Files(self, indexes:tuple[int, Union[int, str]]=(0, "max"), modes:list=["w"]) -> bool:
        """This function will create Files in the provided paths inside the provided list.

        Args:
            indexes (tuple[int, Union[int, str]], optional): This defines the number of Files to create. The first value of the tuple must define from where the Files should be created and the second value must define till where the Files should be created (second value can be 'max' to define [till all]). (0, "max").

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        if not self.isFile:
            print("Not Files. Defined in [isFile]. [Large_File_Management_System]")
            return False

        try:
            index_from = indexes[0]
            index_to = str(indexes[1])

            if index_to.isalpha():
                if index_to.lower() == "max":
                    index_to = len(self.path)
                else:
                    print(f"\nWARNING: Invalid [indexes][{indexes[1]}]. Setting it to [{index_from}].[Large_File_Management_System]\n")
                    index_to = index_from

            index_to = int(index_to)

            for i, v in enumerate(self.path):
                if i >= index_from and i <= index_to:
                    self.Make_File(i, modes[i])

            return True
        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")
            return False

    def Make_Empty_Files(self, indexes:tuple[int, Union[int, str]]=(0, "max"), modes:list=["w"]) -> bool:
        """This function will create empty Files in the provided paths inside the provided list.

        Args:
            indexes (tuple[int, Union[int, str]], optional): This defines the number of Files to create. The first value of the tuple must define from where the Files should be created and the second value must define till where the Files should be created (second value can be 'max' to define [till all]). (0, "max").

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        if not self.isFile:
            print("Not Files. Defined in [isFile]. [Large_File_Management_System]")
            return False

        try:
            index_from = indexes[0]
            index_to = str(indexes[1])

            if index_to.isalpha():
                if index_to.lower() == "max":
                    index_to = len(self.path)
                else:
                    print(f"\nWARNING: Invalid [indexes][{indexes[1]}]. Setting it to [{index_from}].[Large_File_Management_System]\n")
                    index_to = index_from

            index_to = int(index_to)

            for i, v in enumerate(self.path):
                if i >= index_from and i <= index_to:
                    self.Make_Empty_File(i, modes[i])

            return True
        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")
            return False

    def Read_File(self, index:int=0, character_index:int=0) -> str:
        """This function will make a File on the specified index of the list. If no index is given it will use the first index of the list.

        Args:
            index (int, optional): The index of the path inside the list of paths where the File must be created. Defaults to 0.
            character_index (str, optional): The character number where the reading starts. Defaults to 0.

        Returns:
            str: The output.
        """

        if not self.isFile:
            print("Not a File. Defined in [isFile]. [Large_File_Management_System]")
            return False


        try:
            data = ""
            with open(self.path[index], "r") as file:
                file.seek(character_index)
                data = file.read()
            return data
        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")
            return ""

    def Read_Files(self, indexes:tuple=(0, Union[int, str]), character_indexes:list=[0]) -> list:
        """This function will read a number of Files on the specified index of the list. If no index is given it will use the first index of the list till the last.

        Args:
            indexes (tuple[int, Union[int, str]], optional): This defines the number of Files to read. The first value of the tuple must define from where the Files should be read and the second value must define till where the Files should be read (second value can be 'max' to define [till all]). (0, "max").
            character_index (list, optional): The character number where the reading starts. Defaults to [0].

        Returns:
            str: The output.
        """

        if not self.isFile:
            print("Not Files. Defined in [isFile]. [Large_File_Management_System]")
            return False

        try:
            data:list = []

            index_from = indexes[0]
            index_to = str(indexes[1])

            if index_to.isalpha():
                if index_to.lower() == "max":
                    index_to = len(self.path)
                else:
                    print(f"\nWARNING: Invalid [indexes][{indexes[1]}]. Setting it to [{index_from}].[Large_File_Management_System]\n")
                    index_to = index_from

            index_to = int(index_to)

            data = ""
            for i, v in enumerate(self.path):
                if i >= index_from and i <= index_to:
                    data.append(self.Read_File(i, character_indexes[i]))
            return data
        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")
            return ""

    def Make_Json_File(self, index:int=0, mode:str="w") -> bool:
        """This function will make a File with Json-like structure on the specified index of the list. If no index is given it will use the first index of the list.

        Args:
            index (int, optional): The index of the path inside the list of paths where the File must be created. Defaults to 0.
            mode (str, optional): The mode in which the File shall be opened. Defaults to 'w'.

        Returns:
            bool: True if the operation was successful, False otherwise.
        """

        if not self.isFile:
            print("Not a File. Defined in [isFile]. [Large_File_Management_System]")
            return False

        try:
            with open(self.path[index], mode) as file:
                json.dump(self.content[index], file)
            return True
        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")
            return False

    def Make_JSON_Files(self, indexes:tuple[int, Union[int, str]]=(0, "max"), modes:list=["w"]) -> bool:
        """This function will create Files with json-like structure in the provided paths inside the provided list.

        Args:
            indexes (tuple[int, Union[int, str]], optional): This defines the number of Files to create. The first value of the tuple must define from where the Files should be created and the second value must define till where the Files should be created (second value can be 'max' to define [till all]). (0, "max").

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        if not self.isFile:
            print("Not Files. Defined in [isFile]. [Large_File_Management_System]")
            return False

        try:
            index_from = indexes[0]
            index_to = str(indexes[1])

            if index_to.isalpha():
                if index_to.lower() == "max":
                    index_to = len(self.path)
                else:
                    print(f"\nWARNING: Invalid [indexes][{indexes[1]}]. Setting it to [{index_from}].[Large_File_Management_System]\n")
                    index_to = index_from

            index_to = int(index_to)

            for i, v in enumerate(self.path):
                if i >= index_from and i <= index_to:
                    self.Make_Json_File(i, modes[i])

            return True
        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")
            return False

    def Move_File(self, index:int=0) -> bool:
        """This function will move a File on the specified index of the list to the specifed index of [path2] list. If no index is given it will use the first index of the lists.

        Args:
            index (int, optional): The index of the path inside the lists of paths where the File must be moved. Defaults to 0.

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        if not self.isFile:
            print("Not a File. Defined in [isFile]. [Large_File_Management_System]")
            return False

        try:
            shutil.move(self.path[index], self.path2[index])
            return True
        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")
            return False

    def Move_Files(self, indexes:tuple=(0, "max")) -> bool:
        """This function will move Files in the provided paths inside the provided list [path] and list [path2].

        Args:
            indexes (tuple[int, Union[int, str]], optional): This defines the number of Files to move. The first value of the tuple must define from where the Files should be moved and the second value must define till where the Files should be moved (second value can be 'max' to define [till all]). (0, "max").

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        if not self.isFile:
            print("Not Files. Defined in [isFile]. [Large_File_Management_System]")
            return False

        try:
            index_from = indexes[0]
            index_to = str(indexes[1])

            if index_to.isalpha():
                if index_to.lower() == "max":
                    index_to = len(self.path)
                else:
                    print(f"\nWARNING: Invalid [indexes][{indexes[1]}]. Setting it to [{index_from}].[Large_File_Management_System]\n")
                    index_to = index_from

            index_to = int(index_to)

            for i, v in enumerate(self.path):
                if i >= index_from and i <= index_to:
                    self.Move_File(i)

            return True
        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")
            return False

    def Delete_File(self, index:int=0) -> bool:
        """This function will delete a File on the specified index of the list [path]. If no index is given it will use the first index of the list [path].

        Args:
            index (int, optional): The index of the path inside the list [path] defines which File must be deleted. Defaults to 0.

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        if not self.isFile:
            print("Not a File. Defined in [isFile]. [Large_File_Management_System]")
            return False

        try:
            os.remove(self.path[index])
            return True
        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")
            return False

    def Delete_Files(self, indexes:tuple=(0, "max")) -> bool:
        """This function will delete Files in the provided paths inside the provided list [path].

        Args:
            indexes (tuple[int, Union[int, str]], optional): This defines the number of Files to delete. The first value of the tuple must define from where the Files should be deleted and the second value must define till where the Files should be deleted (second value can be 'max' to define [till all]). (0, "max").

        Returns:
            bool: True if the operation was successful, False otherwise.
        """

        if not self.isFile:
            print("Not Files. Defined in [isFile]. [Large_File_Management_System]")
            return False

        try:
            index_from = indexes[0]
            index_to = str(indexes[1])

            if index_to.isalpha():
                if index_to.lower() == "max":
                    index_to = len(self.path)
                else:
                    print(f"\nWARNING: Invalid [indexes][{indexes[1]}]. Setting it to [{index_from}].[Large_File_Management_System]\n")
                    index_to = index_from

            index_to = int(index_to)

            return True
        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")
            return False

    def Delete_Folder(self, index:int=0) -> bool:
        """This function will delete a Folder on the specified index of the list [path]. If no index is given it will use the first index of the list [path].

        Args:
            index (int, optional): The index of the path inside the list [path] defines which Folder must be deleted. Defaults to 0.

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        try:
            os.rmdir(self.path[index])
            return True
        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")
            return False

    def Delete_Folders(self, indexes:tuple=(0, "max")) -> bool:
        """This function will delete Folders in the provided paths inside the provided list [path].

        Args:
            indexes (tuple[int, Union[int, str]], optional): This defines the number of Folders to delete. The first value of the tuple must define from where the Folders should be deleted and the second value must define till where the Folders should be deleted (second value can be 'max' to define [till all]). (0, "max").

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        try:
            index_from = indexes[0]
            index_to = str(indexes[1])

            if index_to.isalpha():
                if index_to.lower() == "max":
                    index_to = len(self.path)
                else:
                    print(f"\nWARNING: Invalid [indexes][{indexes[1]}]. Setting it to [{index_from}].[Large_File_Management_System]\n")
                    index_to = index_from

            index_to = int(index_to)

            for i, v in enumerate(self.path):
                if i >= index_from and i <= index_to:
                    self.Delete_Folder(i)

            return True
        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")
            return False

    def Remove_Tree(self, index:int=0) -> bool:
        """This function will delete a tree on the specified index of the list [path]. If no index is given it will use the first index of the list [path].

        Args:
            index (int, optional): The index of the path inside the list [path] defines which tree must be deleted. Defaults to 0.

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        try:
            shutil.rmtree(self.path[index])
            return True
        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")
            return False

    def Remove_Trees(self, indexes:tuple=(0, "max")) -> bool:
        """This function will delete trees in the provided paths inside the provided list [path].

        Args:
            indexes (tuple[int, Union[int, str]], optional): This defines the number of trees to delete. The first value of the tuple must define from where the trees should be deleted and the second value must define till where the trees should be deleted (second value can be 'max' to define [till all]). (0, "max").

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        try:
            index_from = indexes[0]
            index_to = str(indexes[1])

            if index_to.isalpha():
                if index_to.lower() == "max":
                    index_to = len(self.path)
                else:
                    print(f"\nWARNING: Invalid [indexes][{indexes[1]}]. Setting it to [{index_from}].[Large_File_Management_System]\n")
                    index_to = index_from

            index_to = int(index_to)

            for i, v in enumerate(self.path):
                if i >= index_from and i <= index_to:
                    self.Remove_Tree(i)

            return True
        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")
            return False

    def Rename_File(self, index:int=0) -> bool:
        """This function will rename a File on the specified index of the list [path]. If no index is given it will use the first index of the list [path].

        Args:
            index (int, optional): The index of the path inside the list [path] defines which File must be renamed. Defaults to 0.

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        if not self.isFile:
            print("Not a File. Defined in [isFile]. [Large_File_Management_System]")
            return False

        try:
            os.rename(self.path[index], self.path2[index])
            return True
        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")
            return False

    def Rename_Files(self, indexes:tuple=(0, "max")) -> bool:
        """This function will rename Files in the provided paths inside the provided list [path] and list [path2].

        Args:
            indexes (tuple[int, Union[int, str]], optional): This defines the number of Files to rename. The first value of the tuple must define from where the Files should be renamed and the second value must define till where the Files should be renamed (second value can be 'max' to define [till all]). (0, "max").

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        if not self.isFile:
            print("Not Files. Defined in [isFile]. [Large_File_Management_System]")
            return False

        try:
            index_from = indexes[0]
            index_to = str(indexes[1])

            if index_to.isalpha():
                if index_to.lower() == "max":
                    index_to = len(self.path)
                else:
                    print(f"\nWARNING: Invalid [indexes][{indexes[1]}]. Setting it to [{index_from}].[Large_File_Management_System]\n")
                    index_to = index_from

            index_to = int(index_to)

            for i, v in enumerate(self.path):
                if i >= index_from and i <= index_to:
                    self.Rename_File(i)

            return True
        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")
            return False

    def Rename_Folder(self, index:int=0) -> bool:
        """This function will rename a Folder on the specified index of the list [path] and list [path2]. If no index is given it will use the first index of the list [path] and list [path2].

        Args:
            index (int, optional): The index of the path inside the list [path] defines which Folder must be renamed. Defaults to 0.

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        try:
            os.rename(self.path[index], self.path2[index])
            return True
        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")
            return False

    def Rename_Folders(self, indexes:tuple=(0, "max")) -> bool:
        """This function will rename Folders in the provided paths inside the provided list [path] and list [path2].

        Args:
            indexes (tuple[int, Union[int, str]], optional): This defines the number of Folders to rename. The first value of the tuple must define from where the Folders should be renamed and the second value must define till where the Folders should be renamed (second value can be 'max' to define [till all]). (0, "max").

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        try:
            index_from = indexes[0]
            index_to = str(indexes[1])

            if index_to.isalpha():
                if index_to.lower() == "max":
                    index_to = len(self.path)
                else:
                    print(f"\nWARNING: Invalid [indexes][{indexes[1]}]. Setting it to [{index_from}].[Large_File_Management_System]\n")
                    index_to = index_from

            index_to = int(index_to)

            for i, v in enumerate(self.path):
                if i >= index_from and i <= index_to:
                    self.Rename_Folder(i)

            return True
        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")
            return False

    def Rename_File_Folder(self, index:int=0) -> bool:
        """This function will rename a File/Folder on the specified index of the list [path]. If no index is given it will use the first index of the list [path].

        Args:
            index (int, optional): The index of the path inside the list [path] defines which File/Folder must be renamed. Defaults to 0.

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        try:
            os.rename(self.path[index])
            return True
        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")
            return False

    def Rename_Files_Folders(self, indexes:tuple=(0, "max")) -> bool:
        """This function will rename Folders/Files in the provided paths inside the provided list [path] and list [path2].

        Args:
            indexes (tuple[int, Union[int, str]], optional): This defines the number of Files/Folders to rename. The first value of the tuple must define from where the Files/Folders should be renamed and the second value must define till where the Files/Folders should be renamed (second value can be 'max' to define [till all]). (0, "max").

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        try:
            index_from = indexes[0]
            index_to = str(indexes[1])

            if index_to.isalpha():
                if index_to.lower() == "max":
                    index_to = len(self.path)
                else:
                    print(f"\nWARNING: Invalid [indexes][{indexes[1]}]. Setting it to [{index_from}].[Large_File_Management_System]\n")
                    index_to = index_from

            index_to = int(index_to)

            for i, v in enumerate(self.path):
                if i >= index_from and i <= index_to:
                    self.Rename_File_Folder(i)

            return True
        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")
            return False

    def Link(self, index:int=0) -> bool:
        """This Function makes a hard-link.

        Args:
            index (int, optional): This defines which path should be used in list [path] and list [path2]. Defaults to 0.

        Returns:
            bool: True is the operation was successful or False otherwise.
        """

        if self.isFile:
            print("Not a File, defined in [isFile]. [Large_File_Management_System]")
            return False

        try:
            os.link(self.path[index], self.path2[index])

        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")

    def Links(self, indexes:tuple=(0, "max")) -> bool:
        """This function will make hard-links by provided list [path] and list [path2].

        Args:
            indexes (tuple[int, Union[int, str]], optional): This defines the number of Hard-Links to make. The first value of the tuple must define from where the Hard-Links should be renamed and the second value must define till where the Hard-Links should be made (second value can be 'max' to define [till all]). (0, "max").

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        try:
            index_from = indexes[0]
            index_to = str(indexes[1])

            if index_to.isalpha():
                if index_to.lower() == "max":
                    index_to = len(self.path)
                else:
                    print(f"\nWARNING: Invalid [indexes][{indexes[1]}]. Setting it to [{index_from}].[Large_File_Management_System]\n")
                    index_to = index_from

            index_to = int(index_to)

            for i, v in enumerate(self.path):
                if i >= index_from and i <= index_to:
                    self.Link(i)

            return True
        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")
            return False

    def Make_Encoded_File(self, index:int=0, mode:str="w") -> bool:
        """This function make a File which is encoding using PCEMU (Pheonix Compressed Encoding Method User) by the provided path in the list [path].

        Args:
            index (int, optional): This will define which path to use while making the File. Defaults to 0.
            mode (str, optional): This will define which mode to use while making the File. Defaults to 'w'.

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        if not self.isFile:
            print("Not a File. Defined in [isFile]. [Large_File_Management_System]")
            return False

        try:
            with open(self.path[index], mode) as file:
                content = BIN(use_pheonixApp_encoder=True, compressed=True, content=self.content[index]).PCEMU()
                file.write(content)
            return True
        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")
            return False

    def Make_Encoded_Files(self, indexes:tuple=(0, "max"), modes:list=["w"]) -> bool:
        """This function make a bunch of Files which are encoding using PEMU (Pheonix Encoding Method User) by the provided path in the list [path].

        Args:
            indexes (tuple, optional): This will define which paths to use while making the Files. The first number defines from which index should the encoded Files will be made and second one defines 'till where'. Set second to 'max' to define the full length of the list [path]. Defaults to (0, 'max').
            modes (list, optional): This will define which modes to use while making the Files. Defaults to ['w'].

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        if not self.isFile:
            print("Not a File. Defined in [isFile]. [Large_File_Management_System]")
            return False

        try:
            index_from = indexes[0]
            index_to = str(indexes[1])

            if index_to.isalpha():
                if index_to.lower() == "max":
                    index_to = len(self.path)
                else:
                    print(f"\nWARNING: Invalid [indexes][{indexes[1]}]. Setting it to [{index_from}].[Large_File_Management_System]\n")
                    index_to = index_from

            index_to = int(index_to)

            for i, v in enumerate(self.path):
                if i >= index_from and i <= index_to:
                    self.Make_Encoded_File(i, modes[i])

            return True
        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")
            return False

    def Make_Bin_Encoded_File(self, index:int=0, mode:str="wb") -> bool:
        """The Files will be in binary format.
        This function make a File which is encoding using PCEMU (Pheonix Compressed Encoding Method User) by the provided path in the list [path].

        Args:
            index (int, optional): This will define which path to use while making the File. Defaults to 0.
            mode (str, optional): This will define which mode to use while making the File. Defaults to 'w'.

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        if not self.isFile:
            print("Not a File. Defined in [isFile]. [Large_File_Management_System]")
            return False

        try:
            with open(self.path[index], mode) as file:
                content = BIN(use_pheonixApp_encoder=True, compressed=True).str_to_bytes(BIN(use_pheonixApp_encoder=True, compressed=True, content=self.content[index]).PCEMU(), "utf-16")
                file.write(content)
            return True
        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")
            return False

    def Make_BIN_Encoded_Files(self, indexes:tuple=(0, "max"), modes:list=["wb"]) -> bool:
        """The Files are in binary format.
        This function make a bunch of Files which are encoding using PEMU (Pheonix Encoding Method User) by the provided path in the list [path].

        Args:
            indexes (tuple, optional): This will define which paths to use while making the Files. The first number defines from which index should the encoded Files will be made and second one defines 'till where'. Set second to 'max' to define the full length of the list [path]. Defaults to (0, 'max').
            modes (list, optional): This will define which modes to use while making the Files. Defaults to ['w'].

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        if not self.isFile:
            print("Not a File. Defined in [isFile]. [Large_File_Management_System]")
            return False

        try:
            index_from = indexes[0]
            index_to = str(indexes[1])

            if index_to.isalpha():
                if index_to.lower() == "max":
                    index_to = len(self.path)
                else:
                    print(f"\nWARNING: Invalid [indexes][{indexes[1]}]. Setting it to [{index_from}].[Large_File_Management_System]\n")
                    index_to = index_from

            index_to = int(index_to)

            for i, v in enumerate(self.path):
                if i >= index_from and i <= index_to:
                    self.Make_Bin_Encoded_File(i, modes[i])

            return True
        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")
            return False

    def Read_Encoded_File(self, index:int=0, character_index:int=0) -> str:
        """This function read a File which is encoding using PEMU (Pheonix Encoding Method User) by the provided path in the list [path].

        Args:
            index (int, optional): This will define which paths to use while reading the File. Defaults to 0.
            character_index (str, optional): The character number where the reading starts. Defaults to 0.

        Returns:
            bool: True if the operation was successful, False otherwise.
        """

        if not self.isFile:
            print("Not a File. Defined in [isFile]. [Large_File_Management_System]")
            return False

        try:
            data = ""
            with open(self.path[index], "r") as file:
                file.seek(character_index)
                data = BIN(content=file.read()).PCDMU()
            return data
        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")
            return ""

    def Read_Encoded_Files(self, indexes:tuple=(0, 'max'), character_indexes:list=[0]) -> list:
        """This function read a bunch of Files which are encoding using PEMU (Pheonix Encoding Method User) by the provided path in the list [path].

        Args:
            indexes (tuple, optional): This will define which paths to use while reading the Files. The first number defines from which index should the encoded Files will be read and second one defines 'till where'. Set second to 'max' to define the full length of the list [path]. Defaults to (0, 'max').
            character_indexes (str, optional): The character number where the reading starts. Defaults to 0.

        Returns:
            bool: True if the operation was successful, False otherwise.
        """

        if not self.isFile:
            print("Not Files. Defined in [isFile]. [Large_File_Management_System]")
            return False

        try:
            data:list = []

            index_from = indexes[0]
            index_to = str(indexes[1])

            if index_to.isalpha():
                if index_to.lower() == "max":
                    index_to = len(self.path)
                else:
                    print(f"\nWARNING: Invalid [indexes][{indexes[1]}]. Setting it to [{index_from}].[Large_File_Management_System]\n")
                    index_to = index_from

            index_to = int(index_to)

            data = ""
            for i, v in enumerate(self.path):
                if i >= index_from and i <= index_to:
                    data.append(self.Read_Encoded_File(i, character_indexes[i]))
            return data
        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")
            return ""

    def Read_Bin_Encoded_File(self, index:int=0, character_index:int=0) -> str:
        """The File should be in binary format.
        This function read a File which is encoding using PEMU (Pheonix Encoding Method User) by the provided path in the list [path].

        Args:
            index (int, optional): This will define which paths to use while reading the File. Defaults to 0.
            character_index (str, optional): The character number where the reading starts. Defaults to 0.

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        if not self.isFile:
            print("Not a File. Defined in [isFile]. [Large_File_Management_System]")
            return False

        try:
            data = ""
            with open(self.path[index], "rb") as file:
                file.seek(character_index)
                data_ = file.read()
                data = BIN(content=data_).bytes_to_str(data_)
                data = BIN(content=data).PCDMU()
            return data
        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")
            return ""

    def Read_Bin_Encoded_Files(self, indexes:tuple=(0, 'max'), character_indexes:list=[0]) -> list:
        """The Files should be in binary format.
        This function read a bunch of Files which are encoding using PEMU (Pheonix Encoding Method User) by the provided path in the list [path].

        Args:
            indexes (tuple, optional): This will define which paths to use while reading the Files. The first number defines from which index should the encoded Files will be read and second one defines 'till where'. Set second to 'max' to define the full length of the list [path]. Defaults to (0, 'max').
            character_indexes (str, optional): The character number where the reading starts. Defaults to 0.

        Returns:
            bool: True if the operation was successful, False otherwise.
        """

        if not self.isFile:
            print("Not Files. Defined in [isFile]. [Large_File_Management_System]")
            return False

        try:
            data:list = []

            index_from = indexes[0]
            index_to = str(indexes[1])

            if index_to.isalpha():
                if index_to.lower() == "max":
                    index_to = len(self.path)
                else:
                    print(f"\nWARNING: Invalid [indexes][{indexes[1]}]. Setting it to [{index_from}].[Large_File_Management_System]\n")
                    index_to = index_from

            index_to = int(index_to)

            data = ""
            for i, v in enumerate(self.path):
                if i >= index_from and i <= index_to:
                    data.append(self.Read_Bin_Encoded_File(i, character_indexes[i]))
            return data
        except Exception as e:
            print(f"\nLarge_File_Management_System:\n{e}\n")
            return ""