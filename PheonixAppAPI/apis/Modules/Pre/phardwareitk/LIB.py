import os

class Paths:
    # NOEXT Files are to be made without the use of the foldername.
    #Folders
    phardwareitk = os.path.dirname(os.path.abspath(__file__))
    ErrorSystem = os.path.join(phardwareitk, 'ErrorSystem')
    Extensions = os.path.join(phardwareitk, 'Extensions')
    FileSystem = os.path.join(phardwareitk, 'FileSystem')
    GUI = os.path.join(phardwareitk, 'GUI')
    HGame = os.path.join(phardwareitk, 'HGame')
    ModuleController = os.path.join(phardwareitk, 'ModuleController')
    PLTEC = os.path.join(phardwareitk, 'PLTEC')
    System = os.path.join(phardwareitk, 'System')
    CLI = os.path.join(phardwareitk, 'CLI')

    C = os.path.join(GUI, 'C')

    #Inits
    __init__PY_phardwareitk = os.path.join(phardwareitk, '__init__.py')
    __init__PY_ErrorSystem = os.path.join(ErrorSystem, '__init__.py')
    __init__PY_Extensions = os.path.join(Extensions, '__init__.py')
    __init__PY_FileSystem = os.path.join(FileSystem, '__init__.py')
    __init__PY_GUI = os.path.join(GUI, '__init__.py')
    __init__PY_HGame = os.path.join(HGame, '__init__.py')
    __init__PY_ModuleController = os.path.join(ModuleController, '__init__.py')
    __init__PY_PLTEC = os.path.join(PLTEC, '__init__.py')
    __init__PY_System = os.path.join(System, '__init__.py')
    __init__PY_CLI = os.path.join(CLI, '__init__.py')

    #Files in phardwareitk
    defrunSettingsNOEXT = os.path.join(phardwareitk, 'defrunSettings')
    DependenciesPY_phardwareitk = os.path.join(phardwareitk, 'Dependencies.py')

    #Files in CLI
    cliToolKitPY_CLI = os.path.join(CLI, 'cliToolKit.py')

    #Files in ErrorSystem
    ErrorSystemPY_ErrorSystem = os.path.join(ErrorSystem, 'ErrorSystem.py')

    #Files in Extention
    HyperOutPY_Extensions = os.path.join(Extensions, 'HyperOut.py')
    HyperInPY_Extensions = os.path.join(Extensions, 'HyperIn.py')

    #Files in FileSystem
    FileSystemPY_FileSystem = os.path.join(FileSystem, 'FileSystem.py')

    #Files in GUI
    guiPY_GUI = os.path.join(GUI, 'gui.py')
    gui_sdlPY_GUI = os.path.join(GUI, 'gui_sdl.py')
    renderGUIPYX_GUI = os.path.join(GUI, 'renderGUI.pyx')
    renderGUIPYD_GUI = os.path.join(GUI, 'renderGUI.pyd')
    renderGUISO_GUI = os.path.join(GUI, 'renderGUI.so')

    #Files in HGame

    #Files in ModuleController
    mainPY_ModuleController = os.path.join(ModuleController, 'main.py')

    #Files in PLTEC
    anayzerPY_PLTEC = os.path.join(PLTEC, 'anayzer.py')
    ASMPY_PLTEC = os.path.join(PLTEC, 'ASM.py')
    CheckerPY_PLTEC = os.path.join(PLTEC, 'Checker.py')
    DEF_langJSON_PLTEC = os.path.join(PLTEC, 'DEF_lang.json')
    DEF_LanguageSETJSON_PLTEC = os.path.join(PLTEC, 'DEF_LanguageSET.json')
    LinkerPY_PLTEC = os.path.join(PLTEC, 'Linker.py')
    LoggerPY_PLTEC = os.path.join(PLTEC, 'Logger.py')
    mainPY_PLTEC = os.path.join(PLTEC, 'main.py')
    OBJECTPY_PLTEC = os.path.join(PLTEC, 'OBJECT.py')
    ReaderPY_PLTEC = os.path.join(PLTEC, 'Reader.py')

    #File in System
    SysUsagePY_System = os.path.join(System, 'SysUsage.py')