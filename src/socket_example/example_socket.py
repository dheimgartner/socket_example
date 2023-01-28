import socket

def hello_socket():
    """Hello world for socket and communication 
    
    This is amazing!!
    """
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # get local machine name
    host = socket.gethostname()
    
    port = 12345
    
    # bind the socket to a specific address and port
    s.bind((host, port))
    
    # become a server socket
    s.listen(5)
    
    print(f'Server listening on {host}:{port}')
    
    while True:
        # establish a connection
        client_socket, addr = s.accept()
        print(f'Got a connection from {addr}')
        client_socket.send(b'Thank you for connecting')
        client_socket.close()


if __name__ == '__main__':
    hello_socket()
