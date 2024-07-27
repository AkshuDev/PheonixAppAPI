import setuptools.build_meta

class MyBackend(setuptools.build_meta):
    def run_install(self, install_args, env):
        # Run the normal install
        super().run_install(install_args, env)
        # Add your post-installation script here
        self.post_install()

    def post_install(self):
        print("\nInstalling Required Files\n")
        from PheonixAppAPI.pheonixapp.files import PheonixStudioStarter

        print("Starting to build [settings.ini]...")
        print("Process started.")
        PheonixStudioStarter.SettingsHandler().run("--createfile")
        print("Process finished.")
        print("[settings.ini] built successfully!")
        print("Starting to build [PATFsettings.patf]...")
        PheonixStudioStarter.PATFHandler(False, "", "API-USER", "").run("terminal --createfile")
        print("Process finished.")
        print("[PATFsettings.patf] built successfully!")
        print("All Required Files are now installed!")