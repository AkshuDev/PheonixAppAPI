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

import os
import subprocess
import time
import pathlib
import xlsxwriter
from importlib.machinery import SourceFileLoader

class Create():
    def __init__(self, name, password, rootpath=''):
        self.name = name
        self.password = password
        if rootpath == '':
            self.rootpath = input("Path: ")
        else:
            self.rootpath = rootpath
        self.path = os.path.join(self.rootpath, self.name).replace('\\', '\\\\')
        self.lockcode = f"""
import subprocess

class AskL():
    def __init__(self, mode='l', type='', mes=''):
        self.passw = '{self.password}'
        self.mes = mes
        self.mode = mode
        self.type = type
        self.path = '{self.path}'
    def give_dbPass(self, *args):
        return self.passw
    def start(self, *args):
        if self.mode == 'l':
            self.lock()
        elif self.mode == 'ul':
            self.unlock()
        elif self.mode == 'err':
            self.error(self.type, self.mes)
        elif self.mode == 'give_dbPass':
            return self.give_dbPass()
        else:
           self.error('@d_print', 'None')
    def lock(self, *args):
        pasw = input('Please Enter Your DataBase Password: ')
        if pasw == self.passw:
            subprocess.check_call(['attrib', '+H', f'{'{self.path}'}'])
    def unlock(self, *args):
        pasw = input('Please Enter Your DataBase Password: ')
        if pasw == self.passw:
            subprocess.check_call(['attrib', '-H', f'{'{self.path}'}'])
    def error(self, type, mes):
        if type != '@d_print':
            print(type, mes)
        """
        self.lockrunner = """
mode = ''
if mode == '':
    mode = input('Press (Enter) For Skip: ')

if mode != 'l' or mode != 'ul':
    AskL(mode).start()
else:
    AskL(mode).start()
        """
        self.full_lock_code = self.lockcode + self.lockrunner

        os.mkdir(self.path)
        with open(os.path.join(self.rootpath, f'{self.name}_unlocker.py'), 'w') as db_ul:
            db_ul.write(self.full_lock_code)
        with open("pheonixserver\\javascript_itneed(db).txt", "w+") as jsiDb:
            jsiDb.write(self.name)

class DBManager():
    def __init__(self, db_name, db_path, db_rootpath, func='func', fetch_m = 'files', fetch_mn = 'None', upt_Type='file', upt_Mode='None'):
        self.db_name = db_name
        self.fetchm = fetch_m
        self.db_rootpath = db_rootpath
        self.fetchmn = fetch_mn
        self.func = func
        self.db_path = db_path
        self.upt_type = upt_Type
        self.upt_mode = upt_Mode
        self.fetch_type = ''
    def start_db(self, *args):
        print('Starting database...')
        if 'fetch' in self.func:
            print('Started')
            if '@get' in self.func:
                return self.fetch('return')
            elif '@give-' in self.func:
                self.fetch_type = self.func.replace('fetch@give-', '')
                self.fetch(self.fetch_type)
            elif '@out' in self.func:
                self.fetch_type = 'print'
                self.fetch(self.fetch_type)
        elif self.func == 'update':
            self.update()
        elif self.func == 'ul':
            self.ulDB()
        elif self.func == 'l':
            self.lDB()
        else:
            self.error('Unknown function:', self.func)
    def ulDB(self, *args):
        subprocess.check_call(['attrib', '-H', self.db_path])
    def error(self, type, mes):
        print(type, mes)
    def lDB(self, *args):
        subprocess.check_call(['attrib', '+H', self.db_path])
    def get_pass(self, *args):
        unlocker_name = os.path.join(self.db_rootpath, self.db_name+'_unlocker.py')
        unlocker = SourceFileLoader(unlocker_name.replace('.py', ''), os.path.join(self.db_rootpath, unlocker_name)).load_module()
        unlocker.mode = 'give_dbPass'
        return unlocker.AskL(unlocker.mode).start()

    def fetch(self, args):
        print('log started...')
        time.sleep(1)
        print('checking types and args')
        if self.fetchm == 'files@list':
            print('found list')
            output = os.listdir(self.db_path)
            print('checking args')
            if 'return' in args:
                print('returning')
                return output
            elif 'print' in args:
                print('printing output')
                print(output)
        elif self.fetchm == 'file@single':
            print('found at single file')
            list_ = os.listdir(self.db_path)
            print('for loop started')
            for file_ in list_:
                if file_ == self.fetchmn:
                    print('file confirmed')
                    if 'print' in args:
                        print('printing file')
                        print(file_, '-', 'Exists')
                    else:
                        print('returning file')
                        return file_

    def update(self, *args):
        pass

class makeSQL():
    def __init__(self, fileName: str, data: list, headers_list: list):
        self.fileName = fileName
        self.data = data
        self.data2 = headers_list
        self.create_sql()
    def create_sql(self, *args):
        workbook = xlsxwriter.Workbook(self.fileName+'.xlsx')
        worksheet = workbook.add_worksheet(self.fileName+'_Sheet')

        for idx, header in enumerate(self.data2):
            worksheet.write(0, idx, str(header).capitalize())

        for idx1, entry in enumerate(self.data):
            for idx2, header in enumerate(self.data2):
                worksheet.write(idx1+1, idx2, entry[header])

        workbook.close()

# makeSQL("Test", ["test", "test2"], [
#     {
#         'test': "testgod",
#         'test2': 'testgod2'
#     }])