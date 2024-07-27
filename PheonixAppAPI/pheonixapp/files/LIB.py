#    _____              .___       __________            _____   __           .__          ___.   .__
#   /     \ _____     __| _/____   \______   \___.__.   /  _  \ |  | __  _____|  |__   ____\_ |__ |  |__ ___.__._____
#  /  \ /  \\__  \   / __ |/ __ \   |    |  _<   |  |  /  /_\  \|  |/ / /  ___/  |  \ /  _ \| __ \|  |  <   |  |\__  \
# /    Y    \/ __ \_/ /_/ \  ___/   |    |   \\___  | /    |    \    <  \___ \|   Y  (  <_> ) \_\ \   Y  \___  | / __ \_
# \____|__  (____  /\____ |\___  >  |______  // ____| \____|__  /__|_ \/____  >___|  /\____/|___  /___|  / ____|(____  /
#         \/     \/      \/    \/          \/ \/              \/     \/     \/     \/           \/     \/\/          \/
#     ___ ___________                      .___             ___
#    /  / \_   _____/___  __ __  ____    __| _/___________  \  \
#   /  /   |    __)/  _ \|  |  \/    \  / __ |/ __ \_  __ \  \  \
#  (  (    |     \(  <_> )  |  /   |  \/ /_/ \  ___/|  | \/   )  )
#   \  \   \___  / \____/|____/|___|  /\____ |\___  >__|     /  /
#    \__\      \/                   \/      \/    \/        /__/






# __________.__                        .__           _________ __            .___.__
# \______   \  |__   ____  ____   ____ |__|__  ___  /   _____//  |_ __ __  __| _/|__| ____  ______
#  |     ___/  |  \_/ __ \/  _ \ /    \|  \  \/  /  \_____  \\   __\  |  \/ __ | |  |/  _ \/  ___/
#  |    |   |   Y  \  ___(  <_> )   |  \  |>    <   /        \|  | |  |  / /_/ | |  (  <_> )___ \
#  |____|   |___|  /\___  >____/|___|  /__/__/\_ \ /_______  /|__| |____/\____ | |__|\____/____  >
#                \/     \/           \/         \/         \/                 \/               \/

