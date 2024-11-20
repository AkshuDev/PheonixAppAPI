API Reference
=============

Welcome to the API Reference for **PheonixAppAPI**. This document covers the classes, methods, and functionalities available in the API. The **PheonixAppAPI** provides a robust set of tools to interact with the Pheonix application and its modules.

.. contents:: Table of Contents
   :local:
   :depth: 2

Modules Overview
----------------

The API is organized into the following modules:

- **main.PheonixAppAPI**: Core functionality for initializing and interacting with the application.
- **api.GUI**: Manages the graphical user interface (GUI).
- **api.MiniGames**: Provides mini-games like "Guess The Number."
- **api.PATF_API**: Operations related to Pheonix App Terminal File (PATF).
- **api.Utilities**: Utility functions like calculator and Wikipedia search.
- **api.BIN**: Tools for binary data manipulation.
- **api.ModuleAPI**: Handles module management.
- **api.FileManager**: File system and large file management.
- **apis.Cipher**: Encryption and decryption utilities.
- **apis.PACI**: Downloading and uploading management.
- **apis.Modules.Pre**: Predefined modules like `PheonixExceptions`, `PheonixJson`, `PheonixCipherTools`, and more.

Classes and Methods
-------------------

### main.PheonixAppAPI

**Description**: The entry point for initializing and managing the application.

**Methods**:

- **initialize()**  
  Initializes the application.  

  **Returns**:  
  - `None`

  **Example**:

  .. code-block:: python

     main_ = main.PheonixAppAPI(False).initialize()

- **set_parent(parent)**  
  Sets the parent instance for the application.  

  **Returns**:  
  - `None`

  **Example**:

  .. code-block:: python

     set_parent(main_)

### api.GUI

**Description**: Handles the graphical user interface (GUI) of the application.

**Methods**:

- **start()**  
  Launches the graphical interface.  

  **Returns**:  
  - `None`

  **Example**:

  .. code-block:: python

     gui = api.GUI()
     gui.start()

### api.MiniGames

**Description**: Contains methods to run mini-games.

**Methods**:

- **GuessTheNumber()**  
  Launches the "Guess The Number" game.  

  **Returns**:  
  - `None`

  **Example**:

  .. code-block:: python

     games = api.MiniGames()
     games.GuessTheNumber()

### api.PATF_API

**Description**: Provides operations for working with the Pheonix App Terminal File (PATF).

**Methods**:

- **run(command)**  
  Executes commands in the PATF context.  

  **Arguments**:  
  - `command` (str): Command to execute.

  **Returns**:  
  - `None`

  **Example**:

  .. code-block:: python

     patf_api = api.PATF_API()
     patf_api.run("terminal --createfile")

### api.Utilities

**Description**: Utility functions like a calculator and Wikipedia search.

**Methods**:

- **Calc_Terminal()**  
  Launches a terminal-based calculator.  

  **Returns**:  
  - `None`

  **Example**:

  .. code-block:: python

     utils = api.Utilities()
     utils.Calc_Terminal()

- **Wiki_Terminal()**  
  Launches a terminal-based Wikipedia search.  

  **Returns**:  
  - `None`

  **Example**:

  .. code-block:: python

     utils.Wiki_Terminal()

### api.BIN

**Description**: Tools for binary data operations.

**Methods**:

- **str_to_bin(data)**  
  Converts a string to a binary string.  

  **Arguments**:  
  - `data` (str): Data to convert.

  **Returns**:  
  - `str`: Binary representation.

  **Example**:

  .. code-block:: python

     bin = api.BIN(path="test.bin", content="Hello")
     print(bin.str_to_bin("Hello world"))

- **bin_to_str(data)**  
  Converts binary data back into a string.  

  **Arguments**:  
  - `data` (str): Binary data to convert.

  **Returns**:  
  - `str`: Decoded string.

  **Example**:

  .. code-block:: python

     bin = api.BIN(path="test.bin", content="Hello")
     print(bin.bin_to_str(bin.str_to_bin("Hello world")))

### api.ModuleAPI

**Description**: Handles module checking and installation.

**Methods**:

- **CheckModules(mode, module_list=None, log=False)**  
  Checks if modules are installed.  

  **Arguments**:  
  - `mode` (str): Check mode ('all', 'list', or 'module').  
  - `module_list` (list, optional): List of modules to check.  
  - `log` (bool, optional): Whether to log the process.

  **Returns**:  
  - `tuple[list, bool]`: Uninstalled modules and success status.

  **Example**:

  .. code-block:: python

     not_installed_modules, success = api.ModuleAPI.CheckModules('all', log=False)

- **DownloadModules(mode, module_list=None, log=False)**  
  Downloads specified modules.  

  **Arguments**:  
  - `mode` (str): Download mode.  
  - `module_list` (list, optional): List of modules to download.  
  - `log` (bool, optional): Whether to log the process.

  **Returns**:  
  - `tuple[list, bool]`: Uninstalled modules and success status.

  **Example**:

  .. code-block:: python

     not_successful_modules, success = api.ModuleAPI.DownloadModules('all', log=True)

