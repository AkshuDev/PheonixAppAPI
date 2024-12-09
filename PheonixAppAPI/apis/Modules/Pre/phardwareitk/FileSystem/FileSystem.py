import os
import sys
import binascii
import json

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

from . import *

if not sys.path[PHardwareITK] == PHardwareITK_P:
    sys.path.append(PHardwareITK_P)

from phardwareitk import LIB

import phardwareitk.ErrorSystem.ErrorSystem as ES

from typing import *

class BasicFileSystem:
    @staticmethod
    def CreateFile(filePath:str, data:Union[str, dict, int]) -> tuple[bool, str]:
        """Creates a new file with the provided data.
        
        Args:
            filePath (str): The path to the file to be created.
            date (Union[str, dict, int]) : The data to be inserted into the file.
            
        Returns:
            tuple[bool, str] ->
                bool: True if successful, False otherwise.
                str: The Error if success was False.
            
        Calls (Without raising):
            PheonixException: If an Unknown Error occurs during creation.
            PheonixIOError: If an Input/Output Error occurs during creation."""
        success:bool = False
        error:str = ""
        
        try:
            with open(filePath, 'w') as f:
                f.write(str(data))
                f.close()

            error = ""
            success = True
        except IOError as e:
            error = ES.PheonixIOError(str(e))
            success = False
            return success, error
        except Exception as e:
            error = ES.PheonixException(str(e))
            success = False
            return success, error

        return success, error

    @staticmethod
    def AppendFile(filePath:str, data:Union[str, int, dict], seek:Union[None, int]=None) -> tuple[bool, str]:
        """Appends the data to the given filePath

        Args:
            filePath (str): The path to the file to append.
            data (Union[str, int, dict]): The data to append in the file.
            seek (Optional) (Union[None, int]): The seek position. 'None' means to append at the end of the file. Defaults to None.

        Returns:
            tuple[bool, str] ->
                bool: True if successful, False otherwise.
                str: The Error if success was False

        Calls (Without raising):
            PheonixException: If an Unknown Error occurs during creation.
            PheonixIOError: If an Input/Output Error occurs during creation.
            PheonixFileNotFoundError: If file was not found."""
        success:bool = False
        error:str = ""

        if not os.path.exists(filePath):
            error = ES.PheonixFileNotFoundError(f"File doesn't exist [{filePath}]")
            success = False
            return success, error
        
        else:
            try:
                if seek != None:
                    with open(filePath, "a") as f:
                        f.seek(seek)
                        f.write(str(data))
                        f.close()
                else:
                    with open(filePath, "a") as f:
                        f.write(str(data))
                        f.close()

                error = ""
                success = True
            except IOError as e:
                error = ES.PheonixIOError(str(e))
                success = False
                return success, error
            except Exception as e:
                error = ES.PheonixException(str(e))
                success = False
                return success, error
            
            return success, error
        
    @staticmethod
    def ReadFile(filePath: str) -> tuple[bool, Union[str, None]]:
        """Reads the content of the file.

        Args:
            filePath (str): The path to the file to read.

        Returns:
            tuple[bool, Union[str, None]] -> 
                bool: True if successful, False otherwise.
                str: The content of the file if successful, or error message if not.

        Calls (Without raising):
            PheonixException: If an Unknown Error occurs during reading.
            PheonixFileNotFoundError: If file was not found."""
        success: bool = False
        content: Union[str, None] = None
        error: str = ""

        if not os.path.exists(filePath):
            error = ES.PheonixFileNotFoundError(f"File doesn't exist [{filePath}]")
            success = False
            return success, error
        
        try:
            with open(filePath, 'r') as f:
                content = f.read()
            error = content
            success = True
        except IOError as e:
            error = ES.PheonixIOError(str(e))
            success = False
        except Exception as e:
            error = ES.PheonixException(str(e))
            success = False

        return success, error

    @staticmethod
    def DeleteFile(filePath: str) -> tuple[bool, str]:
        """Deletes the specified file.

        Args:
            filePath (str): The path to the file to delete.

        Returns:
            tuple[bool, str] ->
                bool: True if successful, False otherwise.
                str: The error message if unsuccessful.

        Calls (Without raising):
            PheonixFileNotFoundError: If file was not found."""
        success: bool = False
        error: str = ""

        if not os.path.exists(filePath):
            error = ES.PheonixFileNotFoundError(f"File doesn't exist [{filePath}]")
            success = False
            return success, error

        try:
            os.remove(filePath)
            success = True
            error = ""
        except IOError as e:
            error = ES.PheonixIOError(str(e))
            success = False
        except Exception as e:
            error = ES.PheonixException(str(e))
            success = False

        return success, error

    @staticmethod
    def RenameFile(oldPath: str, newPath: str) -> tuple[bool, str]:
        """Renames a file from `oldPath` to `newPath`.

        Args:
            oldPath (str): The current path of the file to rename.
            newPath (str): The new name/path of the file.

        Returns:
            tuple[bool, str] ->
                bool: True if successful, False otherwise.
                str: The error message if unsuccessful.

        Calls (Without raising):
            PheonixFileNotFoundError: If file was not found."""
        success: bool = False
        error: str = ""

        if not os.path.exists(oldPath):
            error = ES.PheonixFileNotFoundError(f"File doesn't exist [{oldPath}]")
            success = False
            return success, error

        try:
            os.rename(oldPath, newPath)
            success = True
            error = ""
        except IOError as e:
            error = ES.PheonixIOError(str(e))
            success = False
        except Exception as e:
            error = ES.PheonixException(str(e))
            success = False

        return success, error

    @staticmethod
    def FileExists(filePath: str) -> tuple[bool, str]:
        """Checks if the file exists at the specified path.

        Args:
            filePath (str): The path to check.

        Returns:
            tuple[bool, str] ->
                bool: True if the file exists, False otherwise.
                str: An appropriate message."""
        exists: bool = False
        error: str = ""

        if os.path.exists(filePath):
            exists = True
            error = "File exists."
        else:
            exists = False
            error = ES.PheonixFileNotFoundError(f"File not found at [{filePath}]")

        return exists, error

    @staticmethod
    def GetFileSize(filePath: str) -> tuple[bool, Union[int, str]]:
        """Returns the size of the specified file.

        Args:
            filePath (str): The path to the file.

        Returns:
            tuple[bool, Union[int, str]] ->
                bool: True if successful, False otherwise.
                int: The size of the file in bytes if successful.
                str: Error message if unsuccessful.

        Calls (Without raising):
            PheonixFileNotFoundError: If file was not found."""
        success: bool = False
        error: Union[int, str] = 0

        if not os.path.exists(filePath):
            error = ES.PheonixFileNotFoundError(f"File doesn't exist [{filePath}]")
            success = False
            return success, error

        try:
            size = os.path.getsize(filePath)
            error = size
            success = True
        except IOError as e:
            error = ES.PheonixIOError(str(e))
            success = False
        except Exception as e:
            error = ES.PheonixException(str(e))
            success = False

        return success, error

    @staticmethod
    def CopyFile(srcPath: str, destPath: str) -> tuple[bool, str]:
        """Copies a file from the source path to the destination path.

        Args:
            srcPath (str): The source file path.
            destPath (str): The destination file path.

        Returns:
            tuple[bool, str] ->
                bool: True if successful, False otherwise.
                str: Error message if unsuccessful.

        Calls (Without raising):
            PheonixFileNotFoundError: If the source file does not exist."""
        success: bool = False
        error: str = ""

        if not os.path.exists(srcPath):
            error = ES.PheonixFileNotFoundError(f"Source file doesn't exist [{srcPath}]")
            success = False
            return success, error

        try:
            import shutil
            shutil.copy(srcPath, destPath)
            success = True
            error = ""
        except IOError as e:
            error = ES.PheonixIOError(str(e))
            success = False
        except Exception as e:
            error = ES.PheonixException(str(e))
            success = False

        return success, error

    @staticmethod
    def MoveFile(srcPath: str, destPath: str) -> tuple[bool, str]:
        """Moves a file from the source path to the destination path.

        Args:
            srcPath (str): The source file path.
            destPath (str): The destination file path.

        Returns:
            tuple[bool, str] ->
                bool: True if successful, False otherwise.
                str: Error message if unsuccessful.

        Calls (Without raising):
            PheonixFileNotFoundError: If the source file does not exist."""
        success: bool = False
        error: str = ""

        if not os.path.exists(srcPath):
            error = ES.PheonixFileNotFoundError(f"Source file doesn't exist [{srcPath}]")
            success = False
            return success, error

        try:
            os.rename(srcPath, destPath)
            success = True
            error = ""
        except IOError as e:
            error = ES.PheonixIOError(str(e))
            success = False
        except Exception as e:
            error = ES.PheonixException(str(e))
            success = False

        return success, error

    @staticmethod
    def CreateDirectory(dirPath: str) -> tuple[bool, str]:
        """Creates a directory at the specified path.

        Args:
            dirPath (str): The path where the directory will be created.

        Returns:
            tuple[bool, str] ->
                bool: True if successful, False otherwise.
                str: Error message if unsuccessful.
        """
        success: bool = False
        error: str = ""

        try:
            os.makedirs(dirPath, exist_ok=True)
            success = True
            error = ""
        except IOError as e:
            error = ES.PheonixIOError(str(e))
            success = False
        except Exception as e:
            error = ES.PheonixException(str(e))
            success = False

        return success, error

