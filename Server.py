# import os
import socket

# import sys
# import pickle
# import numpy as np
# import zlib

HOST = '10.16.33.135'
# HOST = '192.168.1.6'
PORT = 52191

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    print('Socket created')
    server_socket.bind((HOST, PORT))
    print('Socket bind complete')
    server_socket.listen(10)
    print('Socket now listening')

    conn, addr = server_socket.accept()
    try:
        with conn:
            print('Connected by', addr)
            while True:
                # Sending LoginDataPacketFrame
                data = '78 78 11 01 03 51 60 80 80 77 92 88 22 03 32 01 01 AA 53 36 0D 0A'
                conn.sendall(data.encode('utf-8'))
                print("Sent LOGIN_DATA_PACKET_FRAME as - ", data.encode('utf-8'))

                # receiving response for LoginDataPacketFrame
                data = conn.recv(1024)
                data = data.decode('utf-8')
                print("Received RESPONSE_LOGIN_DATA_PACKET_FRAME as - ", data)
                if data == '78 78 05 01 00 05 9F F8 0D 0A':

                    while data != '78 78 05 23 01 00 67 0E 0D 0A':
                        # sending heartbeat packet
                        data = '78 78 0B 23 C0 01 22 04 00 01 00 08 18 72 0D 0A'
                        conn.sendall(data.encode('utf-8'))
                        print("Sent HEARTBEAT_DATA_PACKET_FRAME as - ", data.encode('utf-8'))

                        # receiving response for HeartBeatDataPacketFrame
                        data = conn.recv(1024)
                        data = data.decode('utf-8')
                        print("Received RESPONSE_HEARTBEAT_DATA_PACKET_FRAME as - ", data)


                # sending GPS Location packet
                data = '78 78 22 22 0F 0C 1D 02 33 05 C9 02 7A C8 18 0C 46 58 60 00 14 00 01 CC 00 28 7D 00 1F 71 00 00 01 00 08 20 86 0D 0A'
                conn.sendall(data.encode('utf-8'))
                print("Sent GPS_LOCATION_DATA_PACKET_FRAME as - ", data.encode('utf-8'))

                # receiving response for GPSDataPacketFrame
                data = conn.recv(1024)
                data = data.decode('utf-8')
                print("Received RESPONSE_GPS_LOCATION_DATA_PACKET_FRAME as - ", data)
                if data == '78 78 22 22 0F 0C 1D 02 33 05 C9 02 7A C8 18 0C 46 58 60 00 14 00 01 CC 00 28 7D 00 1F 71 00 ' \
                           '00 01 00 08 20 86 0D 0A':
                    f = open("gps.txt", "a+")
                    f.write("\nGPS_LOCATION_DATA_PACKET is :- \n" + data)
                    f.close()

                if not data:
                    break
                data = data.encode('utf-8')
                conn.sendall(data)
                server_socket.close()
    except:
        print("\n\n\t\t\t\t\t\t\t\t\t\t\t *-* CONNECTION CLOSED *-* ")