import time
import BaseHTTPServer
from WebHandler import WebHandler

HOST_NAME = 'example.net' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 80 # Maybe set this to 9000.

class FormWebManager:
    def __init__(self,form):
        self.form=form


    def createServer(self):
        server_class = BaseHTTPServer.HTTPServer
        httpd = server_class((HOST_NAME, PORT_NUMBER), WebHandler)
        print(time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        httpd.server_close()
        print(time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))



