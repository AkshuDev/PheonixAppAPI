# Pheonix App 1.0

[![PyPI Downloads](https://static.pepy.tech/badge/pheonixappapi)](https://pepy.tech/projects/pheonixappapi)


## Overview


Pheonix App 1.0 is a powerful Python application designed to streamline various tasks, from managing files to playing mini-games. This README provides comprehensive instructions on how to use the app effectively.

## Getting Started

To start the app, follow these steps:

Open PheonixStudiosStarter.py.
Run the script in your terminal.
Upon execution, the terminal will prompt you with a command line, starting with your current directory path.

## Usage

## GUI Mode
To switch to GUI mode, use the following command:



    gui start


## Mini-Games
To play a mini-game, use the following command format:



    fun !minigame [minigame_name]


Replace **[minigame_name]** with the name of the mini-game you want to play.

## Terminal Mode


For terminal mode, use the same command format as displayed when starting the app:



    C:/Users/main/mydir/pheonixapp1.0/files ->


## Devtools
To enable or disable devtools, use the following commands:



    terminal !devtools:ENABLE


    terminal !devtools:DISABLE


## Release Mode


To enable or disable release mode, use the following command:



    terminal !devtools:CLcmds:T:release


## PATF File Commands


To work with the PATF (Pheonix App Terminal File) file, use the following commands:


**terminal --createfile**: Creates a fresh PATF file with information from the old one.

**terminal --deletefile**: Deletes the PATF file (shuts down the app as the file is required to work).

**terminal --modifyfile**: Modifies the PATF file.

**terminal --upgradefile**: Upgrades PATF file information and then creates the file.

**terminal --changefiletype**:(file_type): Changes the file type. Available file types are patf, txt, and ini.

**terminal !clear**: Clears the terminal screen.

**terminal !color:(color_number)**: Changes the color of text in the terminal. Use DEFAULT to revert to default color.

**terminal !utilities**:(utility_name): Starts the utilities function. Available utilities are calc and wiki.


## Utilities


Utilities calc: Starts a calculator.
Utilities wiki: Performs a Wikipedia search.


## Installation

To install the required modules or dependencies, run PheonixStudiosStarter.py. The script will automatically install necessary packages. Additionally, Pheonix App can be installed via PACI (Pheonix App Community Installer) software or downloaded at **[https://pheonixntx.wixsite.com/paos/blank](Pheonix Studios AOS Site)**.

To install this module just use this command : **pip install PheonixappAPI**


# PheonixAppAPI

To start import the files : **(api.py, main.py)**

Then do : **main.INITIALIZE(LoginOrSignup:bool=False, email:str="", username:str="", password:str="")**

First argument is LoginOrSignup, If you want to signup and use it then make it True else False
Other arguments are your login arguments

## api File

### Initialization
Create an instance of the PheonixAppAPI class:

    from PheonixAppAPI import main, api

    main_ = main.PheonixAppAPI(False).initialize()

    set_parent(main_)

## GUI Mode
To start the GUI mode, use the GUI class:

**api.GUI**

### Example usage

    gui = GUI()
    gui.start()

## Mini-Games

To play the "Guess The Number" mini-game, use the MiniGames class:

**api.MiniGames**

### Example usage
    games = MiniGames
    games.GuessTheNumber()


## PATF Commands
Use the PATF_API class to manage the PATF file and perform other related tasks:

### Examples :

#### Creating a PATF File

##### Example Usage

    patf_api = PATF_API()
    patf_api.run("terminal --createfile")

#### Checking Modules

##### Example Usage

    patf_api = PATF_API()
    patf_api.CheckModules(mode="all", list=["module1", "module2"])


#### Getting Certificate path

##### Example Usage

    patf_api = PATF_API()
    path = patf_api.getCertificatePath(code="12345", flag="+BOOL")
    print(path)

## Encoding and Decoding Messages

### Encoding

#### Example Usage

    encoder = Encoder(msg="YourMessage", type="Hype_Space")
    encoded_message = encoder.Encode()
    print(encoded_message)

### Decoding

#### Example Usage

    decoder = Decoder(msg="EncodedMessage", type_="Hype_Space")
    decoded_message = decoder.Decode()
    print(decoded_message)


## Utilities

### Calculator

#### Example Usage

    utils = Utilities()
    utils.Calc_Terminal()

### Wikipedia Search

#### Example Usage

    utils.Wiki_Terminal()

## Error Handling

### Example Usage

    try:
        # Your code that may raise an exception
        pass
    except Exception as e:
        Error(type_=e, name="ErrorName", details="Error details", log=False, mode="")


## Extra Commands

### Example Usage

    extra_cmd = Extra_Commands(cmd="your_command")
    extra_cmd.Terminal_run()

## Extra Functions

### Example Usage

    extra = Extra()
    extra.Object_Detector()
    extra.HaCline()

## Maps

Maps can be used for adding your own encryption language to PheonixAppAPI by a map (a dictionary with with keys as letters and values as the encryption of the letters)

### Example Usage

    my_new_map = api.create_map()
    api.push_map("My New Map", my_new_map)
    my_map = api.get_map("My New Map")
    api.remove_maps("one", ["My New Map"])

### Functions

#### create_map

Creates a dictionary where each key is a character and each value is a unique, randomly assigned character.

Args:

keys (str, optional): The string of characters to use as keys and values. Defaults to a comprehensive set of keyboard characters.

Returns:

dict: A dictionary mapping each character to a unique, random character.

#### push_map

Writes the map to an encrypted file. Creates the file if it does not exist.

Args:

name (str): The name of the map to push.

map_ (dict, optional): The dictionary map to push. Default Value is set to [{}].

Returns:

None: Nothing.

#### get_map

Retrieves and decrypts the map from the encrypted file.

Args:

name (str): The name of the map to get.

map_ (dict, optional): This is not required by the user as it is only used for creating the object.

Returns:

dict: The decrypted map.

Raises:

Exception: If the map file does not exist.

#### remove_maps

A function to remove maps from the file.

Attributes:

mode (str): The name of the map.

Available :

1. one: Only removes the map that is at the first of the names list.

2. list: Removes all the maps that are present in the names list.

3. all: Removes all the maps except the default ones.

names(list): The list of names to remove. If [mode] is [one] then only the first map in this list is removed.

Raises:

Exception: No Map File to begin with.

Returns:

None: Nothing.

## Binary Workings

How to work with binary using PheonixAppAPI

Bin functions can be used as well as from api.py and from retrieving the BIN class using [api.BIN(ARGS....)]. The BIN class does have more functions than the ones present in api.py hence, it is recommended to use BIN class instead of api.py functions.

### Example Usage

    bin = api.BIN(path="test.bin", content="Hello")
    print(bin.str_to_bin("Hello world"))
    print(bin.bin_to_str(bin.str_to_bin("Hello world")))
    print(bin.to_binINT("Hello world"))
    print(bin.str_to_bytes("Hello world", "utf-16"))
    print(bin.bytes_to_str(bin.str_to_bytes("Hello world", "utf-16"), "utf-16"))

    bin.push_str()
    data = bin.get_str()

### Functions

#### str_to_bin

Convert a string, integer, or dictionary to its binary string representation.

Args:

data (typing.Union[str, int, dict]): The data to convert to binary.

Returns:

str: The binary string representation of the input data.

#### bin_to_str

Convert a binary string back to its original string representation.

Args:

data (str): The binary string to convert.

Returns:

str: The original string representation of the binary input.

#### to_binINT :

Convert a dictionary or string to a binary integer.

Args:

data_dict (dict, optional): The dictionary to convert. Defaults to an empty dictionary.

data_str (str, optional): The string to convert. Defaults to an empty string.

useString (bool, optional): Flag to indicate if data_str should be used. Defaults to True.

Returns:

int: The binary integer representation of the input data.

#### str_to_bytes :

Convert a string, integer, or dictionary to its byte representation.

Args:

data (typing.Union[str, int, dict]): The data to convert to bytes.

encoding (str, optional): The encoding to use for the conversion. Defaults to "utf-16".

Returns:

bytes: The byte representation of the input data.

#### bytes_to_str :

Convert bytes back to a string using the specified encoding.

Args:

data (bytes): The byte data to convert.

encoding (str, optional): The encoding to use for the conversion. Defaults to "utf-16".

Returns:

str: The string representation of the byte input.

#### api.BIN :

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

**NOTE: [This file is copied from our another program known as AOL(Assembly Orientated Language) and some of its functions are removed to match this Module]**

Returns:

    bin_worker.BIN: The class for working with binary

## ModuleAPI
Module API is a way of interacting with modules.

### Functions
#### CheckModules :
Checks the specified modules. Script Version.

Args:

prompt(bool, optional): This defines shall the script prompt the user for downloading the modules. If it is false it doesn't download modules. Default to False.

mode (str, optional): The mode for checking modules. Default to 'list':

Available Modes are ->

1. 'all' This mode checks for all PheonixApp required Modules.

2. 'list' This mode checks for the specified list.

3. 'module' This mode checks for a specified module.

module (str, optional): The specific module to check. Defaults to 'PheonixAppAPI'.

module_list (list, optional): The list of modules to check. Defaults to ['PheonixAppAPI'].

log (bool, optional): If prompt is active log wil give info about the download. Defaults to False.

Returns:

tuple[list, bool]: The tuple's first part is the uninstalled modules from the provided list [module_list]. The second part is True if the module/all modules from the provided list [module_list]  are installed, else False.

##### Example Usage
    not_installed_modules, success = api.ModuleAPI.CheckModules(False, 'all', log=False)

#### DownloadModules :
Downloads the specified modules. Script Version.

Args:

prompt(bool, optional): This defines shall the script prompt the user for downloading the modules. If it is false it doesn't ask the user for permission to download modules. Default to False.

mode (str, optional): The mode for downloading modules. Default to 'list':

Available Modes are ->

1. 'all' This mode downloads for all PheonixApp required Modules.

2. 'list' This mode downloads for the specified list.

3. 'module' This mode downloads for a specified module.
    

module (str, optional): The specific module to download. To install a specific version add [==] after the name and specify the version after the sign, keep no spaces. Defaults to 'PheonixAppAPI'.

module_list (list, optional): The list of modules to download. To install a specific version add [==] after the name and specify the version after the sign, keep no spaces, do it for all the modules in the list that you want to have a specific version. Defaults to ['PheonixAppAPI'].

log (bool, optional): If set to True this wil give info about the download, otherwise it will not. Defaults to False.

upgraded_module (bool, optional): If set to True it will download the latest version of the module. Defaults to True.

Returns:

tuple[list, bool]: The tuple's first part is the uninstalled modules from the provided list [module_list]. The second part is True if the module/all modules from the provided list [module_list]  are successfully installed, else False.

##### Example Usage
not_successful_modules, success = api.ModuleAPI.DownloadModules(True, 'all', log=True, upgraded_module=True)

## File_Management
### Large_File_Management_System :
A System for managing large amounts of Files.

Args:

path (Union[str, list, pathlib.Path, pathlib.PurePath, pathlib.PurePosixPath, pathlib.PosixPath, pathlib.PureWindowsPath, pathlib.WindowsPath]): The Path/Paths of File/Files/Folder/Folders.

path2 (Union[str, list, pathlib.Path, pathlib.PurePath, pathlib.PurePosixPath, pathlib.PosixPath, pathlib.PureWindowsPath, pathlib.WindowsPath], optional): The second Path/Paths of File/Files/Folder/Folders. Defaults to [].

content (list, optional): The content of File/Files. Defaults to [''].

isFile (bool, optional): If the Paths represent Files/File. Defaults to False.

name (list, optional): The name/names of the Folders/Folder/Files/File. Defaults to [''].

include_name (bool, optional): To be set to False if the name of the Folders are present in the list else True. Defaults to False.

Returns:

Large_File_Management_System

## APIS (Application Programming Interfaces)
### Import
#### Example Usage
    from PheonixAppAPI.apis import *

### ModuleAPI
**CheckModules**
**DownloadModules**

### FileManager
**Large_File_Management_System**


# Support
For any assistance or inquiries, please contact the Pheonix Studios at [pheonix.community.mail@gmail.com] or go to [https://paperexcahange.wixsite.com/pheonixstudios]

To Find tutorials go to AkshobhyaEverything yt channel or PIdevz yt channel or PheonixStudios yt channel.

# Modules Pre-Installed, Published
# PHardwareITK (Pheonix Hardware Interface Toolkit)
## Overview

PHardwareITK, or Pheonix Hardware Interface Toolkit, is a comprehensive Python module developed by Pheonix Studios (AkshuDev/Akshobhya). This toolkit provides a variety of functions and utilities to assist developers in creating complex command-line applications, graphical user interfaces, system utilities, and more. With over 50 distinct functions and multiple specialized toolsets, PHardwareITK is designed to be versatile, modular, and cross-platform, ensuring compatibility with a wide range of development needs.

For examples please visit -> [https://github.com/AkshuDev/PHardwareITK] and navigate to the Tests folder.

## Table of Contents ->
1. Module Overview
2. Key Features
3. Installation
4. Usage
5. Available Toolkits
6. Dependencies
7. Contributing
8. License
9. Module Overview

## Details
    
PHardwareITK serves as a complete suite for developing hardware-related applications, system utilities, and GUI-based tools. It aims to provide developers with powerful, efficient, and easy-to-use resources that handle everything from hardware interactions and system monitoring to building sophisticated user interfaces.

The module includes a set of tools for both novice and experienced developers, including:

1. CLI Toolkit: For creating complex command-line applications.
2. GUI Toolkit: A cross-platform framework for building custom graphical applications.
3. ErrorSystem: A comprehensive error handling system.
4. FileSystem: A set of utilities for interacting with various file formats and performing low-level file operations.
5. HGame: A versatile game development framework that supports multiple rendering engines.

## Key Features

1. Cross-Platform: Works on Linux, Windows, and macOS without modification.
2. Modular Design: Includes a variety of specialized toolkits that can be used independently or together.
3. User-Friendly: Functions are designed to be simple to use, but powerful enough for advanced use cases.
4. Customizable: With features like custom error classes and extendable file system operations, users can adapt the toolkit to their specific needs.
5. Comprehensive Documentation: Detailed explanations and examples of how to use each feature.

## Installation
To install PHardwareITK, follow the steps below:

1. Ensure you are using Python 3.7 or later.
2. Install Using the following command

    pip install phardwareitk

3. Or instead download PheonixAppAPI which includes this module pre-installed inside PheonixAppAPI.Apis.Modules.Pre.phardwareitk
4. Install PheonixAppAPI
   
    pip install PheonixAppAPI

5. Navigate to the downloaded PheonixAppAPI folder/Scripts and run PostInstall.py
6. Your good to go

# Usage
Once the module is installed, you can import it into your Python code. Here are some example use cases:

## Example: Using the CLI Toolkit. (Nano Copy in 100 lines)
# Command Line Interface ToolKit Test

    import sys
    import os
    import time
    import keyboard
    import string
    
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    
    from phardwareitk.CLI import cliToolKit as cli
    from phardwareitk.Extentions import *
    
    global dataBuffer
    dataBuffer:str = ""
    
    def StatusLabel():
        cli.Cursor.MoveCursorToBottom()
        cli.Text.WriteText(" ^X - Exit\t^O - Write Out")
        cli.Cursor.RestoreCursorPosition()
    
    def Start_SuperCLI():
        cli.Screen.ClearScreen()
        cli.Cursor.SetCursorPositionToHome()
        cli.Cursor.SaveCursorPosition()
    
    def WriteOut(data:str):
        cli.Cursor.MoveCursorToBottom()
        cli.Cursor.MoveCursorUp(3)
        cli.Cursor.SetCursorToBeginningOfLine()
        filePath:str = cli.Text.InputText(" File Path: ")
        cli.Screen.ClearCurrentLine()
        cli.Cursor.SetCursorToBeginningOfLine()
        mode:str = cli.Text.InputText(" Mode: ")
        cli.Screen.ClearCurrentLine()
        cli.Cursor.RestoreCursorPosition()
    
        if os.path.exists(filePath):
            cli.Cursor.MoveCursorToBottom()
            cli.Cursor.MoveCursorUp(3)
            cli.Cursor.SetCursorToBeginningOfLine()
            cli.Text.WriteText(" Path Exist!")
            time.sleep(2)
            cli.Screen.ClearCurrentLine()
            cli.Cursor.RestoreCursorPosition()
        else:
            if not mode.lower() in ["binary", "bin", "normal", "utf-8"]:
                cli.Cursor.MoveCursorToBottom()
                cli.Cursor.MoveCursorUp(3)
                cli.Cursor.SetCursorToBeginningOfLine()
                cli.Text.WriteText(" Mode doesn't Exist! Available Modes -> [binary/bin], [normal/utf-8]")
                time.sleep(2)
                cli.Screen.ClearCurrentLine()
                cli.Cursor.RestoreCursorPosition()
            else:
                if mode.lower() == "binary" or mode.lower() == "bin":
                    with open(filePath, "wb") as f:
                        f.write(data.encode())
                        f.close()
                elif mode.lower() == "normal" or mode.lower() == "utf-8":
                    with open(filePath, "w") as f:
                        f.write(data)
                        f.close()
    
        Start_SuperCLI()
        StatusLabel()
    
    def AddData(key:keyboard.KeyboardEvent):
        global dataBuffer
    
        if key.name == "Enter":
            dataBuffer += "\n"
            cli.Text.WriteText("\n")
            cli.Cursor.SaveCursorPosition()
    
        if key.name == "space":
            dataBuffer += " "
            cli.Text.WriteText(" ")
            cli.Cursor.SaveCursorPosition()
    
        if (key.name in string.printable or key.name == "space") and len(key.name) == 1:
            dataBuffer += key.name
            cli.Text.WriteText(key.name)
            cli.Cursor.SaveCursorPosition()
    
    def BackSpace():
        global dataBuffer
        cursor_y, cursor_x = cli.Cursor.CurrentCursorPosition()
    
        if cursor_x > 1:
            dataBuffer = dataBuffer[:-1]
            cli.Text.BackSpaceChar()
    
    def Delete():
        cursor_y, cursor_x = cli.Cursor.CurrentCursorPosition()
    
        if cursor_x <= len(dataBuffer):
            del dataBuffer[cursor_x - 1]
            cli.Text.DeleteChar()
    
    def KeyPress():
        if keyboard.is_pressed("up"):
            cli.Cursor.MoveCursorUp(1)
        elif keyboard.is_pressed("right"):
            cli.Cursor.MoveCursorRight(1)
        elif keyboard.is_pressed("left"):
            cli.Cursor.MoveCursorLeft(1)
        elif keyboard.is_pressed("down"):
            cli.Cursor.MoveCursorDown(1)
        elif keyboard.is_pressed("ctrl+x"):
            cli.Screen.ClearScreen()
            cli.Cursor.SetCursorPositionToHome()
            exit(0)
        elif keyboard.is_pressed("ctrl+o"):
            WriteOut(dataBuffer)
        else:
            key_ = keyboard.read_event()
            if not key_.event_type == keyboard.KEY_UP:
                AddData(key_)
    
    Start_SuperCLI()
    StatusLabel()
    while True:
        KeyPress()

# Available Toolkits ->
1. CLI Toolkit:

The CLI Toolkit provides over 50 distinct functions for creating and managing command-line interfaces (CLI). It enables developers to rapidly build custom CLI applications, similar to nano or other text-based utilities, with minimal lines of code.

Key features:

50+ pre-built functions to handle inputs, outputs, and commands. \
Full control over terminal interactions and interface flow. \
Support for custom command parsing and input handling. \
Text Output/Input with font and colors.

2. GUI Toolkit

The GUI Toolkit is a cross-platform toolkit that allows developers to create complex graphical user interfaces from scratch. It supports multiple UI frameworks including OpenGL, SDL2. The toolkit is fully customizable and provides advanced functionality for creating modern applications.

It is under development and renderGUI.pyx has to be compiled by GCC/Clang and Cython. Instead for the time, use gui_sdl.py (phardwareitk.GUI.gui). The functions inside gui_sdl and renderGUI are supposed to make the process easy, but it is still under development. Hence, you can still use SDL and OpenGL functions to do whatever you want unlike PyQT5 and Tkinter. This toolkit provides all the functions in SDL2 and OpenGL.

Key features:

Full cross-platform support (Linux, Windows, macOS). \
Highly customizable and extensible components. \
Multiple backend support (OpenGL, SDL2).

3. PLTEC

PLTEC (Pheonix Language To Executable Converter) is a separate App that is included with PHardwareITK. You can find the full documentation for PLTEC here -> [https://github.com/AkshuDev/PLTEC].

5. ErrorSystem
   
The ErrorSystem provides a complete error handling framework with over 50 built-in error classes. It also allows users to create custom error classes for more specialized exceptions.

Key features:

A robust set of error classes for different scenarios. \
Custom error class creation for specialized needs. \
Detailed error messages and stack trace support. 

5. System
   
The System folder includes a range of system utilities such as SysUsage, which allows you to monitor and interact with your computer’s hardware and devices.

Key features:

50+ functions to interact with hardware, monitor system performance, and manage processes. \
Real-time usage statistics and logging.

6. Extensions
   
The Extensions folder provides enhanced versions of Python's built-in functions, adding more capabilities. For example, the printH function in the HyperOut.py file allows for advanced text printing with background and foreground colors, fonts, and other enhancements. It also includes custom functions that make hard parts of programming easy like -> progressH that can create a progress bar in the terminal. It is highly flexible.

NOTE: Mostly all terminal tasks even inside the phardwareitk are done using the cliToolKit.py (phardwareitk.CLI.cliToolKit).

NOTE: phardwareitk.Extensions.HyperIn.inputH is a fully custom input function that doesn't use Python's input. Hence, some important factors are to NOTE -

a. It is still Under Enhancements and if any bug occurs please provide a detailed explanation in [https://github/AkshuDev/PHardwareITK/Issues].
b. It requires a time sleep to prevent CPU Hogging, the cpuHogging parameter in the function is defined to be 0.005 seconds or 5 milliseconds, you cannot go under 3 milliseconds or 0.003 seconds, as it is very dangerous for the CPU to do so.

Key features:

Extended versions of basic Python functions. \
Support for custom styling (colors, fonts) in terminal output. \
Enhanced file writing operations. 

7. FileSystem
   
The FileSystem toolkit provides utilities for performing file operations, including working with JSON, assembly, and binary formats. The module includes over 50 functions for tasks ranging from simple file manipulation to complex data transformations.

Key features:

Support for JSON, binary, and assembly file formats. \
High-level functions for file manipulation and data storage.

8. HGame
   
HGame is an alternative to Pygame, providing a more flexible framework for game development. It supports multiple rendering backends, including PHardwareITK.GUI, Tkinter, OpenGL, and SDL2, making it highly cross-platform.

NOTE: Not yet ready for use, just use GUI toolkit for the time.

Key features:

Multiple rendering backends. \
Cross-platform game development support. \
Easy-to-use game object management and event handling.

9. Dependencies.py
    
The Dependencies.py file contains a list of all required libraries and modules for PHardwareITK. This file ensures that any missing dependencies are noted and can be easily installed. NOTE: All requirements are default modules. This files Exisits to install them incase, they are deleted.

11. LIB.py
    
The LIB.py file contains a class called Paths, which provides access to file paths across the entire module. This class is useful for dynamically managing file locations without hardcoding paths.

# Dependencies

PHardwareITK is designed to run with mostly the Python standard library, ensuring compatibility across all systems with minimal need for external dependencies. However, in the case that any of the pre-installed modules are deleted or missing, the Dependencies.py file will help ensure that all necessary libraries are present.

Required Dependencies ->

1. PySDL2 (pip install pysdl2)
2. PySDL2-DLL (pip install pysdl2-dll)
3. PyOpenGL (pip install PyOpenGL)

NOTE: All these are for the gui toolkit.

# Contributing

We welcome contributions from the community! If you have ideas for new features, bug fixes, or improvements, please follow the steps below:

# Fork the repository.

Create a new branch (git checkout -b feature-branch).\
Make your changes. \
Commit your changes (git commit -m 'Add new feature'). \
Push to your branch (git push origin feature-branch). \
Open a pull request with a description of your changes. 

# License

PHardwareITK is licensed under the MIT License. Feel free to use, modify, and distribute the software under the terms of this license.

# For more information, refer to the official documentation or reach out to us through the repository issues page.
