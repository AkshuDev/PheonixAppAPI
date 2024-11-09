from typing import *

class PheonixException(Exception):
    """The BaseClass for all Pheonix Related Exceptions.

    Args:
        message (str): The message to provide upon exception.
    """
    def __init__(self, message:str):
        self.message = message
        super().__init__(self.message)

class NotAccessFile(PheonixException):
    """The Error indicating that the file given is not an Access file.

    Args:
        message (str): The message to provide upon exception.
    """
    pass

class InvalidType(PheonixException):
    """The Error indicating that the provided argument's type is not valid.

    Args:
        message (str): The message to provide upon exception.
    """
    pass

class ErrorWhileCreatingFile(PheonixException):
    """The Error indicating that an issue occurred while creating the/a file.

    Args:
        message (str): The message to provide upon exception.
    """
    pass

class ModuleDoesntExist(PheonixException):
    """The Error indicating that a module does not exist.

    Args:
        message (str): The message to provide upon exception.
    """
    pass

class ErrorOccuredWhileInstallingModule(PheonixException):
    """The Error indicating that an issue occurred while installing a module.

    Args:
        message (str): The message to provide upon exception.
    """
    pass

class NoInternet(PheonixException):
    """The Error indicating that there is no network connection.

    Args:
        message (str): The message to provide upon exception.
    """
    pass