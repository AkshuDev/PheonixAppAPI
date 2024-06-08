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

from PheonixAppAPI.pheonixapp.files import PheonixStudioStarter

class PATFbridge():
    def __init__(self, usefileData:bool=False, email:str="", username:str="", password:str="") -> None:
        self.pss = PheonixStudioStarter.PATFHandler(usefileData, email, username, password)

    def createfile(self, flag:str=""):
        self.pss.createfile(flag)

    def getCertificatePath(self, code:str="", flag:str="+BOOL"):
        return self.pss.getCertificatePath(code, flag)

    def run(self, mode):
        self.pss.run(mode)

class API():
    def __init__(self, LoginOrSignup:bool=False, usefileData:bool=False, email:str="", username:str="", password:str="") -> None:
        self.LoginOrSignup:bool = LoginOrSignup
        self.usefiledata:bool = usefileData
        self.email:str = email
        self.username:str = username
        self.password:str = password
        self.pss = None

        if LoginOrSignup:
            self.pss = PheonixStudioStarter.PATFHandler(self.usefiledata, self.email, self.username, self.password)
        else:
            self.email = "$AOS([APICALL->NOLogin])"
            self.username = "$AOS([APICALL->NOLogin])"
            self.password = "$AOS([APICALL->NOLogin])"

            self.pss = PheonixStudioStarter.PATFHandler(self.usefiledata, self.email, self.username, self.password)

    def CheckModules(self, mode:str="all", list:list=[], module:str="") -> None:
        PheonixStudioStarter.CheckModules(mode, list, module)

    def createfile(self, flag:str="") -> None:
        self.pss.createfile(flag)

    def getCertificatePath(self, code:str="", flag:str="+BOOL") -> str:
        return self.pss.getCertificatePath(code, flag)

    def run(self, mode) -> None:
        self.pss.run(mode)