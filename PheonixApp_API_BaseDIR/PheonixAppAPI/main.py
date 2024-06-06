import os
from pheonixapp.files import PSSbridge

class INITIALIZE:
    def __init__(self, LoginOrSignup:bool=False, email:str="", username:str="", password:str=""):
        if LoginOrSignup:
            PSSbridge.API(False, email, username, password).LoginOrSignup()
        else:
            PSSbridge.API(False, email, username, password).No_LoginOrSignUp()