API Reference
=============

Welcome to the API Reference for PheonixAppAPI. This document covers the classes, methods, and functionalities available in the API. The PheonixAppAPI provides a set of tools to interact with the Pheonix application and its modules.

Modules Overview
----------------

- **main.PheonixAppAPI**: The core class for initializing and interacting with the application.
- **api.GUI**: Manages the graphical user interface (GUI) for PheonixApp.
- **api.MiniGames**: Contains mini-games like Guess The Number.
- **api.PATF_API**: Handles operations related to the Pheonix App Terminal File (PATF).
- **api.Utilities**: Provides utility functions like Calculator and Wikipedia search.
- **api.BIN**: Tools for working with binary data and file manipulation.
- **api.ModuleAPI**: Handles module management, including installation and checking.
- **api.FileManager**: Provides tools for managing file systems and large file operations.
- **apis.Cipher...**: Cipher File, Provides Encryption and Decryption.
- **apis.PACI...**: PACI File, Provides Downloading/Uploading, etc.
- **apis.Modules.Pre.PheonixExceptions...**: Provides Exceptions, (Simple File).
- **apis.Modules.Pre.PheonixJson...**: Provides Json, (Simple File).
- **apis.Modules.Pre.PheonixCipherTools...**: Provides Cipher Tools, (Simple File).
- **apis.Modules.Pre.phardwareitk...**: Provides Hardware Related Program, (Very Complex Folder), (Published Pheonix Module).

Classes
-------

### main.PheonixAppAPI

This class is the entry point for initializing and controlling the app.

#### Methods

- **initialize()**
  - Initializes the application and prepares it for use.
  - **Returns**: `None`
  - **Example**:
    ```python
    main_ = main.PheonixAppAPI(False).initialize()
    ```

- **set_parent(parent)**
  - Sets the parent instance for the application.
  - **Returns**: `None`
  - **Example**:
    ```python
    set_parent(main_)
    ```

### api.GUI

Manages the GUI of the Pheonix app, allowing the user to interact with the application via a graphical interface.

#### Methods

- **start()**
  - Starts the graphical user interface.
  - **Returns**: `None`
  - **Example**:
    ```python
    gui = api.GUI()
    gui.start()
    ```

### api.MiniGames

Contains methods for running mini-games within the Pheonix app.

#### Methods

- **GuessTheNumber()**
  - Starts the "Guess The Number" game.
  - **Returns**: `None`
  - **Example**:
    ```python
    games = api.MiniGames
    games.GuessTheNumber()
    ```

### api.PATF_API

Handles operations related to the **Pheonix App Terminal File** (PATF). This file is essential for certain functionalities within the app.

#### Methods

- **run(command)**
  - Executes a given command on the PATF file.
  - **Arguments**: `command` (str) – The command to execute.
  - **Returns**: `None`
  - **Example**:
    ```python
    patf_api = api.PATF_API()
    patf_api.run("terminal --createfile")
    ```

### api.Utilities

This class provides various utility functions, such as starting a calculator or performing a Wikipedia search.

#### Methods

- **Calc_Terminal()**
  - Starts a terminal-based calculator.
  - **Returns**: `None`
  - **Example**:
    ```python
    utils = api.Utilities()
    utils.Calc_Terminal()
    ```

- **Wiki_Terminal()**
  - Starts a terminal-based Wikipedia search.
  - **Returns**: `None`
  - **Example**:
    ```python
    utils.Wiki_Terminal()
    ```

### api.BIN

This class contains methods for working with binary data, including converting strings to binary, encoding/decoding data, and managing binary files.

#### Methods

- **str_to_bin(data)**
  - Converts a string or other data type into a binary string.
  - **Arguments**: `data` (str) – The data to convert.
  - **Returns**: `str` – The binary representation of the input data.
  - **Example**:
    ```python
    bin = api.BIN(path="test.bin", content="Hello")
    print(bin.str_to_bin("Hello world"))
    ```

- **bin_to_str(data)**
  - Converts binary data back into a string.
  - **Arguments**: `data` (str) – The binary data to convert.
  - **Returns**: `str` – The decoded string.
  - **Example**:
    ```python
    bin = api.BIN(path="test.bin", content="Hello")
    print(bin.bin_to_str(bin.str_to_bin("Hello world")))
    ```

### api.ModuleAPI

Manages modules and their installation.

#### Methods