class JsonFileSystem:
    @staticmethod
    def CreateJsonFile(filePath: str, data: Union[dict, list]) -> tuple[bool, str]:
        """Creates a new JSON file with the provided data.
        
        Args:
            filePath (str): The path to the JSON file to be created.
            data (Union[dict, list]): The data to be inserted into the JSON file.

        Returns:
            tuple[bool, str] -> 
                bool: True if successful, False otherwise.
                str: The error message if unsuccessful.
            
        Calls (Without raising):
            PheonixException: If an unknown error occurs during file creation.
            PheonixIOError: If there is an input/output error during file creation."""
        
        import json
        success: bool = False
        error: str = ""

        try:
            with open(filePath, 'w') as f:
                json.dump(data, f, indent=4)
            success = True
        except IOError as e:
            error = ES.PheonixIOError(str(e))
        except Exception as e:
            error = ES.PheonixException(str(e))
        
        return success, error

    @staticmethod
    def AppendJsonData(filePath: str, data: Union[dict, list]) -> tuple[bool, str]:
        """Appends data to an existing JSON file.

        Args:
            filePath (str): The path to the JSON file to append data.
            data (Union[dict, list]): The data to be appended.

        Returns:
            tuple[bool, str] -> 
                bool: True if successful, False otherwise.
                str: Error message if unsuccessful.

        Calls (Without raising):
            PheonixFileNotFoundError: If the file is not found.
            PheonixIOError: If an input/output error occurs."""
        success: bool = False
        error: str = ""

        if not os.path.exists(filePath):
            error = ES.PheonixFileNotFoundError(f"File not found: {filePath}")
        else:
            try:
                with open(filePath, 'r+') as f:
                    current_data = json.load(f)
                    if isinstance(current_data, list):
                        current_data.append(data)
                    elif isinstance(current_data, dict):
                        current_data.update(data)
                    else:
                        error = ES.PheonixException("Unsupported data format in file.")
                        return success, error
                    f.seek(0)
                    json.dump(current_data, f, indent=4)
                success = True
            except IOError as e:
                error = ES.PheonixIOError(str(e))
            except Exception as e:
                error = ES.PheonixException(str(e))

        return success, error

    @staticmethod
    def ReadJsonFile(filePath: str) -> tuple[bool, Union[dict, list, str]]:
        """Reads data from a JSON file.

        Args:
            filePath (str): The path to the JSON file.

        Returns:
            tuple[bool, Union[dict, list, str]] -> 
                bool: True if successful, False otherwise.
                dict/list: The contents of the file if successful, error message if not.

        Calls (Without raising):
            PheonixFileNotFoundError: If file not found.
            PheonixIOError: If an input/output error occurs."""
        success: bool = False
        error: str = ""

        if not os.path.exists(filePath):
            error = ES.PheonixFileNotFoundError(f"File not found: {filePath}")
        else:
            try:
                with open(filePath, 'r') as f:
                    data = json.load(f)
                    success = True
                    error = data
            except IOError as e:
                error = ES.PheonixIOError(str(e))
            except json.JSONDecodeError as e:
                error = ES.PheonixException(f"JSON decoding error: {str(e)}")
            except Exception as e:
                error = ES.PheonixException(str(e))

        return success, error

    @staticmethod
    def DeleteJsonFile(filePath: str) -> tuple[bool, str]:
        """Deletes a JSON file.

        Args:
            filePath (str): The path to the JSON file to be deleted.

        Returns:
            tuple[bool, str] -> 
                bool: True if successful, False otherwise.
                str: The error message if unsuccessful.

        Calls (Without raising):
            PheonixFileNotFoundError: If file does not exist."""
        success: bool = False
        error: str = ""

        if not os.path.exists(filePath):
            error = ES.PheonixFileNotFoundError(f"File not found: {filePath}")
        else:
            try:
                os.remove(filePath)
                success = True
            except IOError as e:
                error = ES.PheonixIOError(str(e))
            except Exception as e:
                error = ES.PheonixException(str(e))

        return success, error

    @staticmethod
    def FileExists(filePath: str) -> bool:
        """Checks if the JSON file exists.

        Args:
            filePath (str): The path to the JSON file.

        Returns:
            bool: True if the file exists, False otherwise."""
        return os.path.exists(filePath)

    @staticmethod
    def GetJsonKeys(filePath: str) -> tuple[bool, Union[list, str]]:
        """Returns all keys in a JSON file (if it is a JSON object).

        Args:
            filePath (str): The path to the JSON file.

        Returns:
            tuple[bool, Union[list, str]] -> 
                bool: True if successful, False otherwise.
                list: List of keys if file is a dictionary, error message if not.

        Calls (Without raising):
            PheonixFileNotFoundError: If file does not exist."""
        success: bool = False
        error: str = []

        if not os.path.exists(filePath):
            error = ES.PheonixFileNotFoundError(f"File not found: {filePath}")
        else:
            try:
                with open(filePath, 'r') as f:
                    data = json.load(f)
                    if isinstance(data, dict):
                        success = True
                        error = list(data.keys())
                    else:
                        error = ES.PheonixException("File does not contain a JSON object.")
            except IOError as e:
                error = ES.PheonixIOError(str(e))
            except json.JSONDecodeError as e:
                error = ES.PheonixException(f"JSON decoding error: {str(e)}")
            except Exception as e:
                error = ES.PheonixException(str(e))

        return success, error

    @staticmethod
    def GetJsonFileSize(filePath: str) -> tuple[bool, Union[int, str]]:
        """Returns the size of the JSON file.

        Args:
            filePath (str): The path to the JSON file.

        Returns:
            tuple[bool, Union[int, str]] -> 
                bool: True if successful, False otherwise.
                int: File size in bytes if successful, error message if not.

        Calls (Without raising):
            PheonixFileNotFoundError: If file does not exist."""
        success: bool = False
        error: str = ""

        if not os.path.exists(filePath):
            error = ES.PheonixFileNotFoundError(f"File not found: {filePath}")
        else:
            try:
                success = True
                error = os.path.getsize(filePath)
            except Exception as e:
                error = ES.PheonixException(str(e))

        return success, error

    @staticmethod
    def UpdateJsonKey(filePath: str, key: str, new_value: Union[str, int, dict, list]) -> tuple[bool, str]:
        """Updates the value of a specific key in a JSON file.

        Args:
            filePath (str): The path to the JSON file.
            key (str): The key whose value needs to be updated.
            new_value (Union[str, int, dict, list]): The new value to update.

        Returns:
            tuple[bool, str] -> 
                bool: True if successful, False otherwise.
                str: The error message if unsuccessful.

        Calls (Without raising):
            PheonixFileNotFoundError: If file does not exist."""
        success: bool = False
        error: str = ""

        if not os.path.exists(filePath):
            error = ES.PheonixFileNotFoundError(f"File not found: {filePath}")
        else:
            try:
                with open(filePath, 'r+') as f:
                    data = json.load(f)
                    if isinstance(data, dict) and key in data:
                        data[key] = new_value
                        f.seek(0)
                        json.dump(data, f, indent=4)
                        success = True
                    else:
                        error = ES.PheonixException(f"Key '{key}' not found in JSON.")
            except IOError as e:
                error = ES.PheonixIOError(str(e))
            except json.JSONDecodeError as e:
                error = ES.PheonixException(f"JSON decoding error: {str(e)}")
            except Exception as e:
                error = ES.PheonixException(str(e))

        return success, error

    @staticmethod
    def ValidateJson(filePath: str) -> tuple[bool, str]:
        """Validates if a file is a valid JSON.

        Args:
            filePath (str): The path to the JSON file.

        Returns:
            tuple[bool, str] -> 
                bool: True if valid, False otherwise.
                str: The error message if invalid.

        Calls (Without raising):
            PheonixFileNotFoundError: If file not found."""
        success: bool = False
        error: str = ""

        if not os.path.exists(filePath):
            error = ES.PheonixFileNotFoundError(f"File not found: {filePath}")
        else:
            try:
                with open(filePath, 'r') as f:
                    json.load(f)
                success = True
            except json.JSONDecodeError as e:
                error = ES.PheonixException(f"Invalid JSON: {str(e)}")
            except Exception as e:
                error = ES.PheonixException(str(e))

        return success, error

    @staticmethod
    def GetJsonFileExtension(filePath: str) -> tuple[bool, str]:
        """Gets the file extension of a JSON file.

        Args:
            filePath (str): The path to the JSON file.

        Returns:
            tuple[bool, str] -> 
                bool: True if successful, False otherwise.
                str: The file extension ('.json') if successful, error message if not."""
        success: bool = False
        error: str = ""

        if not os.path.exists(filePath):
            error = ES.PheonixFileNotFoundError(f"File not found: {filePath}")
        else:
            _, ext = os.path.splitext(filePath)
            if ext == ".json":
                success = True
                error = ext
            else:
                error = ES.PheonixException(f"File is not a JSON file: {filePath}")

        return success, error

    @staticmethod
    def MergeJsonFiles(srcPath: str, destPath: str) -> tuple[bool, str]:
        """Merges two JSON files.

        Args:
            srcPath (str): The source JSON file path.
            destPath (str): The destination JSON file path.

        Returns:
            tuple[bool, str] -> 
                bool: True if successful, False otherwise.
                str: The error message if unsuccessful.

        Calls (Without raising):
            PheonixFileNotFoundError: If any file is not found."""
        success: bool = False
        error: str = ""

        if not os.path.exists(srcPath):
            error = ES.PheonixFileNotFoundError(f"Source file not found: {srcPath}")
        elif not os.path.exists(destPath):
            error = ES.PheonixFileNotFoundError(f"Destination file not found: {destPath}")
        else:
            try:
                with open(srcPath, 'r') as f_src, open(destPath, 'r+') as f_dest:
                    src_data = json.load(f_src)
                    dest_data = json.load(f_dest)

                    if isinstance(src_data, dict) and isinstance(dest_data, dict):
                        dest_data.update(src_data)
                    else:
                        error = ES.PheonixException("Both files should contain JSON objects.")
                        return success, error

                    f_dest.seek(0)
                    json.dump(dest_data, f_dest, indent=4)
                    success = True
            except Exception as e:
                error = ES.PheonixException(str(e))

        return success, error

    @staticmethod
    def CreateJsonBackup(filePath: str) -> tuple[bool, str]:
        """Creates a backup of a JSON file.

        Args:
            filePath (str): The path to the JSON file to be backed up.

        Returns:
            tuple[bool, str] -> 
                bool: True if successful, False otherwise.
                str: The error message if unsuccessful."""
        success: bool = False
        error: str = ""

        if not os.path.exists(filePath):
            error = ES.PheonixFileNotFoundError(f"File not found: {filePath}")
        else:
            try:
                backup_path = filePath + ".bak"
                with open(filePath, 'r') as f_src, open(backup_path, 'w') as f_bak:
                    json.dump(json.load(f_src), f_bak, indent=4)
                success = True
            except Exception as e:
                error = ES.PheonixException(str(e))

        return success, error

