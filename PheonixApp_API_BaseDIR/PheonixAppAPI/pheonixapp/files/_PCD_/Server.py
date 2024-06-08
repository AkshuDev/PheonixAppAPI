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

from http.server import HTTPServer, BaseHTTPRequestHandler
import socket

class Server_Serve(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/pheonixserver/home.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = 'File not found'
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

class Connect_HostServer():
    def __init__(self, port=8000, log=False):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostname()
        self.port = port
        self.log = log
    def _start_host_(self, *args):
        self.socket.bind((self.host, self.port))
        self.socket.listen(10)
        end_host = False
        while not end_host:
            client, address = self.socket.accept()
            mes = input("|||: ")
            if self.log:
                print(f'connection from {address} has been established')
            if '#cmd#' in mes:
                mes = mes.replace('#cmd#', '')
                if mes == 'end_host':
                    client.send(bytes('end_client', 'utf-8'))
                    client.close()
                    end_host = True
            client.send(bytes(mes, 'utf-8'))
    def _start_client_(self, *args):
        self.socket.connect((self.host, self.port))
        end_client = False
        while not end_client:
            mes = self.socket.recv()
            if mes.decode('utf-8') == 'end_client':
                end_client = True
            if self.log:
                print(mes.decode('utf-8'))
    def _start_connection_server_(self, *args):
        pass