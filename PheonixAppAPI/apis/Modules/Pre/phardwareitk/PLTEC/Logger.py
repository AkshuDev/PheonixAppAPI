import os
import sys
import datetime
from typing import *

class LOG():
    def __init__(self, dateTime:bool=True, logLevel:int=1, debugLog:bool=True, pathInclude:bool=True, pathMsgInclude:bool=True, MessageInclude:bool=True,
                descriptionInclude:bool=True, errorTitleInclude:bool=True, titleInclude:bool=True, TitleMsg:str = "", errorTitle:str="", debugMsg:str="", dateFormat:str="%d-%m-%y %I:%M:%S %p",
                path:str="", pathMsg:str="", Message:str="", descriptionMsg:str="", ErrorCodeInclude:bool=True, ErrorCode: str="",
                LogFormat:str="\n$dateTime$:%$Title$%<->%$Error->%$errorTitle$:\n$Message$\n\nDescription:%$description$\n\nPath:%$path$:%$pathMsg$\n\nDebug:%$debugLog$\nCode:%$ErrorCode$^PERCENT^ ") -> None:
        
        """
        MAIN initialize function


        LogFormat % refers to the the sperater string after ^PERCENT^. DEFAULT: SPACE (' ')


        VARIABLES IN LogFormat: ['dateTime', 'Title', 'errorTitle', 'Message', 'description', 'path', 'pathMsg', 'debugLog', 'ErrorCode']
        """

        dateNOW = datetime.datetime.now()
        self.dateTime = dateNOW.strftime(dateFormat)

        self.logLevel:bool = logLevel
        self.errorCodeInclude = ErrorCodeInclude
        self.debugLog:bool = debugLog
        self.pathInclude:bool = pathInclude
        self.pathMsgInclude:bool = pathMsgInclude
        self.MessageInclude:str = MessageInclude
        self.descriptionInclude:bool = descriptionInclude
        self.errorTitleInclude:bool = errorTitleInclude
        self.titleInclude:bool = titleInclude
        self.titleMsg:str = TitleMsg
        self.errorTitle:str = errorTitle
        self.debugMsg:str = debugMsg
        self.dateFormat:str = dateFormat
        self.path:str = path
        self.pathMsg:str = pathMsg
        self.Message:str = Message
        self.descriptionMsg:str = descriptionMsg
        self.LogFormat:str = LogFormat
        self.errorCode:str= ErrorCode

        self.LOGvariables:dict = {
            'dateTime': self.dateTime,
            'Title': self.titleMsg,
            'errorTitle': self.errorTitle, 
            'Message': self.Message, 
            'description': self.descriptionMsg, 
            'path': self.path, 
            'pathMsg': self.pathMsg, 
            'debugLog': self.debugMsg, 
            'ErrorCode': self.errorCode,
            "dateTime_include": dateTime,
            "Title_include": self.titleInclude,
            "errorTitle_include": self.errorTitleInclude,
            "Message_include": self.MessageInclude,
            "description_include": self.descriptionInclude,
            "path_include": self.pathInclude,
            "pathMsg_include": self.pathMsgInclude,
            "debugLog_include": self.debugLog,
            "ErrorCode_include": self.errorCodeInclude,
        }

    def _compileLOG(self) -> str:
        """
        Not to be called directly from script.
        """
        log:str = ""

        logSplit = self.LogFormat.split("$")
        logSeperator = logSplit[len(logSplit)-1].split("^PERCENT^")[1]

        logSplit.pop(len(logSplit)-1)

        for k, j in enumerate(logSplit):
            logSplit[k] = j.replace("%", logSeperator)

        for i, v in enumerate(logSplit):
            if v in self.LOGvariables.keys():
                if self.LOGvariables[v+"_include"] == True:
                    log += self.LOGvariables[v]
            else:
                log += v

        return log
    
    def log(self, returnType:Union[str, None]=None) -> Union[str, None]:
        """
        'None' means printing the log and 'str' means, it returns the log.
        """
        log:str = self._compileLOG()

        if returnType is None:
            print(log)
            return None
        else:
            return log
