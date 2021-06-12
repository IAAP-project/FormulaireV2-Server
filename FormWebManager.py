import time
import BaseHTTPServer
from functools import partial
#from http.server import HTTPServer
from Form import Form
from WebHandler import WebHandler

HOST_NAME = "192.168.137.28" # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 8010 # Maybe set this to 9000.

class FormWebManager:
    def __init__(self, formName, choreg):
        self.form = Form(formName, self)
        self.choregraphe = choreg
        self.server_class = BaseHTTPServer.HTTPServer
        handler = partial(WebHandler, self)
        self.httpd = self.server_class((HOST_NAME, PORT_NUMBER), handler)
        self.isRunning = False

    def retreiveEditedInputs(self):
        return self.form.retreiveEditedInputs()

    def createServer(self):
        print(time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
        try:
            self.isRunning = True
            self.httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        self.httpd.server_close()
        print(time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))

    def stopServer(self):
        if not self.isRunning:
            return
        print("Server stopped ;)")
        self.isRunning = False
        self.httpd.server_close()
        self.httpd.shutdown()
        print(time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))

    def getForm(self):
        return self.form

    def say(self,str):
        self.choregraphe.say(str)

    def sayNextInput(self, input):
        self.choregraphe.sayNextInput(input)

    def sayEndInput(self, input):
        self.choregraphe.sayEndInput(input)

    def sayEndForm(self):
        self.choregraphe.sayEndForm()


