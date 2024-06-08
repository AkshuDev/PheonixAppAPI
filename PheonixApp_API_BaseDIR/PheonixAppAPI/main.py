import os
from PheonixAppAPI.pheonixapp.files import PSSbridge

class PheonixAppAPI:
    def __init__(self, LoginOrSignup:bool=False, email:str="", username:str="", password:str=""):
        self.Api = None

        if LoginOrSignup:
            self.Api = PSSbridge.API(True, False, email, username, password)
        else:
            self.Api = PSSbridge.API(False, False, email, username, password)

    def initialize(self) -> object:
        return self.Api