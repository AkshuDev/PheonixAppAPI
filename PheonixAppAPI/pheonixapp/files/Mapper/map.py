import os
import sys
import json
import random

from PheonixAppAPI.pheonixapp.files import HashDecoderT
from PheonixAppAPI import bin_worker

if __name__ == "__main__":
    print("This cannot be used in the terminal.")
    exit(1)

class Map():
    """
    A class to create, store, and retrieve a map for an encoder.

    Attributes:
    name (str): The name of the map.
    map_ (dict): The dictionary representing the map.
    map (str): The string representation of the map.
    """
    def __init__(self, name:str, map:dict={}) -> None:
        """
        Initializes the Map with a name and an optional map dictionary.

        Args:
        name (str): The name of the map.
        map (dict, optional): The dictionary representing the map. Defaults to an empty dictionary.
        """
        self.map_ = map
        self.map = str(map)
        self.name = name

    def create_map(self, keys:str="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~") -> dict:
        """
        Creates a dictionary where each key is a character and each value is a unique, randomly assigned character.

        Args:
        keys (str, optional): The string of characters to use as keys and values. Defaults to a comprehensive set of keyboard characters.

        Returns:
        dict: A dictionary mapping each character to a unique, random character.
        """
        dict_ = {}
        used_val = []
        keys__ = keys
        keys_ = list(keys)
        keys = list(keys)

        random.shuffle(keys)

        for char in keys:
            available_val = [c for c in keys__ if not c in used_val]
            if not available_val:
                break

            value = random.choice(available_val)
            dict_[char] = value
            used_val.append(value)

        dict_ = {k: v for k, v in dict_.items() if v}

        return dict_

    def push_map(self) -> None:
        """
        Writes the map to an encrypted file. Creates the file if it does not exist.
        """
        if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "maps.encMaps")):
            pass
        else:
            with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "maps.encMaps"), "w") as file:
                file.seek(0)
                file.write(HashDecoderT.Encode(json.dumps({"Example": {"key": "value"}}), "Hype_Space_BIN", "Community").run())
                file.close()

        data = {}

        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "maps.encMaps"), "r") as file:
            file.seek(0)
            data = file.read()
            data = json.loads(HashDecoderT.Decode(data, "Hype_Space_BIN").run())
            file.close()

        print(HashDecoderT.Encode(json.dumps(self.map_), "Hype_Space_BIN", "Community").run())
        data[self.name] = self.map_

        data = HashDecoderT.Encode(json.dumps(data), "Hype_Space_BIN", "Community").run()

        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "maps.encMaps"), "w") as file:
                file.seek(0)
                file.write(data)
                file.close()

    def get_map(self) -> dict:
        """
        Retrieves and decrypts the map from the encrypted file.

        Returns:
        dict: The decrypted map.

        Raises:
        Exception: If the map file does not exist.
        """
        if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "maps.encMaps")):
            raise Exception("No Map File to begin with.")

        data = {}

        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "maps.encMaps"), "r") as file:
            file.seek(0)
            data = json.loads(HashDecoderT.Decode(file.read(), "Hype_Space_BIN").run())
            file.close()

        data = data[self.name]

        return data

    def remove_maps(self, mode:str="one", names:list=[]) -> None:
        """A function to remove maps from the file.

    Attributes:
    mode (str): The name of the map.

    Available ->
    1. one: Only removes the map that is at the first of the names list.
    2. list: Removes all the maps that are present in the names list.
    3. all: Removes all the maps except the default ones.

    names(list): The list of names to remove. If [mode] is [one] then only the first map in this list is removed.

    Raises:
    Exception: No Map File to begin with.

    Returns:
    None: Nothing."""

        maps_fileP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "maps.encMaps")
        data:dict = {}

        if not os.path.exists(maps_fileP):
            raise Exception("No Map File to begin with.")

        with open(maps_fileP, "r") as file:
            file.seek(0)
            data = json.loads(HashDecoderT.Decode(file.read(), "Hype_Space_BIN").run())
            file.close()

        if mode == "one":
            if names and names[0] in data and names[0] != "Example":
                del data[names[0]]
        elif mode == "list":
            for name in names:
                if name in data and name != "Example":
                    del data[name]
        elif mode == "all":
            data = {"Example": {"key": "value"}}

        with open(maps_fileP, "w") as file:
            file.seek(0)
            file.write(HashDecoderT.Encode(json.dumps(data), "Hype_Space_BIN", "Community").run())
            file.close()