class PSH:
    PSntx_H1 = {
        "a": "e",
        "b": "@",
        "c": "%",
        "d": "!",
        "e": "&",
        "f": "b",
        "g": "/",
        "h": "g",
        "i": "d",
        "j": "^",
        "k": "1",
        "l": "6",
        "m": "7",
        "n": "~",
        "o": ")",
        "p": "9",
        "q": "(",
        "r": "*",
        "s": "`",
        "t": "V",
        "u": "P",
        "v": "E",
        "w": "'",
        "x": "<",
        "y": ">",
        "z": ","
    }

    pheonix_utx = {
            'a': '!',
            'b': '#',
            'c': '%',
            'd': '&',
            'e': '(',
            'f': '@',
            'g': '$',
            'h': '^',
            'i': '*',
            'j': ')',
            'k': '-',
            'l': '=',
            'm': '_',
            'n': '+',
            'o': '{',
            'p': ']',
            'q': '[',
            'r': '}',
            's': '|',
            't': ':',
            'u': '"',
            'v': ';',
            'w': "'",
            'x': '<',
            'y': '.',
            'z': ',',
            '1': 'D',
            '2': 'J',
            '3': 'G',
            '4': 'P',
            '5': 'A',
            '6': 'b',
            '7': 'B',
            '8': 'F',
            '9': 'X',
            '0': 'Z',
            '.': '/',
            ',': '?',
            '?': '1',
            '|': '2',
            ':': '3',
            ';': '4',
            '/': '5',
            '"': '6',
            "'": '7',
            '<': '8',
            '>': '9',
            '&': '0',
            ' ': '~',
            '@': '`'
    }

    hype_space = {
    "A": "+", "B": "-", "C": "@", "D": "*", "E": "(", "F": ")", "G": "'", "H": '"', "I": "/", "J": "\\", "K": ".", "L": ",", "M": "~",
    "N": "4", "O": "3", "P": "2", "Q": "1", "R": "0", "S": "9", "T": "8", "U": "7", "V": "6", "W": "5", "X": "^", "Y": "A", "Z": "B",
    "a": "C", "b": "D", "c": "E", "d": "K", "e": "J", "f": "L", "g": "N", "h": "I", "i": "Q", "j": "S", "k": "R", "l": "U", "m": "T",
    "n": "Y", "o": "X", "p": "W", "q": "V", "r": "Z", "s": "F", "t": "G", "u": "H", "v": "M", "w": "O", "x": "P", "y": "a", "z": "b",
    "+": "c", "-": "d", "@": "e", "*": "f", "(": "g", ")": "h", "'": "i", '"': "j", "/": "k", "\\": "l", ".": "m", ",": "n", "&": "`",
    "#": "$", "$": "&", "%": "!", "!": "%", "{": "}", "}": "{", ":": ";", ";": ":", "<": "?", "?": "<", ">": " ", "[": "]", "]": "[",
    "|": "#", " ": "o", "1": "p", "2": "q", "3": "r", "4": "s", "5": "t", "6": "u", "7": "v", "8": "w", "9": "x", "0": "y", "~": "z",
    "`": "_", "_": "=", "=": "|"
    }

    hype_space_bin = {
    "A": "+", "B": "-", "C": "@", "D": "*", "E": "(", "F": ")", "G": "'", "H": '"', "I": "/", "J": "\\", "K": ".", "L": ",", "M": "~",
    "N": "4", "O": "3", "P": "2", "Q": "1", "R": "0", "S": "9", "T": "8", "U": "7", "V": "6", "W": "5", "X": "^", "Y": "A", "Z": "B",
    "a": "C", "b": "D", "c": "E", "d": "K", "e": "J", "f": "L", "g": "N", "h": "I", "i": "Q", "j": "S", "k": "R", "l": "U", "m": "T",
    "n": "Y", "o": "X", "p": "W", "q": "V", "r": "Z", "s": "F", "t": "G", "u": "H", "v": "M", "w": "O", "x": "P", "y": "a", "z": "b",
    "+": "c", "-": "d", "@": "e", "*": "f", "(": "g", ")": "h", "'": "i", '"': "j", "/": "k", "\\": "l", ".": "m", ",": "n", "&": "`",
    "#": "$", "$": "&", "%": "!", "!": "%", "{": "}", "}": "{", ":": ";", ";": ":", "<": "?", "?": "<", ">": " ", "[": "]", "]": "[",
    "|": "#", " ": "o", "1": "p", "2": "q", "3": "r", "4": "s", "5": "t", "6": "u", "7": "v", "8": "w", "9": "x", "0": "y", "~": "z",
    "`": "_", "_": "=", "=": "|"
    }

    hype_space_bin = {k: format(ord(v), '08b') for k, v in hype_space_bin.items()}

    pheonix_utx_DESC = "Lower alphabets, numbers and some symbols allowed."

    PSntx_H1_DESC = "Only lower alphabets are allowed."

    hype_space_DESC = "Every Character except [^] are allowed."

    hype_space_bin_DESC = f"Hype_Space [{hype_space_DESC}] but in binary."

class PSS:
    #For PATF commands
    atribbs = ["--createfile", "--modifyfile", "--deletefile", "--upgradefile", "--changefiletype", "!clear", "!color:default", "!devtools", "!utilities:calc", "!utilities:wiki", "!certificate:S:path"]
    devtools = ["ENABLE", "DISABLE", "CMDS", "CLcmds"]
    devtools_3S = ["CMDS", "CLcmds"]

    cmds_devtool = ["ALL", "ENABLE", "DISABLE", "CMDS", "CLcmds"]
    clcmdsT = ["release"]
    attribs_cft = ["patf", "txt", "ini"]

    #For Non PATF commands
    Tcmds = ["!time", "!fact", "!quote", "!remind", "!decodefile", "!encodefile"]

    modules = ["os", "shutil", "time", "pathlib", "datetime", "pickle", "importlib", "configparser", "binascii", "random", "subprocess",
               "xlsxwriter", "requests", "json", "http", "socket", "PyQt5", "qdarkstyle", "ctypes", "validate_email", "opencv-python",
               "pyttsx3", "speech_recognition", "zlib"]

    nonDEF_modules = [
        "PyQt5",
        "wikipedia",
        "xlsxwriter",
        "requests",
        "qdarkstyle",
        "validate_email",
        "opencv-python",
        "pyttsx3",
        "SpeechRecognition"
    ]

    modes_CM = ["all", "list", "module", "math", "wikipedia"]

    attribs_settingshandler = ["--createfile", "--deletefile", "--getfile"]
    attribs_settingshandler_getfile = ["patfsettings_ext", "alldata"]


    desc_devtools = {
        "ENABLE": "ENABLE command enables the devtools which is necessary for using devtools.",
        "DISABLE": "DISABLE command disables the devtools which shutdowns the devtools.",
        "CMDS": "CMDS command helps to get info about devtool commands.",
        "CLcmds": "CLcmds command helps to do various functions. There are two types of this command [T: Terminal, G: Gui]"
    }

PA_ID = "pheonixstudios.pheonixapp.gui.1.0"