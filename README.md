 __________.__                        .__           _________ __            .___.__
 \______   \  |__   ____  ____   ____ |__|__  ___  /   _____//  |_ __ __  __| _/|__| ____  ______
  |     ___/  |  \_/ __ \/  _ \ /    \|  \  \/  /  \_____  \\   __\  |  \/ __ | |  |/  _ \/  ___/
  |    |   |   Y  \  ___(  <_> )   |  \  |>    <   /        \|  | |  |  / /_/ | |  (  <_> )___ \
  |____|   |___|  /\___  >____/|___|  /__/__/\_ \ /_______  /|__| |____/\____ | |__|\____/____  >
                \/     \/           \/         \/         \/                 \/               \/

Pheonix App 1.0


Overview


Pheonix App 1.0 is a powerful Python application designed to streamline various tasks, from managing files to playing mini-games. This README provides comprehensive instructions on how to use the app effectively.

Getting

To start the app, follow these steps:

Open PheonixStudiosStarter.py.
Run the script in your terminal.
Upon execution, the terminal will prompt you with a command line, starting with your current directory path.

Usage

GUI Mode
To switch to GUI mode, use the following command:



gui start


Mini-Games
To play a mini-game, use the following command format:



fun !minigame [minigame_name]


Replace [minigame_name] with the name of the mini-game you want to play.

Terminal Mode


For terminal mode, use the same command format as displayed when starting the app:



C:/Users/main/mydir/pheonixapp1.0/files ->


Devtools
To enable or disable devtools, use the following commands:



terminal !devtools:ENABLE


terminal !devtools:DISABLE


Release Mode


To enable or disable release mode, use the following command:



terminal !devtools:CLcmds:T:release


PATF File Commands


To work with the PATF (Pheonix App Terminal File) file, use the following commands:


terminal --createfile: Creates a fresh PATF file with information from the old one.
terminal --deletefile: Deletes the PATF file (shuts down the app as the file is required to work).
terminal --modifyfile: Modifies the PATF file.
terminal --upgradefile: Upgrades PATF file information and then creates the file.
terminal --changefiletype:(file_type): Changes the file type. Available file types are patf, txt, and ini.
terminal !clear: Clears the terminal screen.
terminal !color:(color_number): Changes the color of text in the terminal. Use DEFAULT to revert to default color.
terminal !utilities:(utility_name): Starts the utilities function. Available utilities are calc and wiki.


Utilities


Utilities calc: Starts a calculator.
Utilities wiki: Performs a Wikipedia search.


Installation

