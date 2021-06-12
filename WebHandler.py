#from http.server import BaseHTTPRequestHandler
import json
import BaseHTTPServer

class WebHandler(BaseHTTPServer.BaseHTTPRequestHandler, object):
    def __init__(self, formManager, request, client_address, server):
        self.formManager = formManager
        super(WebHandler, self).__init__(request, client_address, server)

    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(self):
        if "STOP_SERVER" in self.path:
            self.formManager.stopServer()
        else:
            dict = {}
            for input in self.formManager.retreiveEditedInputs():
                dict[input.getId()] = input.getValue()

        #print("ok" + str(dict))



        self.send_response(200)
        self.addHeaders()
        self.wfile.write(json.dumps(dict).encode(encoding="utf_8"))
        """Send edited inputs."""
        '''s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("<html><head><title>Title goes here.</title></head>")
        s.wfile.write("<body><p>This is a test.</p>")
        # If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".
        s.wfile.write("<p>You accessed path: %s</p>" % s.path)
        s.wfile.write("</body></html>")'''

    def do_POST(self):
        data_string = self.rfile.read(int(self.headers['Content-Length']))
        print("{}".format(data_string))
        data = json.loads(data_string)
        for key in data:
            self.formManager.getForm().saisieById(data[key], key)
        return

    def do_OPTIONS(self):
        self.addHeaders()

    def addHeaders(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
