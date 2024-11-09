from typing import *

################################################################

# PHardwareITK Errors

class PHardwareITKException(Exception):
    def __init__(self, message:str="", *args) -> None:
        super().__init__(message)

class PHardwareITK_RuntimeError(Exception):
    def __init__(self, message:str="", *args) -> None:
        super().__init__(message)

class PHardwareITK_NotSupportedError(Exception):
    def __init__(self, message:str="", *args) -> None:
        super().__init__(message)

class PHardwareITK_ValueError(Exception):
    def __init__(self, message:str="", *args) -> None:
        super().__init__(message)

class PHardwareITK_ParserError(Exception):
    def __init__(self, message:str="", *args) -> None:
        super().__init__(message)

class PHardwareITK_SettingsError(Exception):
    def __init__(self, message:str="", *args) -> None:
        super().__init__(message)

class PHardwareITK_FileError(Exception):
    def __init__(self, message:str="", *args) -> None:
        super().__init__(message)

class PHardwareITK_FileNotFoundError(Exception):
    def __init__(self, message:str="", *args) -> None:
        super().__init__(message)

class PHardwareITK_IOError(Exception):
    def __init__(self, message:str="", *args) -> None:
        super().__init__(message)

# Pheonix Errors

class PheonixException(Exception):
    def __init__(self, message:str="", *args) -> None:
        super().__init__(message)

class PheonixFileNotFoundError(Exception):
    def __init__(self, message:str="", *args) -> None:
        super().__init__(message)

class PheonixInternalError(Exception):
    def __init__(self, message:str="", *args) -> None:
        super().__init__(message)

class PheonixValuerError(Exception):
    def __init__(self, message:str="", *args) -> None:
        super().__init__(message)

class PheonixArgumentError(Exception):
    def __init__(self, message:str="", *args) -> None:
        super().__init__(message)

class PheonixSettingsError(Exception):
    def __init__(self, message:str="", *args) -> None:
        super().__init__(message)

class PheonixObjectError(Exception):
    def __init__(self, message:str="", *args) -> None:
        super().__init__(message)

class PheonixOsError(Exception):
    def __init__(self, message:str="", *args) -> None:
        super().__init__(message)

class PheonixOsVersionError(Exception):
    def __init__(self, message:str="", *args) -> None:
        super().__init__(message)

class PheonixVersionNotSupported(Exception):
    def __init__(self, message:str="", *args) -> None:
        super().__init__(message)

class PheonixUnknownVersion(Exception):
    def __init__(self, message:str="", *args) -> None:
        super().__init__(message)

class PheonixUnknownSetting(Exception):
    def __init__(self, message:str="", *args) -> None:
        super().__init__(message)

class PheonixIOError(Exception):
    def __init__(self, message:str="", *args) -> None:
        super().__init__(message)

# Custom Errors

class CustomError(Exception):
    """Custom Error
    
    Args:
        name (str): The name of the Exception.
        message (str): The message displayed.
        *args (Any): Other Arguments.
        
    Calls:
        Exception"""
    def __init__(self, name:str, message:str="", *args) -> None:
        self.name = name
        self.message = message

        super().__init__(message)

    def __str__(self):
        return f"{self.name}: {self.message}"

class RunCustomError(): # Same as CustomError
    """Run Custom Error
    
    Args:
        name (str): The name of the Exception.
        message (str): The message displayed.
        *args (Any): Other Arguments.
        
    Calls:
        CustomError -> Exception
        
    NOTE: Same as Custom Error."""
    def __init__(self, name:str, message:str="", *args) -> None:
        raise CustomError(name, message, *args)