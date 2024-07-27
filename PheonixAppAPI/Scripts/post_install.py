def post_install():
    print("\nInstalling Required Files\n")
    from PheonixAppAPI.pheonixapp.files import PheonixStudioStarter

    print("Starting to build [settings.ini]...")
    print("Process started.")
    PheonixStudioStarter.SettingsHandler().run("--createfile")
    print("Process finished.")
    print("[settings.ini] built successfully!")
    print("Starting to build [PATFsettings.patf]...")
    PheonixStudioStarter.PATFHandler(False, "", "API-USER", "").createfile()
    print("Process finished.")
    print("[PATFsettings.patf] built successfully!")
    print("All Required Files are now installed!")

if __name__ == "__main__":
    post_install()