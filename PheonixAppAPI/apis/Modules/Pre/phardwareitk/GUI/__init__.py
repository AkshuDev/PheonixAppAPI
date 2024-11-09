import platform

def get_platform() -> str:
    return platform.system().lower()

#Check Platform
OS:str = get_platform()
Linux:bool = False
Windows:bool = False
Unix:bool = False
Unknown_os:bool = True

if OS == "windows":
    Windows = True
    Unknown_os = False
elif OS == "linux":
    Linux = True
    Unknown_os = False
elif OS == "unix":
    Unix = True
    Unknown_os = False
else:
    Unknown_os = True

# Constants
WM_DESTROY:int = 2
WM_PAINT:int = 15