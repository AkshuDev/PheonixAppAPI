#    _____              .___       __________            _____   __           .__          ___.   .__
#   /     \ _____     __| _/____   \______   \___.__.   /  _  \ |  | __  _____|  |__   ____\_ |__ |  |__ ___.__._____
#  /  \ /  \\__  \   / __ |/ __ \   |    |  _<   |  |  /  /_\  \|  |/ / /  ___/  |  \ /  _ \| __ \|  |  <   |  |\__  \
# /    Y    \/ __ \_/ /_/ \  ___/   |    |   \\___  | /    |    \    <  \___ \|   Y  (  <_> ) \_\ \   Y  \___  | / __ \_
# \____|__  (____  /\____ |\___  >  |______  // ____| \____|__  /__|_ \/____  >___|  /\____/|___  /___|  / ____|(____  /
#         \/     \/      \/    \/          \/ \/              \/     \/     \/     \/           \/     \/\/          \/
#     ___ ___________                      .___             ___
#    /  / \_   _____/___  __ __  ____    __| _/___________  \  \
#   /  /   |    __)/  _ \|  |  \/    \  / __ |/ __ \_  __ \  \  \
#  (  (    |     \(  <_> )  |  /   |  \/ /_/ \  ___/|  | \/   )  )
#   \  \   \___  / \____/|____/|___|  /\____ |\___  >__|     /  /
#    \__\      \/                   \/      \/    \/        /__/






# __________.__                        .__           _________ __            .___.__
# \______   \  |__   ____  ____   ____ |__|__  ___  /   _____//  |_ __ __  __| _/|__| ____  ______
#  |     ___/  |  \_/ __ \/  _ \ /    \|  \  \/  /  \_____  \\   __\  |  \/ __ | |  |/  _ \/  ___/
#  |    |   |   Y  \  ___(  <_> )   |  \  |>    <   /        \|  | |  |  / /_/ | |  (  <_> )___ \
#  |____|   |___|  /\___  >____/|___|  /__/__/\_ \ /_______  /|__| |____/\____ | |__|\____/____  >
#                \/     \/           \/         \/         \/                 \/               \/

import pathlib
import requests
import json
import os
import sys

mainDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

if __name__ == "__main__":
    os.chdir(mainDir)

    sys.path.append(os.getcwd())

from PheonixAppAPI.pheonixapp.files import LIB
from PheonixAppAPI.pheonixapp.files import HashDecoderT
from PheonixAppAPI.pheonixapp.files._PCD_ import DataBase_ as dbM

class pcd():
    def __init__(self, line):
        self.line = line
        self.Make_datatype = None
        self.Make_dict = ""
        self.Tempor_Dict_File = ''

        if 'make' in self.line:
            self.make()
        elif 'fetch' in self.line:
            self.fetch()

    def fetch(self, *args):
        fetch_file = ''
        datatype = 'Dictionary'
        fileH = []
        n_idx = 0
        n_done = False

        self.line = self.line.replace('fetch file ', '')
        self.line = self.line.replace('fetch ', '')

        while not n_done:
            if not self.line[n_idx] == " ":
                fileH.append(self.line[n_idx])
                n_idx += 1

            if self.line[n_idx] == " ":
                n_done = True
                break

        n_idx = 0
        n_done = False

        while not n_done:
            if not n_idx == len(fileH):
                fetch_file = fetch_file + fileH[n_idx]
                n_idx += 1

            if n_idx == len(fileH):
                n_done = True

        self.line = self.line.replace(fetch_file, '')
        self.line = self.line.replace(' ', '')
        if self.line == 'dict':
            datatype = 'Dictionary'
        elif self.line == 'db':
            datatype = 'Database'

        if datatype == 'Dictionary':
            mode = input(">>>: ")

        if datatype == 'Dictionary':
            if self.file_exist(fetch_file):
                with open(fetch_file, 'a+') as file:
                    data = json.load(file)
                    if mode == 'print':
                        print(data)
                    elif mode == "edit":
                        key = input("KEY: ")
                        if key in data:
                            val = input("VAL: ")
                            end = False
                            end2 = False
                            idx = 0
                            while not end:
                                if not data[idx] == key[len(key) - 1]:
                                    self.Tempor_Dict_File += data[idx]
                                    idx += 1
                                else:
                                    self.Tempor_Dict_File += ': "'
                                    idx += 1
                                    self.Tempor_Dict_File += val
                                    idx += len(val) - 1
                                    self.Tempor_Dict_File += '"'
                                    idx += 1
                                    while not end2:
                                        if not data[idx] == ']':
                                            self.Tempor_Dict_File += data[idx]
                                        else:
                                            self.Tempor_Dict_File += '}'
                                            end2 = True
                                    end2 = False
                                    idx = 0
                                    end = False
                                    file.write(self.Tempor_Dict_File)
                                    self.Tempor_Dict_File = ''
                        else:
                            self.error("Key Error:", f"Key {key} is not present inside the file")
            else:
                self.error("Exists Error:", 'File '+fetch_file+' does not exist')
        elif datatype == 'Database':
            fOu = input('|}{: ')
            if 'fetch' in fOu:
                fetchm_ = input("][ *: ")
                fetchmn_ = input("][ *: ")
                db_name = fetch_file
                db_rootpath = input('Path where your Database is stored: ')
                db_path = os.path.join(db_rootpath, db_name)
                i_password = input('Database Password: ')
                if i_password == dbM.DBManager(db_name, db_path, db_rootpath).get_pass():
                    dbM.DBManager(db_name, db_path, db_rootpath, fOu, fetchm_, fetchmn_).start_db()
                else:
                    self.error('Database Password Error:', 'Wrong password')

    def file_exist(self, file):
        return os.path.exists(file)

    def make(self, *args):
        dict_name = ''
        n_idx = 0
        n_done = False
        self.line = self.line.replace('make ', '')

        while not n_done:
            if not self.line[n_idx] == " ":
                dict_name += self.line[n_idx]
                n_idx += 1

            if self.line[n_idx] == " ":
                n_done = True

        n_idx = 0
        n_done = False

        self.line = self.line.replace(dict_name, '')

        if 'dict' in self.line:
            self.Make_datatype = 'Dictionary'
            dict_name += '.json'
            if '@db' in self.line:
                db_rootpath = input("Path where DataBase is stored: ")
                db_name = input("Name of DataBase: ")
                db_path = os.path.join(db_rootpath, db_name)
                db_pathB = True
        elif 'db' in self.line:
            self.Make_datatype = 'Database'

        if self.Make_datatype == 'Dictionary':
            lb_endB = False
            arr = False
            idx = 0
            a_sb = False
            q_endB = False
            while not lb_endB:
                if not a_sb:
                    self.Make_dict += input(">>>: ")
                self.Make_dict += input(">>>: ")
                mk = input(">>>: ")
                if mk == "{":
                    arr = False
                    self.Make_dict += mk
                else:
                    arr = True
                if not arr:
                    mk = input(">>>: ")
                    if ';' in mk:
                        mk = mk.replace(';', '')
                        self.Make_dict += mk
                    elif ',' in mk:
                        while not q_endB:
                            if ',' in mk:
                                self.Make_dict += mk + ' '
                                mk = input(">>>: ")
                            elif ';' in mk:
                                self.Make_dict += mk.replace(";", '')
                                q_endB = True
                else:
                    if ';' in mk:
                        mk = mk.replace(';', '')
                        self.Make_dict += mk
                    elif ',' in mk:
                        while not q_endB:
                            if ',' in mk:
                                self.Make_dict += mk + ' '
                                mk = input(">>>: ")
                            elif ';' in mk:
                                self.Make_dict += mk.replace(";", '')
                                q_endB = True
                if not arr:
                    self.Make_dict += input(">>>: ")
                mk = input(">>>: ")
                if '],' in mk:
                    a_sb = True
                    self.Make_dict += mk
                else:
                    self.Make_dict += mk
                    self.Make_dict += input(">>>: ")
                    lb_endB = True

            with open (dict_name, 'w') as file:
                str_dict = json.dumps(self.Make_dict)
                file.write(str_dict)
                file.close()
        elif self.Make_datatype == "Database":
            password = input("Password: ")
            dbM.Create(dict_name, password)
        elif db_pathB == True:
            with open (os.path.join(db_path, dict_name), 'w') as file:
                str_dict = json.dumps(self.Make_dict)
                file.write(str_dict)
                file.close()

    def error(self, error_type, mes):
        print("Exception - ")
        print(error_type, mes)

