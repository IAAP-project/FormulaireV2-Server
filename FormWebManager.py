import time
import BaseHTTPServer
#from http.server import HTTPServer
from WebHandler import WebHandler

HOST_NAME = '127.0.0.1' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 8010 # Maybe set this to 9000.

class FormWebManager:
    def __init__(self, form):
        self.form = form
        self.server_class = BaseHTTPServer.HTTPServer
        self.httpd = self.server_class((HOST_NAME, PORT_NUMBER), WebHandler)

    def createServer(self):
        print(time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
        try:
            self.httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        self.httpd.server_close()
        print(time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))

    def stopServer(self):
        self.httpd.server_close()
        print(time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))



