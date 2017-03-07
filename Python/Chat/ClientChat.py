import socket;
import _thread;

class ClientChat(object):
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.host = socket.gethostname()
        #self.port = 9999
        print ('Client created ...')
    def clientConnect(self, host, port, revCallBack):
        self.host = host
        self.port = port
        self.max_buffer = 2048
        self.client_socket.connect((self.host, self.port))
        _thread.start_new_thread(self.receiveMessage, (revCallBack, ))
        print ('Client starting ...')
    def receiveMessage(self, callback):
        while True:
            msg = self.client_socket.recv(self.max_buffer)
            if msg:
                print ("Receive message: %s" % msg.decode('ascii'))
                if callback:
                    callback (msg.decode('ascii'))
    def sendMessage(self, message):
        self.client_socket.send (message.encode('ascii'))
    def closeConnect(self):
        self.client_socket.close()

