import socket
import json

data = {'ID':0,'status':0}
print "Pre data:",data

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 13373))
s.send(json.dumps(data))
result = json.loads(s.recv(1024))
if(result['ID'] > 0):
    data['ID'] = result['ID']
print result
print data
s.close()