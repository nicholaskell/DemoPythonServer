import SocketServer
import json

nextId = 1;

class MyTCPServer(SocketServer.ThreadingTCPServer):
    allow_reuse_address = True

class MyTCPServerHandler(SocketServer.BaseRequestHandler):
    
    def handle(self):
        try:
            global nextId
            rdata = json.loads(self.request.recv(1024).strip())
            # process the data, i.e. print it:
            print rdata
            if(rdata['ID'] == 0):
                print "ID is 0, going to assign an id of:",nextId
                
                rdata['ID'] = nextId
                nextId = nextId + 1
            else:
                print "Id is not 0"
                
            # send some 'ok' back
            self.request.sendall(json.dumps(rdata))
        except Exception, e:
            print "Exception wile receiving message: ", e

server = MyTCPServer(('127.0.0.1', 13373), MyTCPServerHandler)
server.serve_forever()
