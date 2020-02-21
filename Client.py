import socket
import sys

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error as err:
    print("ERROR :- socket creation failed with error %s" % (err))

port = 52191

try:
    host_ip = input(str("Enter host IP of the VM:\n"))
except socket.gaierror:
    # this means could not resolve the host
    print("ERROR :- There was an error resolving the host")
    sys.exit()

print("The socket has successfully connected to serever on ip {} port {}".format(host_ip, port))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # connecting to the server
    client_socket.connect((host_ip, port))  # '192.168.1.6'

    # Receiving login packet
    data = client_socket.recv(1024)
    data = data.decode('utf-8')
    print("Received LOGIN_DATA_PACKET_FRAME as - ", data)
    if data == '78 78 11 01 03 51 60 80 80 77 92 88 22 03 32 01 01 AA 53 36 0D 0A':
        data = '78 78 05 01 00 05 9F F8 0D 0A'
        # Sending LoginDataPacketFrame response
        client_socket.sendall(data.encode('utf-8'))
        print("Sent RESPONSE_LOGIN_DATA_PACKET_FRAME as - ", data.encode('utf-8'))

    # Receiving heartbeat packet
    data = client_socket.recv(1024)
    data = data.decode('utf-8')
    print("Received HEARTBEAT_DATA_PACKET_FRAME as - ", data)
    if data == '78 78 0B 23 C0 01 22 04 00 01 00 08 18 72 0D 0A':
        data = '78 78 05 23 01 00 67 0E 0D 0A'
        # Sending HeartBeatDataPacketFrame response
        client_socket.sendall(data.encode('utf-8'))
        print("Sent RESPONSE_HEARTBEAT_DATA_PACKET_FRAME as - ", data.encode('utf-8'))

    # Receiving GPS packet
    data = client_socket.recv(1024)
    data = data.decode('utf-8')
    print("Received GPS_LOCATION_DATA_PACKET_FRAME as - ", data)
    if data == '78 78 22 22 0F 0C 1D 02 33 05 C9 02 7A C8 18 0C 46 58 60 00 14 00 01 CC 00 28 7D 00 1F 71 ' \
                           '00 00 01 00 08 20 86 0D 0A':
        # Sending GPSDataPacketFrame response
        client_socket.sendall(data.encode('utf-8'))
        print("Sent RESPONSE_GPS_LOCATION_DATA_PACKET_FRAME as - ", data)
        print('Received', repr(data))
        client_socket.close()
