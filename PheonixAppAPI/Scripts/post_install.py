from cryptography.fernet import Fernet
import os

def Encrypt_Maps(key: bytes) -> None:
    data = ''

    if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "key.bin")):
        return None

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "pheonixapp", "files", "Mapper", "DEFAULT_MAPS.json"), "r") as file:
        file.seek(0)
        data = file.read()
        file.close()

    fernet = Fernet(key)
    enc_data = fernet.encrypt(data.encode())

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "pheonixapp", "files", "Mapper", "DEFAULT_MAPS.encMaps"), "wb") as file:
        file.seek(0)
        file.write(enc_data)
        file.close()

    os.remove(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "pheonixapp", "files", "Mapper", "DEFAULT_MAPS.json"))

def Get_Maps(key: bytes) -> dict:
    data = ''

    if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "key.bin")):
        return {"NoKey.BinFileFound!": "0001"}

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "pheonixapp", "files", "Mapper", "DEFAULT_MAPS.encMaps"), "rb") as file:
        file.seek(0)
        data = file.read()
        file.close()

    fernet = Fernet(key)

    data = fernet.decrypt(data)

    import json
    return json.loads(data)

def Get_Map(key: bytes, map_name:str) -> dict:
    data = ''

    if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "key.bin")):
        return {"NoKey.BinFileFound!": "0001"}

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "pheonixapp", "files", "Mapper", "DEFAULT_MAPS.encMaps"), "rb") as file:
        file.seek(0)
        data = file.read()
        file.close()

    fernet = Fernet(key)

    data = fernet.decrypt(data)

    import json
    return json.loads(data)[map_name]

def Get_Key() -> bytes:
    from PheonixAppAPI.apis import Cipher

    import os

    data = b""

    if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "key.bin")):
        return "NoKey.BinFileFound!"

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "key.bin"), "rb") as file:
        file.seek(0)
        data = file.read()
        file.close()

    cipherfin =  Cipher.PTSEDM().decrypt(data, '')
    return cipherfin

def Secure_Keys() -> None:
    key = Fernet.generate_key()

    print(f"IMPORTANT: CRYPTOGRAPHY KEY IS -> {key}")

    import os

    from PheonixAppAPI.apis import Cipher

    data = Cipher.PTSEDM().encrypt(key, "", "")

    print("ENCRYPTED KEY:", data)

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "key.bin"), "wb") as file:
        file.write(data)
        file.close()

    check = Get_Key()
    print("GOT KEY:", check)

    if not check == key.decode():
        print("Key Securing failed! The output key doesn't match the expected key.\nExiting...")
        exit(1)

def Make_Json() -> None:
    print("Opening File [settings.json]...")
    import json

    settings = {
        "ModuleRegistry": {
            "PheonixStudios": {
                "Names": ["PheonixAppAPI", "pcd_py", "PheonixJson"],
                "Modules": {
                    "PheonixAppAPI": {
                        "Active": "true"
                    },
                    "pcd_py": {
                        "Active": "false"
                    },
                    "PheonixJson": {
                        "Active": "false"
                    }
                }
            }
        }
    }

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "settings.json"), "w") as file:
        print("File Opened")
        print("Writing File...")
        file.seek(0)
        json.dump(settings, file)
        file.close()

def post_install() -> None:
    i = input("This Script will install *33.007485 mb of data to your computer. Is it ok? (y/n): ")
    if i.lower() == "n":
        print("The module requires these files. Exiting!")
        exit(1)
    elif i.lower() == "y":
        pass
    else:
        print("The character could not be understood. The module requires these files. Exiting!")
        exit(1)
    print("\nInstalling Required Files\n")
    from PheonixAppAPI.Scripts import RESOURCES
    RESOURCES.MakeDEFMAPS()

    print("Starting to secure Keys...")
    Secure_Keys()
    print("Process finished.")
    print("Starting to encrypt Default Maps")
    print("Process started.")
    Encrypt_Maps(Get_Key())
    print("Process finished.")
    print("All Default Maps are now encrypted successfully!")
    print("Starting to build CipherTable.json")
    print("Process started.")
    RESOURCES.MAKE_Enc_Table()
    print("Process finished.")

    from PheonixAppAPI.pheonixapp.files import PheonixStudioStarter

    print("Starting to build [settings.ini]...")
    print("Process started.")
    PheonixStudioStarter.SettingsHandler().run("--createfile")
    print("Process finished.")
    print("[settings.ini] built successfully!")
    print("Starting to build [PATFsettings.patf]...")
    PheonixStudioStarter.PATFHandler(False, "temp@gmail.com", "API-USER", "None").createfile()
    print("Process finished.")
    print("[PATFsettings.patf] built successfully!")
    print("Starting to build [settings.json]")
    print("Process started.")
    Make_Json()
    print("Process finished.")
    print("All keys are now secured successfully!")
    print("All Required Files are now installed!")

if __name__ == "__main__":
    post_install()