class LowFileSystem:
    """NOTE: For using majority of the functions in this class, please install GCC, LD, and NASM (Mingw64 or Msys2 UCRT64).
    If you cannot install it. Please use PLTEC via Command Line Interface to convert any language syntax defined in a json file to Assembly or even Object (Undergoing development). But before making such a file please understand the file's syntax ->
        1. Include the convertion Os (ALL CAPS) and mode at the start of the json. Like -> 'ELF': '', 'x86': ''
        2. define a json inside the file with the key as 'SET'. Like -> '{'ELF': '', 'x86': '', 'SET': {}}'. The set is the point where all the syntax will go.
        3. NOTE: The syntax will work with the pre-made funcs in the DEF_LanguageSET.json. The syntax will have to be understood by the you if you want to add more funcs in it.
        4. Each Key in the 'SET' will have to have these required notes ->
            i. No spaces are allowed in the key
            ii. Include /S at the end of the key. And after the /S please include a sperator that will be used to seperate the key. Commomly used -> ' '.
            iii. Here are some important definitions ->
                a. /*DNAME: Specifies that at the specific location the user must type in the name of [something].
                b. /*DVALUE: Specifies that at the specific location the user must type in the value of [something].
                c. /*DSIZE: Specifies that at the specific location the user must type in the size of [something]. NOTE: DSIZE is a must in input function
        5. Inside the 'SET' please include a key:value pair with the value as 'includeFuncs'. This ensures all the neccarry functions will be imported if the user wrote the specific key.
        6. After that include whatever key you want as to be working with the syntax but please remember the 4.iii section. The definitions act as a parameter to the funcs and please openUP DEF_LanguageSET to see the parameters and funcs
        7. In the Value input the func you want to call if the specified key is displayed.

        EXAMPLE Lang.json -> '
        {
            "ELF": "",
            "x86": "",
            "SET": {
                "#include:/*DVALUE/INCLUDEINS/S ": "includeFuncs",
                "BasicIO/INCLUDE": {
                    "print:/*DVALUE/*DNAME/S ": "printINS",
                    "input:/*DNAME/*DSIZE/S ": "inputINS",
                    "clean:/S": "cleanupINS",
                    "return:/*DVALUE/S ": "returnINS"
                }
            }
        }'

        Example Test.txt -> '
        #include: BasicIO
        
        print: helloWorld HelloVariable
        clean:
        return: 0'

        Converted Assembly -> '
        section .data
        HelloVariable_pri db \"helloWorld\"
        HelloVariable_pri_LEN equ $ - HelloVariable_pri

        section .text
        global _start

        _start:
        mov ecx, HelloVariable_pri
        mov edx, HelloVariable_pri_LEN
        call print
        call cleanup32
        mov ebx, 0
        call return

        print:
        mov eax, 4
        mov ebx, 1
        int 80h

        input:
        mov eax, 3
        mov ebx, 1
        int 80h

        return:
        mov eax, 1
        int 80h

        cleanup32:
        xor eax, eax
        xor ebx, ebx
        xor ecx, ecx
        xor edx, edx
        xor esi, esi
        xor ebp, ebp
        ret
        '

        PLTEC has been updated and some changes in the DEF_lang.json might not bee understood. so please try using a AI to understand via the example provided.
    """
    # 1. ASM File Handling
    @staticmethod
    def CreateAsmFile(filePath: str, asmContent: str) -> tuple[bool, str]:
        """Creates a new ASM file with the provided ASM content."""
        try:
            with open(filePath, 'w') as f:
                f.write(asmContent)
            return True, ""
        except Exception as e:
            return False, str(e)

    @staticmethod
    def ReadAsmFile(filePath: str) -> tuple[bool, str]:
        """Reads content from an ASM file."""
        try:
            with open(filePath, 'r') as f:
                content = f.read()
            return True, content
        except Exception as e:
            return False, str(e)

    @staticmethod
    def CompileAsmToObject(filePath: str) -> tuple[bool, str]:
        """Compiles an ASM file to an object (.o) file."""
        try:
            os.system(f"nasm -f elf64 -o {filePath.replace('.asm', '.o')} {filePath}")
            return True, ""
        except Exception as e:
            return False, str(e)

    @staticmethod
    def DisassembleAsmFile(filePath: str) -> tuple[bool, str]:
        """Disassembles an ASM file to inspect the assembly instructions."""
        try:
            disasm = os.popen(f"objdump -d {filePath}").read()
            return True, disasm
        except Exception as e:
            return False, str(e)

    @staticmethod
    def CreateAsmFromString(asmCode: str, outputFile: str) -> tuple[bool, str]:
        """Creates an ASM file from a string of ASM code."""
        try:
            with open(outputFile, 'w') as f:
                f.write(asmCode)
            return True, ""
        except Exception as e:
            return False, str(e)

    # 2. Object File (.O) Handling
    @staticmethod
    def CreateObjectFile(filePath: str) -> tuple[bool, str]:
        """Creates an object (.o) file from a C/C++ file."""
        try:
            os.system(f"gcc -c {filePath} -o {filePath.replace('.c', '.o')}")
            return True, ""
        except Exception as e:
            return False, str(e)

    @staticmethod
    def LinkObjectFiles(objFiles: list[str], outputFile: str) -> tuple[bool, str]:
        """Links multiple object (.o) files into an executable."""
        try:
            os.system(f"ld -o {outputFile} {' '.join(objFiles)}")
            return True, ""
        except Exception as e:
            return False, str(e)

    @staticmethod
    def DisassembleObjectFile(objFilePath: str) -> tuple[bool, str]:
        """Disassembles an object file to inspect the assembly instructions."""
        try:
            disasm = os.popen(f"objdump -d {objFilePath}").read()
            return True, disasm
        except Exception as e:
            return False, str(e)

    # 3. C and C++ File Handling
    @staticmethod
    def CreateCFile(filePath: str, cContent: str) -> tuple[bool, str]:
        """Creates a new C file with the provided C code."""
        try:
            with open(filePath, 'w') as f:
                f.write(cContent)
            return True, ""
        except Exception as e:
            return False, str(e)

    @staticmethod
    def CompileCToObject(filePath: str) -> tuple[bool, str]:
        """Compiles a C file to an object (.o) file."""
        try:
            os.system(f"gcc -c {filePath} -o {filePath.replace('.c', '.o')}")
            return True, ""
        except Exception as e:
            return False, str(e)

    @staticmethod
    def CreateCppFile(filePath: str, cppContent: str) -> tuple[bool, str]:
        """Creates a new C++ file with the provided C++ code."""
        try:
            with open(filePath, 'w') as f:
                f.write(cppContent)
            return True, ""
        except Exception as e:
            return False, str(e)

    @staticmethod
    def CompileCppToObject(filePath: str) -> tuple[bool, str]:
        """Compiles a C++ file to an object (.o) file."""
        try:
            os.system(f"g++ -c {filePath} -o {filePath.replace('.cpp', '.o')}")
            return True, ""
        except Exception as e:
            return False, str(e)

    @staticmethod
    def CompileCPlusPlusFile(filePath: str) -> tuple[bool, str]:
        """Compiles a C++ file into an executable."""
        try:
            os.system(f"g++ {filePath} -o {filePath.replace('.cpp', '')}")
            return True, ""
        except Exception as e:
            return False, str(e)

    # 4. Binary File Handling
    @staticmethod
    def ReadBinaryFile(filePath: str) -> tuple[bool, bytes]:
        """Reads data from a binary file."""
        try:
            with open(filePath, 'rb') as f:
                data = f.read()
            return True, data
        except Exception as e:
            return False, str(e)

    @staticmethod
    def WriteBinaryFile(filePath: str, data: bytes) -> tuple[bool, str]:
        """Writes data to a binary file."""
        try:
            with open(filePath, 'wb') as f:
                f.write(data)
            return True, ""
        except Exception as e:
            return False, str(e)

    @staticmethod
    def AppendBinaryFile(filePath: str, data: bytes) -> tuple[bool, str]:
        """Appends data to a binary file."""
        try:
            with open(filePath, 'ab') as f:
                f.write(data)
            return True, ""
        except Exception as e:
            return False, str(e)

    @staticmethod
    def GetBinaryFileSize(filePath: str) -> tuple[bool, int]:
        """Returns the size of a binary file."""
        try:
            size = os.path.getsize(filePath)
            return True, size
        except Exception as e:
            return False, str(e)

    # 5. Encryption and Decryption (using cryptography)
    @staticmethod
    def EncryptFile(filePath: str, key: bytes) -> tuple[bool, str]:
        """Encrypts the content of a file using AES encryption."""
        try:
            with open(filePath, 'rb') as f:
                data = f.read()

            # AES encryption setup
            cipher = Cipher(algorithms.AES(key), modes.CBC(os.urandom(16)), backend=default_backend())
            padder = padding.PKCS7(algorithms.AES.block_size).padder()
            padded_data = padder.update(data) + padder.finalize()
            encryptor = cipher.encryptor()
            encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

            # Save encrypted file
            with open(filePath + ".enc", 'wb') as f_enc:
                f_enc.write(cipher.iv)  # Prepend IV for later decryption
                f_enc.write(encrypted_data)

            return True, ""
        except Exception as e:
            return False, str(e)

    @staticmethod
    def DecryptFile(filePath: str, key: bytes) -> tuple[bool, str]:
        """Decrypts an encrypted file."""
        try:
            with open(filePath, 'rb') as f:
                iv = f.read(16)  # Extract IV
                encrypted_data = f.read()

            # AES decryption setup
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

            # Unpadding decrypted data
            unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
            unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

            # Save decrypted file
            with open(filePath.replace('.enc', '.dec'), 'wb') as f_dec:
                f_dec.write(unpadded_data)

            return True, ""
        except Exception as e:
            return False, str(e)
        
    @staticmethod
    def Base64EncodeFile(filePath: str) -> tuple[bool, str]:
        """Encodes a file in Base64 format."""
        try:
            with open(filePath, 'rb') as f:
                encoded = binascii.b2a_base64(f.read())
            with open(filePath + '.b64', 'wb') as f_enc:
                f_enc.write(encoded)
            return True, ""
        except Exception as e:
            return False, str(e)

    @staticmethod
    def Base64DecodeFile(filePath: str) -> tuple[bool, str]:
        """Decodes a Base64 encoded file."""
        try:
            with open(filePath, 'rb') as f:
                decoded = binascii.a2b_base64(f.read())
            with open(filePath.replace('.b64', ''), 'wb') as f_dec:
                f_dec.write(decoded)
            return True, ""
        except Exception as e:
            return False, str(e)

