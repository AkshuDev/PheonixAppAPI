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

# Example Usage

from PheonixAppAPI import (api, main)


Then do main.PheonixAppAPI.initialize(). Here is the arguments it takes -> main.PheonixAppAPI(LoginOrSignup:bool=False, email:str="", username:str="", password:str="")

LoginOrSignup: Set to True if you want to sign up and use the application, otherwise set to False.
email: Your email address. Leave blank if not logging in or signing up.
username: Your username. Leave blank if not logging in or signing up.
password: Your password. Leave blank if not logging in or signing up.

# Example Usage

parent_ = main.PheonixAppAPI(False).initialize()

Now, you need to set the parent in the api file.

# Example Usage

api.set_parent(parent_)


API Usage
Initialization
To start using the API, create an instance of the PATF_API class from api.py:

PATF_API = api.PATF_API(True)


Checking Modules
You can check for the existence of certain modules using the CheckModules method:

# Example Usage

PATF_API = api.PATF_API(True)
PATF_API.CheckModules("list", ["PyQt5", "PheonixAppAPI"])


GUI Mode
To start the GUI mode, use the GUI class:

# Example Usage

gui = api.GUI()
gui.start()
Mini-Games
PheonixAppAPI includes a variety of mini-games. Use the MiniGames class to access them:

# Example Usage

games = MiniGames()
games.GuessTheNumber()


PATF Commands
Creating a PATF File
Use the PATF_API class to manage PATF files and perform related tasks. To create a PATF file, use the following command:

# Example Usage

patf_api = PATF_API()
patf_api.run("terminal --createfile")


Checking Modules
Check the status of modules with the CheckModules method:

# Example Usage

patf_api = PATF_API()
patf_api.CheckModules(mode="all", list=["module1", "module2"])


Getting Certificate Path
Retrieve the certificate path using the getCertificatePath method. Note that the code argument is an internally used argument and requires specific knowledge to user:

# Example Usage

patf_api = PATF_API()
path = patf_api.getCertificatePath(code="12345", flag="+BOOL")
print(path)



Support
For any assistance or inquiries, please contact the Pheonix Studios at [pheonix.community.mail@gmail.com]