### api.FileManager

**Description**: Provides tools for managing large files and directories.

**Methods**:

- **Large_File_Management_System(path, path2=None)**  
  Manages large file operations.  

  **Arguments**:  
  - `path` (str or list): Path to file(s) or folder(s).  
  - `path2` (str or list, optional): Additional paths.

  **Returns**:  
  - `Large_File_Management_System`: Instance of the file management system.

  **Example**:

  .. code-block:: python

     file_manager = api.FileManager.Large_File_Management_System(path="path/to/files")

APIs
----

The `PheonixAppAPI.apis` folder contains additional utility files.

### Apis files

**Description**: The files included in the (apis) folder.

#### apis.Cipher

This module provides various encryption and decryption methods for different use cases. It offers functionalities for:

- **Three-dimensional matrix encryption (`PTDMEDMU`)**
- **Large prime number-based encryption (`PMEDMU`)**
- **Two-step encryption using machine identifiers (`PTSEDM`)**
- **Secure encryption using the Advanced Encryption Standard (AES) with PyCryptodome (`_AES_`)**

**Classes:**

**1. PTDMEDMU**

* **Purpose:** This class implements the "Pheonix Three Dimensional Matrix Encrypt/Decrypt Method User" (PTDMEDMU) for data encryption. It encrypts each character four times, placing it on one of the cells from one of six grids.
* **Note:** This method is claimed to be "hard to crack," but the specific security implications are not documented.
* **Available Bytes:** The class accepts data from 1 to 900 bytes for encryption.

**Methods:**

* **__init__(self) -> None:** Initializes the class.
* **new(key:Union[str, int, bytes], use_sys_info:bool=False, value:Union[str, bytes, int]="") -> tuple[str, str]:**
    * **Arguments:**
        * `key`: The key for encryption (string, integer, or bytes).
        * `use_sys_info` (optional, defaults to False): Whether to set/append the key with system information for computer-specific decryption.
        * `value` (optional, defaults to ""): The data to encrypt (string, bytes, or integer).
    * **Returns:** A tuple containing the modified key and the encrypted value.
    * **Description:** This function prepares the key and encrypts the provided value using the PTDMEDMU method.

**Hidden Code (Implementation Details):**

The implementation details of the PTDMEDMU methods (`adjust_ascii`, `process_ascii`, and `encrypt`) are hidden using `.....` placeholders due to potential security concerns and the lack of clear explanations in the code.

Please do not use the (`adjust_ascii`, `process_ascii`) functions directly, and use the `encrypt` function instead.

The `encrypt` function encrypts the provided data and can be potiential security concern, if it is used to create malware, etc.

**2. PMEDMU**

* **Purpose:** This class implements the "Pheonix Mathematical Encrypt/Decrypt Method User" (PMEDMU) for data encryption. It uses large prime numbers for encryption and decryption, typically leveraging a computer's MAC address as a key.
* **Note:** While large prime numbers can offer strong encryption, the implementation might benefit from a more robust key generation approach.

**Methods:**

* **__init__(self) -> None:** Initializes the class.
* **generate_large_prime(self, bits:int) -> int:**
    * **Argument:** `bits`: The bit size for the generated prime number.
    * **Returns:** A large prime number with the specified bit size.
    * **Description:** Generates a random large prime number for encryption.
* **new(self, bits:int) -> int:**
    * **Argument:** `bits`: The bit size for the generated prime numbers.
    * **Returns:** A tuple containing two large prime numbers for encryption and decryption.
    * **Description:** Generates a pair of large prime numbers for the PMEDMU method.
* **encrypt(self, message: Union[str, int, bytes], p: int, q: int) -> bytes:**
    * **Arguments:**
        * `message`: The data to encrypt (string, integer, or bytes).
        * `p`: The first large prime number for encryption.
        * `q`: The second large prime number for encryption.
    * **Returns:** Encrypted data as bytes (encoded in UTF-16).
    * **Raises:** `ValueError` if the message is too large for the given primes.
    * **Description:** Encrypts the message using the PMEDMU method with the provided primes.
* **decrypt(self, encrypted_bytes: bytes, p: int, q: int) -> str:**
    * **Arguments:**
        * `encrypted_bytes`: Encrypted data as bytes (encoded in UTF-16).
        * `p`: The first large prime number used for encryption.
        * `q`: The second large prime number used for encryption.
    * **Returns:** Decrypted data as a string.
    * **Raises:** `Exception` if the message cannot be decoded using the specified primes.
    * **Description:** Decrypts encrypted data using the PMEDMU method with the provided primes.

**3. PTSEDM**