class run_pcd():
    def __init__(self, line):
        pcd(line)

line = input(">>>: ")
run_pcd(line)

class decode():
    def pheonix_utx(self, mes):
        return HashDecoderT.Decode(mes, "pheonix_utx").run()

class encode():
    def pheonix_utx(self, mes):
        return HashDecoderT.Encode(mes, "pheonix_utx", "PheonixStudios").run()

class rename():
    def __init__(self, root, name_of_file, exists_file_name ,counter=0,ext='.txt', mode='e+r+', custom_path=''):
        if mode == 'e+r+':
            if root == '':
                path = pathlib.Path().cwd()
            else:
                path = pathlib.Path().cwd() / root

            for f_file in path.iterdir():
                if f_file.is_dir():
                    self.do_dir(path, '1', name_of_file, f_file, exists_file_name, counter, ext, custom_path)
                if f_file.is_file:
                    if f_file.name == exists_file_name:
                        new_file2 = name_of_file+ext
                        f_file.rename(path / new_file2)
    def do_dir(self, path ,num, name_file, name, exists, counter, ext, custom_path):
        if num == '1':
            for file in name.iterdir():
                if file.is_file:
                    if file.name == exists:
                        new_file2 = name_file+ext
                        file.rename(path / new_file2)
                if file.is_dir:
                    self.do_dir(path, '2', name_file, name, exists, counter, ext, custom_path)
        elif num == '2':
            for file in name.iterdir():
                if file.is_file:
                    if file.name == exists:
                        new_file2 = name_file+ext
                        file.rename(path / new_file2)
                if file.is_dir:
                    self.do_dir(path, '1', name_file, name, exists, counter, ext, custom_path)

class download_from_web():
    def __init__(self, mode='d+', exists_file_name='f',name_of_file='README', ext='.txt',root_url='https://5f1c33e9-b401-4284-a609-899072dd261a.filesusr.com/ugd/f6ac98_c9ed83165b834b1a8b108c5bd3baf7a7.txt?dn=README.txt', c_s=8192):
        if mode == 'd+r+':
            req = requests.get(root_url)
            file_name = req.url[root_url.rfind('/')+1]

            with open(file_name, 'wb') as f:
                for chunk in req.iter_content(chunk_size=c_s):
                    if chunk:
                        f.write(chunk)
                        f.close()

            rename('PheonixApp', name_of_file, exists_file_name, 0, ext)
        elif mode == 'd+':
            req = requests.get(root_url)
            file_name = req.url[root_url.rfind('/')+1]

            with open(file_name, 'wb') as f:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        f.close()