- **CheckModules()**
  - Checks if the specified modules are installed.
  - **Arguments**:
    - `mode` (str): The mode of checking. Can be 'all', 'list', or 'module'.
    - `module_list` (list, optional): A list of modules to check.
    - `log` (bool, optional): Whether to log the process.
  - **Returns**: `tuple[list, bool]` – A tuple containing a list of uninstalled modules and a success status.
  - **Example**:
    ```python
    not_installed_modules, success = api.ModuleAPI.CheckModules(False, 'all', log=False)
    ```

- **DownloadModules()**
  - Downloads the specified modules.
  - **Arguments**:
    - `mode` (str): The mode for downloading.
    - `module_list` (list, optional): A list of modules to download.
    - `log` (bool, optional): Whether to log the download process.
  - **Returns**: `tuple[list, bool]` – A tuple containing a list of uninstalled modules and a success status.
  - **Example**:
    ```python
    not_successful_modules, success = api.ModuleAPI.DownloadModules(True, 'all', log=True)
    ```

### api.FileManager

Manages file operations, particularly for handling large files and directories.

#### Methods

- **Large_File_Management_System()**
  - A system for managing a large amount of files.
  - **Arguments**:
    - `path` (str or list): Path to the file(s) or folder(s).
    - `path2` (str or list, optional): Additional path(s).
  - **Returns**: `Large_File_Management_System` – An instance of the file management system.
  - **Example**:
    ```python
    file_manager = api.FileManager.Large_File_Management_System(path="path/to/files")
    ```

## Apis
PheonixAppAPI.apis, is a folder full of Api files, and more.

### apis.Cipher
This file provides Encryption and Decryption Related Methods.

### Classes: 
#### _AES_
This class uses PyCryptodome for providing with tested security encryptions. This class uses AES (Advanced Encryption Standard).

#### Methods: 
 - **Encrypt()**
 - Encrypt the provided data.
 - **Arguments**:
    - `data` (Union[ByteString, bytes, bytearray]): The data for encryption.
    - `key` (Union[ByteString, bytearray, bytes]): The key that will be used for encryption.
    - `mode` (Any, optional): This defines the mode used for encrypting data. It should be set only using either the _AES_.modes.(mode) or AES.(mode). Defaults to AES.MODE_CBC
 - **Returns**:
    - `Any`: The encrypted data.

 - **Decrypt()**
 - Decrypt the encrypted data
 - **Arguments**:
    - `data` (Union[str, int]): The data for decryption.
    - `key` (Union[ByteString, bytearray, bytes]): The key that was used for encryption.
    - `mode` (Any, optional): This defines the mode that used for encrypting data. It should be set only using either the _AES_MODES.(mode) or AES.(mode). Defaults to AES.MODE_CBC
 - **Returns**:
    - `str`: The decrypted data.

#### _AES_MODES:
This class provides all the AES modes that can be passes to the **_AES_** class.

#### PTDMEDMU:
(Pheonix Three Dimentional Mathematical Encryption / Decryption Method User) is a very very complex Encryption and Decryption Clas.

#### Methods:
 - **Encrypt()**

Examples
--------

Here are some example scripts that demonstrate how to use various components of the PheonixAppAPI.

### Example 1: Starting the GUI

  from PheonixAppAPI import main, api
  
  # Initialize and start the GUI
  main_ = main.PheonixAppAPI(False).initialize()
  set_parent(main_)
  
  gui = api.GUI()
  gui.start()

### Example 2:  Playing a Mini-Game
  from PheonixAppAPI import api
  
  # Start the "Guess The Number" mini-game
  games = api.MiniGames
  games.GuessTheNumber()

### Example 3: Running a PATF command
  from PheonixAppAPI import api

  # Run a PATF command
  patf_api = api.PATF_API()
  patf_api.run("terminal --createfile")

### Conclusion
This concludes the API reference for PheonixAppAPI. For further assistance, please consult the documentation or contact Pheonix Studios support.

For any questions or issues, reach out to us at pheonix.community.mail@gmail.com.

---

### Explanation:

- **Classes**: Describes the core classes in `PheonixAppAPI` such as `main.PheonixAppAPI`, `api.GUI`, `api.MiniGames`, etc.
- **Methods**: Each class has associated methods that are detailed in terms of their arguments and return types.
- **Examples**: A few examples of how to use these classes and methods to interact with the application.

This example covers a 200-line format by outlining key components and functions across various classes. You can extend this file further by adding additional methods, attributes, and examples, as necessary, based on the actual contents of the GitHub repository.

If you need more specific functions or details from the repository, you would need to explore the code directly and incorporate that information into this structure.
