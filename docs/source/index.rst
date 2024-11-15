Welcome to Pheonix App 1.0's documentation!
==========================================

Pheonix App 1.0 is a versatile Python application designed to streamline various tasks, from managing files to playing mini-games. This documentation provides comprehensive instructions on how to use the app effectively.

Contents:
---------

   Introduction

   Installation

   Usage

   Api_reference

   Examples

   Support

Installation
------------

To install Pheonix App 1.0, you can either use the Python Package Index (PIP) or the Phoenix App Community Installer (PACI). Follow the instructions below:

1. **Install via pip**:
   Run the following command in your terminal to install the required modules:

     pip install PheonixappAPI


2. **Install via Website**:
  Go to [https://pheonixntx.wixsite.com/paos]

  Go to the downloads Page

  Click on PheonixApp1.0

  Unzip the folder

  Enjoy!!!

Usage
-----
Pheonix App 1.0 supports two modes: GUI Mode and Terminal Mode.

1. Starting the App
To start the app, open the PheonixStudiosStarter.py script and run it in your terminal.

  python PheonixStudiosStarter.py

Upon execution, the terminal will prompt you with a command line interface (CLI).

2. Switching to GUI Mode
To switch to the graphical user interface (GUI) mode, run the following command in terminal:

  gui start

3. Terminal Mode
If you prefer working in the terminal, the app will display a prompt like:

  C:/Users/main/mydir/pheonixapp1.0/files ->

4. Mini-Games
To play a mini-game, use the following command format:

  fun !minigame [minigame_name]

Replace [minigame_name] with the name of the game you want to play (e.g., "GuessTheNumber").

5. Devtools and Release Mode
Enable or disable devtools and release mode with the following commands:

  terminal !devtools:ENABLE
  terminal !devtools:DISABLE
  terminal !devtools:CLcmds:T:release

6. Working with PATF Files
To manage PATF (Pheonix App Terminal File), use these commands:

a. Create a PATF file:

  terminal --createfile

b. Modify or delete a PATF file:

  terminal --modifyfile
  terminal --deletefile

7. Utilities
a. Calculator: Start a terminal-based calculator:

  terminal !utilities:calc

b. Wikipedia Search: Perform a Wikipedia search:

  terminal !utilities:wiki

8. API Reference
The Pheonix App 1.0 API provides several classes and functions for interacting with the app's features.

a. Importing and Initializing the API
To use the API, first import the necessary files:

  from PheonixAppAPI import main, api

Then initialize the application:

  main_ = main.PheonixAppAPI(False).initialize()
  set_parent(main_)

b. GUI Mode
To start the GUI mode:

  gui = api.GUI()
  gui.start()

c. Mini-Games
To play a mini-game like Guess The Number:

  games = api.MiniGames
  games.GuessTheNumber()

d. PATF Commands
Manage the PATF file with PATF_API class:

patf_api = api.PATF_API()
patf_api.run("terminal --createfile")

Utilities
Calculator:

utils = api.Utilities()
utils.Calc_Terminal()

Wikipedia Search:

utils.Wiki_Terminal()

For a complete API reference, please see the full list of available functions in the API documentation.

Support
For assistance, please contact Pheonix Studios at:

Email: pheonix.community.mail@gmail.com
Official website: Pheonix Studios
You can also find tutorials on the following YouTube channels:

AkshobhyaEverything
PIdevz
PheonixStudios