class FileSystem(BasicFileSystem, JsonFileSystem, LowFileSystem):
    @staticmethod
    def CreateFile(filePath:str, data:str) -> tuple[bool, str]:
        """Creates a new file with the provided data.
        
        Args:
            filePath (str): The path to the file to be created.
            date (Union[str, dict, int]) : The data to be inserted into the file.
            
        Returns:
            tuple[bool, str] ->
                bool: True if successful, False otherwise.
                str: The Error if success was False.
            
        Calls (Without raising):
            PheonixException: If an Unknown Error occurs during creation.
            PheonixIOError: If an Input/Output Error occurs during creation."""
        return super(BasicFileSystem, BasicFileSystem).CreateFile(filePath, data)
    
    @staticmethod
    def AppendFile(filePath: str, data: Union[str, int, dict], seek: Optional[Union[None, int]] = None) -> tuple[bool, str]:
        """Appends the data to the given filePath.

        Args:
            filePath (str): The path to the file to append.
            data (Union[str, int, dict]): The data to append in the file.
            seek (Optional) (Union[None, int]): The seek position. 'None' means to append at the end of the file. Defaults to None.

        Returns:
            tuple[bool, str] -> 
                bool: True if successful, False otherwise.
                str: The Error if success was False

        Calls (Without raising):
            PheonixException: If an Unknown Error occurs during creation.
            PheonixIOError: If an Input/Output Error occurs during creation.
            PheonixFileNotFoundError: If file was not found."""
        return super(BasicFileSystem, FileSystem).AppendFile(filePath, data, seek)

    @staticmethod
    def ReadFile(filePath: str) -> tuple[bool, Union[str, None]]:
        """Reads the content of the file.

        Args:
            filePath (str): The path to the file to read.

        Returns:
            tuple[bool, Union[str, None]] -> 
                bool: True if successful, False otherwise.
                str: The content of the file if successful, or error message if not.

        Calls (Without raising):
            PheonixException: If an Unknown Error occurs during reading.
            PheonixFileNotFoundError: If file was not found."""
        return super(BasicFileSystem, FileSystem).ReadFile(filePath)

    @staticmethod
    def DeleteFile(filePath: str) -> tuple[bool, str]:
        """Deletes the specified file.

        Args:
            filePath (str): The path to the file to delete.

        Returns:
            tuple[bool, str] -> 
                bool: True if successful, False otherwise.
                str: The error message if unsuccessful.

        Calls (Without raising):
            PheonixFileNotFoundError: If file was not found."""
        return super(BasicFileSystem, FileSystem).DeleteFile(filePath)

    @staticmethod
    def RenameFile(oldPath: str, newPath: str) -> tuple[bool, str]:
        """Renames a file from `oldPath` to `newPath`.

        Args:
            oldPath (str): The current path of the file to rename.
            newPath (str): The new name/path of the file.

        Returns:
            tuple[bool, str] -> 
                bool: True if successful, False otherwise.
                str: The error message if unsuccessful.

        Calls (Without raising):
            PheonixFileNotFoundError: If file was not found."""
        return super(BasicFileSystem, FileSystem).RenameFile(oldPath, newPath)

    @staticmethod
    def FileExists(filePath: str) -> tuple[bool, str]:
        """Checks if the file exists at the specified path.

        Args:
            filePath (str): The path to check.

        Returns:
            tuple[bool, str] -> 
                bool: True if the file exists, False otherwise.
                str: An appropriate message."""
        return super(BasicFileSystem, FileSystem).FileExists(filePath)

    @staticmethod
    def GetFileSize(filePath: str) -> tuple[bool, Union[int, str]]:
        """Returns the size of the specified file.

        Args:
            filePath (str): The path to the file.

        Returns:
            tuple[bool, Union[int, str]] -> 
                bool: True if successful, False otherwise.
                int: The size of the file in bytes if successful.
                str: Error message if unsuccessful.

        Calls (Without raising):
            PheonixFileNotFoundError: If file was not found."""
        return super(BasicFileSystem, FileSystem).GetFileSize(filePath)

    @staticmethod
    def CopyFile(srcPath: str, destPath: str) -> tuple[bool, str]:
        """Copies a file from the source path to the destination path.

        Args:
            srcPath (str): The source file path.
            destPath (str): The destination file path.

        Returns:
            tuple[bool, str] -> 
                bool: True if successful, False otherwise.
                str: Error message if unsuccessful.

        Calls (Without raising):
            PheonixFileNotFoundError: If the source file does not exist."""
        return super(BasicFileSystem, FileSystem).CopyFile(srcPath, destPath)

    @staticmethod
    def MoveFile(srcPath: str, destPath: str) -> tuple[bool, str]:
        """Moves a file from the source path to the destination path.

        Args:
            srcPath (str): The source file path.
            destPath (str): The destination file path.

        Returns:
            tuple[bool, str] -> 
                bool: True if successful, False otherwise.
                str: Error message if unsuccessful.

        Calls (Without raising):
            PheonixFileNotFoundError: If the source file does not exist."""
        return super(BasicFileSystem, FileSystem).MoveFile(srcPath, destPath)

    @staticmethod
    def CreateDirectory(dirPath: str) -> tuple[bool, str]:
        """Creates a directory at the specified path.

        Args:
            dirPath (str): The path where the directory will be created.

        Returns:
            tuple[bool, str] -> 
                bool: True if successful, False otherwise.
                str: Error message if unsuccessful.
        """
        return super(BasicFileSystem, FileSystem).CreateDirectory(dirPath)
    
    @staticmethod
    def CreateJsonFile(filePath: str, data: Union[dict, list]) -> tuple[bool, str]:
        """Creates a new JSON file with the provided data.
        
        Args:
            filePath (str): The path to the JSON file to be created.
            data (Union[dict, list]): The data to be inserted into the JSON file.

        Returns:
            tuple[bool, str] -> 
                bool: True if successful, False otherwise.
                str: The error message if unsuccessful.

        Calls (Without raising):
            PheonixException: If an unknown error occurs during file creation.
            PheonixIOError: If there is an input/output error during file creation."""
        return super(JsonFileSystem, JsonFileSystem).CreateJsonFile(filePath, data)

    @staticmethod
    def AppendJsonData(filePath: str, data: Union[dict, list]) -> tuple[bool, str]:
        """Appends data to an existing JSON file.

        Args:
            filePath (str): The path to the JSON file to append data.
            data (Union[dict, list]): The data to be appended.

        Returns:
            tuple[bool, str] -> 
                bool: True if successful, False otherwise.
                str: Error message if unsuccessful.

        Calls (Without raising):
            PheonixFileNotFoundError: If the file is not found.
            PheonixIOError: If an input/output error occurs."""
        return super(JsonFileSystem, JsonFileSystem).AppendJsonData(filePath, data)

    @staticmethod
    def ReadJsonFile(filePath: str) -> tuple[bool, Union[dict, list, str]]:
        """Reads data from a JSON file.

        Args:
            filePath (str): The path to the JSON file.

        Returns:
            tuple[bool, Union[dict, list, str]] -> 
                bool: True if successful, False otherwise.
                dict/list: The contents of the file if successful, error message if not.

        Calls (Without raising):
            PheonixFileNotFoundError: If file not found.
            PheonixIOError: If an input/output error occurs."""
        return super(JsonFileSystem, JsonFileSystem).ReadJsonFile(filePath)

    @staticmethod
    def DeleteJsonFile(filePath: str) -> tuple[bool, str]:
        """Deletes a JSON file.

        Args:
            filePath (str): The path to the JSON file to be deleted.

        Returns:
            tuple[bool, str] -> 
                bool: True if successful, False otherwise.
                str: The error message if unsuccessful.

        Calls (Without raising):
            PheonixFileNotFoundError: If file does not exist."""
        return super(JsonFileSystem, JsonFileSystem).DeleteJsonFile(filePath)

    @staticmethod
    def FileExists(filePath: str) -> bool:
        """Checks if the JSON file exists.

        Args:
            filePath (str): The path to the JSON file.

        Returns:
            bool: True if the file exists, False otherwise."""
        return super(JsonFileSystem, JsonFileSystem).FileExists(filePath)

    @staticmethod
    def GetJsonKeys(filePath: str) -> tuple[bool, Union[list, str]]:
        """Returns all keys in a JSON file (if it is a JSON object).

        Args:
            filePath (str): The path to the JSON file.

        Returns:
            tuple[bool, Union[list, str]] -> 
                bool: True if successful, False otherwise.
                list: List of keys if file is a dictionary, error message if not.

        Calls (Without raising):
            PheonixFileNotFoundError: If file does not exist."""
        return super(JsonFileSystem, JsonFileSystem).GetJsonKeys(filePath)

    @staticmethod
    def GetJsonFileSize(filePath: str) -> tuple[bool, Union[int, str]]:
        """Returns the size of the JSON file.

        Args:
            filePath (str): The path to the JSON file.

        Returns:
            tuple[bool, Union[int, str]] -> 
                bool: True if successful, False otherwise.
                int: File size in bytes if successful, error message if not.

        Calls (Without raising):
            PheonixFileNotFoundError: If file does not exist."""
        return super(JsonFileSystem, JsonFileSystem).GetJsonFileSize(filePath)

    @staticmethod
    def UpdateJsonKey(filePath: str, key: str, new_value: Union[str, int, dict, list]) -> tuple[bool, str]:
        """Updates the value of a specific key in a JSON file.

        Args:
            filePath (str): The path to the JSON file.
            key (str): The key whose value needs to be updated.
            new_value (Union[str, int, dict, list]): The new value to update.

        Returns:
            tuple[bool, str] -> 
                bool: True if successful, False otherwise.
                str: The error message if unsuccessful.

        Calls (Without raising):
            PheonixFileNotFoundError: If file does not exist."""
        return super(JsonFileSystem, JsonFileSystem).UpdateJsonKey(filePath, key, new_value)

    @staticmethod
    def ValidateJson(filePath: str) -> tuple[bool, str]:
        """Validates if a file is a valid JSON.

        Args:
            filePath (str): The path to the JSON file.

        Returns:
            tuple[bool, str] -> 
                bool: True if valid, False otherwise.
                str: The error message if invalid.

        Calls (Without raising):
            PheonixFileNotFoundError: If file not found."""
        return super(JsonFileSystem, JsonFileSystem).ValidateJson(filePath)

    @staticmethod
    def GetJsonFileExtension(filePath: str) -> tuple[bool, str]:
        """Gets the file extension of a JSON file.

        Args:
            filePath (str): The path to the JSON file.

        Returns:
            tuple[bool, str] -> 
                bool: True if successful, False otherwise.
                str: The file extension ('.json') if successful, error message if not."""
        return super(JsonFileSystem, JsonFileSystem).GetJsonFileExtension(filePath)

    @staticmethod
    def MergeJsonFiles(srcPath: str, destPath: str) -> tuple[bool, str]:
        """Merges two JSON files.

        Args:
            srcPath (str): The source JSON file path.
            destPath (str): The destination JSON file path.

        Returns:
            tuple[bool, str] -> 
                bool: True if successful, False otherwise.
                str: The error message if unsuccessful.

        Calls (Without raising):
            PheonixFileNotFoundError: If any file is not found."""
        return super(JsonFileSystem, JsonFileSystem).MergeJsonFiles(srcPath, destPath)

    @staticmethod
    def CreateJsonBackup(filePath: str) -> tuple[bool, str]:
        """Creates a backup of a JSON file.

        Args:
            filePath (str): The path to the JSON file to be backed up.

        Returns:
            tuple[bool, str] -> 
                bool: True if successful, False otherwise.
                str: The error message if unsuccessful."""
        return super(JsonFileSystem, JsonFileSystem).CreateJsonBackup(filePath)

    @staticmethod
    def RenameJsonFile(filePath: str, new_name: str) -> tuple[bool, str]:
        """Renames an existing JSON file.

        Args:
            filePath (str): The path to the existing JSON file.
            new_name (str): The new name for the file.

        Returns:
            tuple[bool, str] -> 
                bool: True if successful, False otherwise.
                str: The error message if unsuccessful."""
        return super(JsonFileSystem, JsonFileSystem).RenameJsonFile(filePath, new_name)

    @staticmethod
    def GetJsonFileInfo(filePath: str) -> tuple[bool, str]:
        """Gets the basic information (size, keys) about a JSON file.

        Args:
            filePath (str): The path to the JSON file.

        Returns:
            tuple[bool, str] -> 
                bool: True if successful, False otherwise.
                str: The error message if unsuccessful."""
        return super(JsonFileSystem, JsonFileSystem).GetJsonFileInfo(filePath)

    @staticmethod
    def ReadJsonKey(filePath: str, key: str) -> tuple[bool, Union[str, dict, list]]:
        """Reads the value of a specific key from a JSON file.

        Args:
            filePath (str): The path to the JSON file.
            key (str): The key whose value needs to be read.

        Returns:
            tuple[bool, Union[str, dict, list]] -> 
                bool: True if successful, False otherwise.
                str/dict/list: The value of the key, or error message if not found."""
        return super(JsonFileSystem, JsonFileSystem).ReadJsonKey(filePath, key)

    @staticmethod
    def SetJsonKey(filePath: str, key: str, value: Union[str, int, dict, list]) -> tuple[bool, str]:
        """Sets the value of a specific key in a JSON file.

        Args:
            filePath (str): The path to the JSON file.
            key (str): The key whose value needs to be set.
            value (Union[str, int, dict, list]): The value to set for the key.

        Returns:
            tuple[bool, str] -> 
                bool: True if successful, False otherwise.
                str: The error message if unsuccessful."""
        return super(JsonFileSystem, JsonFileSystem).SetJsonKey(filePath, key, value)

    @staticmethod
    def CreateEmptyJson(filePath: str) -> tuple[bool, str]:
        """Creates an empty JSON file.

        Args:
            filePath (str): The path where the empty JSON file will be created.

        Returns:
            tuple[bool, str] -> 
                bool: True if successful, False otherwise.
                str: The error message if unsuccessful."""
        return super(JsonFileSystem, JsonFileSystem).CreateEmptyJson(filePath)

    @staticmethod
    def CopyJsonFile(srcPath: str, destPath: str) -> tuple[bool, str]:
        """Copies a JSON file to a new location.

        Args:
            srcPath (str): The source JSON file path.
            destPath (str): The destination file path.

        Returns:
            tuple[bool, str] -> 
                bool: True if successful, False otherwise.
                str: The error message if unsuccessful."""
        return super(JsonFileSystem, JsonFileSystem).CopyJsonFile(srcPath, destPath)
    
    # 1. ASM File Handling
    @staticmethod
    def CreateAsmFile(filePath: str, asmContent: str) -> tuple[bool, str]:
        """Creates a new ASM file with the provided ASM content."""
        return super(FileSystem, FileSystem).CreateAsmFile(filePath, asmContent)

    @staticmethod
    def ReadAsmFile(filePath: str) -> tuple[bool, str]:
        """Reads content from an ASM file."""
        return super(FileSystem, FileSystem).ReadAsmFile(filePath)

    @staticmethod
    def CompileAsmToObject(filePath: str) -> tuple[bool, str]:
        """Compiles an ASM file to an object (.o) file."""
        return super(FileSystem, FileSystem).CompileAsmToObject(filePath)

    @staticmethod
    def DisassembleAsmFile(filePath: str) -> tuple[bool, str]:
        """Disassembles an ASM file to inspect the assembly instructions."""
        return super(FileSystem, FileSystem).DisassembleAsmFile(filePath)

    @staticmethod
    def CreateAsmFromString(asmCode: str, outputFile: str) -> tuple[bool, str]:
        """Creates an ASM file from a string of ASM code."""
        return super(FileSystem, FileSystem).CreateAsmFromString(asmCode, outputFile)

    # 2. Object File (.O) Handling
    @staticmethod
    def CreateObjectFile(filePath: str) -> tuple[bool, str]:
        """Creates an object (.o) file from a C/C++ file."""
        return super(FileSystem, FileSystem).CreateObjectFile(filePath)

    @staticmethod
    def LinkObjectFiles(objFiles: list[str], outputFile: str) -> tuple[bool, str]:
        """Links multiple object (.o) files into an executable."""
        return super(FileSystem, FileSystem).LinkObjectFiles(objFiles, outputFile)

    @staticmethod
    def DisassembleObjectFile(objFilePath: str) -> tuple[bool, str]:
        """Disassembles an object file to inspect the assembly instructions."""
        return super(FileSystem, FileSystem).DisassembleObjectFile(objFilePath)

    # 3. C and C++ File Handling
    @staticmethod
    def CreateCFile(filePath: str, cContent: str) -> tuple[bool, str]:
        """Creates a new C file with the provided C code."""
        return super(FileSystem, FileSystem).CreateCFile(filePath, cContent)

    @staticmethod
    def CompileCToObject(filePath: str) -> tuple[bool, str]:
        """Compiles a C file to an object (.o) file."""
        return super(FileSystem, FileSystem).CompileCToObject(filePath)

    @staticmethod
    def CreateCppFile(filePath: str, cppContent: str) -> tuple[bool, str]:
        """Creates a new C++ file with the provided C++ code."""
        return super(FileSystem, FileSystem).CreateCppFile(filePath, cppContent)

    @staticmethod
    def CompileCppToObject(filePath: str) -> tuple[bool, str]:
        """Compiles a C++ file to an object (.o) file."""
        return super(FileSystem, FileSystem).CompileCppToObject(filePath)

    @staticmethod
    def CompileCPlusPlusFile(filePath: str) -> tuple[bool, str]:
        """Compiles a C++ file into an executable."""
        return super(FileSystem, FileSystem).CompileCPlusPlusFile(filePath)

    # 4. Binary File Handling
    @staticmethod
    def ReadBinaryFile(filePath: str) -> tuple[bool, bytes]:
        """Reads data from a binary file."""
        return super(FileSystem, FileSystem).ReadBinaryFile(filePath)

    @staticmethod
    def WriteBinaryFile(filePath: str, data: bytes) -> tuple[bool, str]:
        """Writes data to a binary file."""
        return super(FileSystem, FileSystem).WriteBinaryFile(filePath, data)

    @staticmethod
    def AppendBinaryFile(filePath: str, data: bytes) -> tuple[bool, str]:
        """Appends data to a binary file."""
        return super(FileSystem, FileSystem).AppendBinaryFile(filePath, data)

    @staticmethod
    def GetBinaryFileSize(filePath: str) -> tuple[bool, int]:
        """Returns the size of a binary file."""
        return super(FileSystem, FileSystem).GetBinaryFileSize(filePath)

    # 5. Encryption and Decryption (using cryptography)
    @staticmethod
    def EncryptFile(filePath: str, key: bytes) -> tuple[bool, str]:
        """Encrypts the content of a file using AES encryption."""
        return super(FileSystem, FileSystem).EncryptFile(filePath, key)

    @staticmethod
    def DecryptFile(filePath: str, key: bytes) -> tuple[bool, str]:
        """Decrypts an encrypted file."""
        return super(FileSystem, FileSystem).DecryptFile(filePath, key)
        
    @staticmethod
    def Base64EncodeFile(filePath: str) -> tuple[bool, str]:
        """Encodes a file in Base64 format."""
        return super(FileSystem, FileSystem).Base64EncodeFile(filePath)

    @staticmethod
    def Base64DecodeFile(filePath: str) -> tuple[bool, str]:
        """Decodes a Base64 encoded file."""
        return super(FileSystem, FileSystem).Base64DecodeFile(filePath)