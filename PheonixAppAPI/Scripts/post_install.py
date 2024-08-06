from cryptography.fernet import Fernet
import os

def Get_Key() -> bytes:
    from PheonixAppAPI.apis import Cipher

    import os

    data = b""

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "key.bin"), "rb") as file:
        file.seek(0)
        data = file.read()
        print("READ FILE [key.bin]:", data)
        file.close()

    return Cipher.PTSEDM().decrypt(data, '')

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
    print("\nInstalling Required Files\n")
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
    print("Starting to secure Keys...")
    Secure_Keys()
    print("Process finished.")
    print("Starting to build [settings.json]")
    print("Process started.")
    Make_Json()
    print("Process finished.")
    print("all keys are now secured successfully!")
    print("All Required Files are now installed!")

if __name__ == "__main__":
    post_install()