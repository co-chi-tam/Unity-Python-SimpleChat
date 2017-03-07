import socket;
import select;
import _thread;

server_socket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost' #socket.gethostname()
port = 9999
max_buffer = 2048

server_socket.bind((host, port))
server_socket.listen (20)

CONNECTION_LIST = []

print ('Server starting ... HOST %s PORT %d' % (host, port))

def receiveConnect():
    while True:
        client_socket, addr = server_socket.accept()
        CONNECTION_LIST.append(client_socket)
        print ('Got a connect from %s + count %d' % (str(addr), len(CONNECTION_LIST)))
        msg = 'Thank you for connecting ' + '\r\n'
        client_socket.send (msg.encode('ascii'))
        #client_socket.close()

_thread.start_new_thread(receiveConnect, ())

def broadcast_msg(sock, message):
    for socket in CONNECTION_LIST:
        if socket != server_socket:
            try:
                socket.send(message)
            except:
                socket.close()
                CONNECTION_LIST.remove(socket)
                continue

while True:
    for sock in CONNECTION_LIST:
        if sock != server_socket:
            try: 
                msg = sock.recv(max_buffer)
                if msg:
                    print (msg.decode('ascii'))
                    broadcast_msg (sock, msg)
            except:
                sock.close()
                CONNECTION_LIST.remove(sock)
                continue
                
server_socket.close()




























