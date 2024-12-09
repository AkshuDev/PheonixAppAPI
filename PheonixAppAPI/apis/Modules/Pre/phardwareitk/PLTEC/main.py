# ----------------------------------------------------------------
# Code to ASM/MACHINECODE                                        |
# ----------------------------------------------------------------
# Pheonix Studios                                                |
# ----------------------------------------------------------------
# Akshobhya                                                      |
# ----------------------------------------------------------------
# https://github.com/AkshuDev                                    |
# ----------------------------------------------------------------
import os
import sys

from . import *

if not sys.path[PHardwareITK] == PHardwareITK_P:
    sys.path.append(PHardwareITK_P)

from phardwareitk.PLTEC import ASM
from phardwareitk.PLTEC import Reader
from phardwareitk.PLTEC import OBJECT
from phardwareitk.PLTEC import Linker
from phardwareitk.PLTEC import Logger
from phardwareitk.PLTEC import Checker

Checker.PLTEC_initCheck()

def job():
    path_for_file = input("PATH: ")
    path_for_output_file = input("OUTPUT (Don't include extention): ")
    path_for_lang = input("PATH FOR LANG.json (Leave for default): ")
    extr_commands = input("EXTRA COMMANDS (Seperate via ','): ")
    extr_commands = extr_commands.lower().split(",")
    data = ""

    object_ = False

    debug = False

    if "-debug" in extr_commands:
        debug = True

    if '-object' in extr_commands or '-o' in extr_commands:
        object_ = True

    CompiledLangSET = Reader.CompileLangSET()
    Lang, LangSET, mode = Reader.Compile_LANG(CompiledLangSET, path_for_lang)

    if debug:
        Logger.LOG(TitleMsg="Compiled LangSET", errorTitle="LOG", debugMsg=str(LangSET), Message="This is the compiled language set.", descriptionMsg="A language set is a json file including assembly code as the values and the keys as the function names. These json files help to easily allow users to convert custom language by calling these functions."
                , path="PLTEC/main.py", pathMsg="This is the main file of PLTEC Converter", ErrorCode="NoError_This_is_a_log1").log()
        Logger.LOG(TitleMsg="Compiled Lang", errorTitle="LOG", debugMsg=str(Lang), Message="This is the compiled language.", descriptionMsg="A lang/language file is a json file containing all the necessary language syntax to allow the program to convert the custom language to assembly, object, etc. The keys in this file are the syntax of the words/lines and the values are the corrosponding function they call in the language SET."
                , path="PLTEC/main.py", pathMsg="This is the main file of PLTEC Converter", ErrorCode="NoError_This_is_a_log2").log()
        Logger.LOG(TitleMsg="MODE", errorTitle="LOG", debugMsg=str(mode), Message="This is the mode of the program.", descriptionMsg="This is the mode in which the program runs. This mode decides the conversion type of the program."
                , path="PLTEC/main.py", pathMsg="This is the main file of PLTEC Converter", ErrorCode="NoError_This_is_a_log3").log()

    with open(path_for_file, "r") as f:
        data = f.read()
        f.close()

    # Covert data
    Output_data = ""
    Data_SECTION = {}
    cancelled_Sections = 0

    if mode[0] == "elf" and mode[1] == "x86":
        Output_data, Data_SECTION, cancelled_Sections = ASM.x86_Linux.convert_to_asm(data, LangSET, Lang)

    if debug:
        Logger.LOG(TitleMsg="Data Section", errorTitle="LOG", debugMsg=str(Data_SECTION), Message="This is the data section of the assembly output.", descriptionMsg="The data section in assembly refers to a sepecifc section/segment of the program where all the variables are defined."
                , path="PLTEC/main.py", pathMsg="This is the main file of PLTEC Converter", ErrorCode="NoError_This_is_a_log4").log()
        
        Logger.LOG(TitleMsg="Assembly Output", errorTitle="LOG", debugMsg=str(Output_data), Message="This is the assembly output.", descriptionMsg="The assembly file is a specific low level hardware interactive file that contains human readable form of machine code which can be used to do anything with a computer. Assembly is one of the most complex, non-effcient (because of manual memory management), and flexible language in the world. All the other languages are made via assembly. It allows the user to do whatever they want with the computer."
                , path="PLTEC/main.py", pathMsg="This is the main file of PLTEC Converter", ErrorCode="NoError_This_is_a_log5").log()

    with open(path_for_output_file+".asm", "w") as f:
        f.write(Output_data)
        f.close()

    if object_:
        labels_addr = {}
        current_addr = 0

        Object = None
        if mode[0] == "elf" and mode[1] == "x86":
            Object = OBJECT.ELF(labels_addr, current_addr)

        section_t, section_d = Object.convert_to_o(Output_data, Data_SECTION)
        section_headers = Object.finalize_elf()
        if debug:
            Logger.LOG(TitleMsg="Section Headers", errorTitle="LOG", debugMsg=str(section_headers), Message="These are the section headers of the object output.", descriptionMsg="The section-headers/string-table is/are a specific portion inside the object file that define the location/address of every section in the machine code."
                    , path="PLTEC/main.py", pathMsg="This is the main file of PLTEC Converter", ErrorCode="NoError_This_is_a_log5").log()
        headers = Object.create_header(section_headers, debug)

        O = headers + section_headers + section_t + section_d

        if debug:
            Logger.LOG(TitleMsg="Object Headers", errorTitle="LOG", debugMsg=str(headers), Message="These are the headers of the object file.", descriptionMsg="The headers inside the object file are one of the most important elements that enable the OS/program to understand about the type/get the info about the file and code."
                    , path="PLTEC/main.py", pathMsg="This is the main file of PLTEC Converter", ErrorCode="NoError_This_is_a_log6").log()
            Logger.LOG(TitleMsg="Object Full Code", errorTitle="LOG", debugMsg=str(O), Message="This is the full Object File Code.", descriptionMsg="A object file is a source file that is created before every file is linked together to form a executable file like (elf32, elf64, exe32, exe64, etc). A object file can be reffered to as a full runnable file but it has to be linked before it can be executed and hence, object files are not executable."
                    , path="PLTEC/main.py", pathMsg="This is the main file of PLTEC Converter", ErrorCode="NoError_This_is_a_log7").log()

        with open(path_for_output_file+".o", "wb") as f:
            f.write(O)
            f.close()

if __name__ == "__main__":
    job()