* **Purpose:** This class implements the "Pheonix Two-Step Encrypt/Decrypt Method" (PTSEDM) for data encryption. It leverages a machine-specific identifier, often derived from the MAC address, for encryption and decryption.
* **Note:** While the use of a machine-specific identifier adds a layer of security, it's important to ensure the security of the identifier itself.

**Methods:**

* **__init__(self) -> None:** Initializes the class.
* **get_machine_identifier(self, key=str(nextprime(256)), data="") -> bytes:**
    * **Arguments:**
        * `key` (optional, defaults to `str(nextprime(256))`): The key used for generating the identifier.
        * `data` (optional, defaults to ""): Additional data to incorporate into the identifier.
    * **Returns:** A unique machine identifier as bytes.
    * **Description:** Generates a unique machine identifier based on system information and the provided key and data.
* **encrypt(self, data: Union[str, int, bytes], flag:str="", key=str(nextprime(256))) -> Union[str, bytes]:**
    * **Arguments:**
        * `data`: The data to encrypt (string, integer, or bytes).
        * `flag` (optional, defaults to ""): A flag to indicate decryption mode.
        * `key` (optional, defaults to `str(nextprime(256))`): The key used for encryption.
    * **Returns:** Encrypted data as bytes or a string (in decryption mode).
    * **Description:** Encrypts data using the PTSEDM method and the machine-specific identifier.
* **decrypt(self, encrypted_data: bytes, key:str=str(nextprime(256))) -> str:**
    * **Arguments:**
        * `encrypted_data`: The encrypted data to decrypt.
        * `key` (optional, defaults to `str(nextprime(256))`): The key used for decryption.
    * **Returns:** Decrypted data as a string.
    * **Raises:** `Exception` if the data cannot be decrypted.
    * **Description:** Decrypts data using the PTSEDM method and the machine-specific identifier.

**4. _AES_**

* **Purpose:** This class provides AES encryption and decryption functionalities using the PyCryptodome library.
* **Note:** PyCryptodome is a well-established library for cryptographic operations, providing strong security guarantees.

**Methods:**

* **__init_(self) -> None:** Initializes the class.
* **Encrypt(self, data:Union[ByteString, bytes, bytearray], key:Union[ByteString, bytearray, bytes], mode=AES.MODE_CBC):**
    * **Arguments:**
        * `data`: The data to encrypt (bytes or bytearray).
        * `key`: The encryption key (bytes or bytearray).
        * `mode` (optional, defaults to `AES.MODE_CBC`): The AES mode of operation.
    * **Returns:** Encrypted data.
    * **Description:** Encrypts data using the specified AES mode and key.
* **Decrypt(self, data, key:Union[ByteString, bytearray, bytes], mode=AES.MODE_CBC) -> str:**
    * **Arguments:**
        * `data`: The encrypted data.
        * `key`: The encryption key used to encrypt the data.
        * `mode` (optional, defaults to `AES.MODE_CBC`): The AES mode of operation used for encryption.
    * **Returns:** Decrypted data as a string.
    * **Description:** Decrypts data using the specified AES mode and key.

**_AES_MODES**

This class provides constants for various AES modes of operation:

* `MODE_CBC`
* `MODE_CCM`
* `MODE_CFB`
* `MODE_CTR`
* `MODE_EAX`
* `MODE_ECB`
* `MODE_GCM`
* `MODE_OCB`
* `MODE_OPENPGP`
* `MODE_SIV`
* `MODE_OFB`

#### apis.PACI

**Description:**

The `apis.PACI` module provides a robust API for managing and installing Pheonix App modules. It offers functionalities for:

- Reading module access files
- Returning module paths
- Creating access files for modules
- Installing Pheonix modules using `pip`

**Methods:**

* **ReadAccessFile(moduleName:str) -> dict:**
    Reads the access file of a specified module and returns its contents as a dictionary.

    **Example:**

    .. code-block:: python

       access_data = PACI.ReadAccessFile("my_module")
       print(access_data)

* **ReturnModulePath(module_name:str) -> str:**
    Returns the path to a module based on its access file information.

    **Example:**

    .. code-block:: python

       module_path = PACI.ReturnModulePath("my_module")
       print(module_path)

* **MakeAccessFile(module_name:str, module_version:str="latest") -> None:**
    Creates an access file for a specified module, defining its path and version information.

    **Example:**

    .. code-block:: python

       PACI.MakeAccessFile("my_module", "1.0.0")

* **InstallPheonixModule(module_name:str, module_version:str="latest", log:bool=False) -> None:**
    Installs a Pheonix module using `pip`, handling potential errors and logging the process if specified.

    **Example:**

    .. code-block:: python

       PACI.InstallPheonixModule("pcd_py", "latest", log=True)

**Note:** The module leverages the `PheonixJson` and `PheonixExceptions` modules for JSON handling and error management, respectively.

---
