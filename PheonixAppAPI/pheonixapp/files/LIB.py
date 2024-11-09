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
    from PheonixAppAPI.Scripts import post_install

    key = post_install.Get_Key()
    PSntx_H1 = post_install.Get_Map(key, "PSntx_H1")

    pheonix_utx = post_install.Get_Map(key, "pheonix_utx")

    hype_space = post_install.Get_Map(key, "hype_space")

    hype_space_bin = post_install.Get_Map(key, "hype_space_bin")

    pheonix_utx_DESC = "Lower alphabets, numbers and some symbols allowed."

    PSntx_H1_DESC = "Only lower alphabets are allowed."

    hype_space_DESC = "Every Character is allowed."

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