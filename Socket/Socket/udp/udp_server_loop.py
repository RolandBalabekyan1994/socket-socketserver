import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("localhost", 8888))

while True:
    try:
        result = sock.recv(1024)
    except KeyboardInterrupt:
        break
    else:
        print("Message", result.decode("utf-8"))