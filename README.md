# ConCox-GPS-Device-Tracker

Create a simulator & Device Adapter for a Concox device which does the following:



Device Simulator

Sends login packet always (78 78 11 01 03 51 60 80 80 77 92 88 22 03 32 01 01 AA 53 36 0D 0A).
Sends heartbeat packet on login packet response (78 78 0B 23 C0 01 22 04 00 01 00 08 18 72 0D 0A).
Continues to send this packet on heartbeat packet response.
Sends GPS location packet on login packet response (78 78 22 22 0F 0C 1D 02 33 05 C9 02 7A C8 18 0C 46 58 60 00 14 00 01 CC 00 28 7D 00 1F 71 00 00 01 00 08 20 86 0D 0A).
Continues to send this packet on login packet response.



Device Adapter

Receives the login packet.
Responds to the login packet.
Receives the heartbeat packet.
Responds to the heartbeat packet.
Receives the GPS location packet.
Responds to GPS location packet.
Saves GPS location packet in a file storage.