To install the required modules or dependencies, run PheonixStudiosStarter.py. The script will automatically install necessary packages. Additionally, Pheonix App can be installed via PACI (Pheonix App Community Installer) software or downloaded at [https://pheonixntx.wixsite.com/paos/blank](Pheonix Studios AOS Site).

To install this module just use this command -> pip install PheonixappAPI


PheonixAppAPI

To start import the files -> (api.py, main.py)

Then do -> main.INITIALIZE(LoginOrSignup:bool=False, email:str="", username:str="", password:str="")

First argument is LoginOrSignup, If you want to signup and use it then make it True else False
Other arguments are your login arguments

api File

Initialization
Create an instance of the PATF_API class:

from pheonixapp.files import PSSbridge

PATF = PSSbridge.API(True)

class PATF_API():
    def __init__(self, useFileData:bool=False, email:str="", username:str="", password:str="") -> None:
        self.useFileData = useFileData
        self.email = email
        self.username = username
        self.password = password
        self.patf = PSSbridge.API(useFileData, email, username, password)

GUI Mode
To start the GUI mode, use the GUI class:

class GUI():
    def __init__(self) -> None:
        pass

    def start(self) -> None:
        PATF.run("gui start")

# Example usage
gui = GUI()
gui.start()
Mini-Games

To play the "Guess The Number" mini-game, use the MiniGames class:

class MiniGames():
    def __init__(self) -> None:
        pass

    def GuessTheNumber(self) -> None:
        PATF.run("fun !minigame guessthenumber")

# Example usage
games = MiniGames()
games.GuessTheNumber()


PATF Commands
Use the PATF_API class to manage the PATF file and perform other related tasks:

Examples ->

Creating a PATF File

# Example Usage

patf_api = PATF_API()
patf_api.run("terminal --createfile")

Checking Modules

# Example Usage

patf_api = PATF_API()
patf_api.CheckModules(mode="all", list=["module1", "module2"])


Getting Certificate path

# Example Usage

patf_api = PATF_API()
path = patf_api.getCertificatePath(code="12345", flag="+BOOL")
print(path)

Encoding and Decoding Messages

Encoding

# Example Usage

encoder = Encoder(msg="YourMessage", type="Hype_Space")
encoded_message = encoder.Encode()
print(encoded_message)


Decoding

# Example Usage

decoder = Decoder(msg="EncodedMessage", type_="Hype_Space")
decoded_message = decoder.Decode()
print(decoded_message)


Utilities

Calculator

# Example Usage

utils = Utilities()
utils.Calc_Terminal()
Wikipedia Search


utils.Wiki_Terminal()


Error Handling

# Example Usage

try:
    # Your code that may raise an exception
    pass
except Exception as e:
    Error(type_=e, name="ErrorName", details="Error details", log=False, mode="")


Extra Commands

# Example Usage

extra_cmd = Extra_Commands(cmd="your_command")
extra_cmd.Terminal_run()
Extra Functions

# Example Usage

extra = Extra()
extra.Object_Detector()
extra.HaCline()

Maps

Maps can be used for adding your own encryption language to PheonixAppAPI by a map (a dictionary with with keys as letters and values as the encryption of the letters)

# Example Usage

my_new_map = api.create_map()
api.push_map("My New Map", my_new_map)
my_map = api.get_map("My New Map")
api.remove_maps("one", ["My New Map"])

Functions ->

create_map ->

    Creates a dictionary where each key is a character and each value is a unique, randomly assigned character.

    Args:
    keys (str, optional): The string of characters to use as keys and values. Defaults to a comprehensive set of keyboard characters.

    Returns:
    dict: A dictionary mapping each character to a unique, random character.

push_map ->

    Writes the map to an encrypted file. Creates the file if it does not exist.

    Args:
    name (str): The name of the map to push.
    map_ (dict, optional): The dictionary map to push. Default Value is set to [{}].

    Returns:
    None: Nothing.

get_map ->

    Retrieves and decrypts the map from the encrypted file.

    Args:
    name (str): The name of the map to get.
    map_ (dict, optional): This is not required by the user as it is only used for creating the object.

    Returns:
    dict: The decrypted map.

    Raises:
    Exception: If the map file does not exist.

remove_maps ->

    A function to remove maps from the file.

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
    None: Nothing.

Binary Workings

How to work with binary using PheonixAppAPI

Bin functions can be used as well as from api.py and from retrieving the BIN class using [api.BIN(ARGS....)]. The BIN class does have more functions than the ones present in api.py hence, it is recommended to use BIN class instead of api.py functions.

# Example Usage

bin = api.BIN(path="test.bin", content="Hello")
print(bin.str_to_bin("Hello world"))
print(bin.bin_to_str(bin.str_to_bin("Hello world")))
print(bin.to_binINT("Hello world"))
print(bin.str_to_bytes("Hello world", "utf-16"))
print(bin.bytes_to_str(bin.str_to_bytes("Hello world", "utf-16"), "utf-16"))

bin.push_str()
data = bin.get_str()

Functions ->

str_to_bin ->

    Convert a string, integer, or dictionary to its binary string representation.

    Args:
    data (typing.Union[str, int, dict]): The data to convert to binary.

    Returns:
    str: The binary string representation of the input data.

bin_to_str ->

    Convert a binary string back to its original string representation.

    Args:
    data (str): The binary string to convert.

    Returns:
    str: The original string representation of the binary input.

to_binINT ->

    Convert a dictionary or string to a binary integer.

    Args:
    data_dict (dict, optional): The dictionary to convert. Defaults to an empty dictionary.
    data_str (str, optional): The string to convert. Defaults to an empty string.
    useString (bool, optional): Flag to indicate if data_str should be used. Defaults to True.

    Returns:
    int: The binary integer representation of the input data.

str_to_bytes ->

    Convert a string, integer, or dictionary to its byte representation.

    Args:
    data (typing.Union[str, int, dict]): The data to convert to bytes.
    encoding (str, optional): The encoding to use for the conversion. Defaults to "utf-16".

    Returns:
    bytes: The byte representation of the input data.

bytes_to_str ->

    Convert bytes back to a string using the specified encoding.

    Args:
    data (bytes): The byte data to convert.
    encoding (str, optional): The encoding to use for the conversion. Defaults to "utf-16".

    Returns:
    str: The string representation of the byte input.

api.BIN ->

    Returns the BIN class of bin_worker.py for working with binary.

    Args:
        path (str, optional): the path of the file while pushing data into file. Defaults to "./aol_var-dict.aolvd".
        format (str, optional): The format to set the content_dict into while pushing dict. Defaults to "vardict-v0.001JSON".
        encoding (str, optional): Encoding for the content or content_dict. Defaults to "utf-16".
        encode (bool, optional): To Encode The Data. Recommended to leave it as it is. Defaults to False.
        content (str, optional): The content in String. Defaults to "".
        content_dict (dict, optional): The content in dictionary. Defaults to {}.
        use_base64 (bool, optional): To encode using base64. NOTE: [low storage taking but less safe]. Defaults to False.
        use_pheonixApp_encoder (bool, optional): To encode using our Encoder. NOTE: [High Storage taking in compare to base64 but more safe (3 Layer Encryption)]. Defaults to True.
        compressed (bool, optional): To compress the size. After setting it to True the file will take less space but the Encryption will lose 1 layer. Defaults to False.
        hyper_compressed (bool, optional): To hyper-compress the size. After setting it to True the file will take less space but the Encryption will lose 2 layers. Defaults to False.

        NOTE: [This file is copied from our another program known as AOL(Assembly Orientated Language) and some of its functions are removed to match this Module]
    Returns:
        bin_worker.BIN: The class for working with binary

Support
For any assistance or inquiries, please contact the Pheonix Studios at [pheonix.community.mail@gmail.com]
