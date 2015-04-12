import SocketServer
import SimpleHTTPServer
import os

#what port to serve on
port = 8080

#where we define what the server does
class getHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        #send the index.html page to the browser
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        index = open("index.html").read()
        self.wfile.write(index)

        #let the user do some things
        if self.path.startswith("/hello"):
            print "hello!"

#start the server
try:
    #this lines to allow socket reuse
    SocketServer.TCPServer.allow_reuse_address = True
    server = SocketServer.TCPServer(('',port), getHandler)
    
    print "started serving on port", port
    server.serve_forever()
except KeyboardInterrupt:
    print "quitting"
    server.socket.close()
