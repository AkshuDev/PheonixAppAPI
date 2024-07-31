import json
from typing import *

class JsonFileManager:
    """This class is used to work with Json objects

        Args:
            path (str): The path to the Json File.
        """
    def __init__(self, path:str) -> None:
        """This class is used to work with Json objects

        Args:
            path (str): The path to the Json File.
        """
        path = path

    def JsonToDict(self) -> dict:
        """Converts a Json object to a dictionary.

        Returns:
            dict: The output.
        """
        data = {}
        with open(self.path, 'r') as f:
            f.seek(0)
            data = json.loads(f.read())
            f.close()

        return data

    def Object_Push(self, content, mode:str="w") -> None:
        """This creates/writes/appends a json file the provided contents.

        Args:
            content (Any): The content to push.
            mode (str, optional): The mode that will be used to open the file. Defaults to 'w'.
        """
        with open(self.path, mode) as f:
            json.dump(content, f)
