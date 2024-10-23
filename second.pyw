import os
from select import select
import time
import socket
import sys
import datetime

login_pass = open('./user/password.txt')
login_name = open('./user/username.txt')
l_p = login_pass.read()
l_n = login_name.read()

print("""naber
bu bilalin işletim sistemi""")
print("hg naber " + l_n + "!")
print("bugün: " + time.strftime("%d / %m / %y"))
while True:
    print("""
[1] google aç
[2] notepad aç
[3] dosyaları aç
[4] saati aç
[5] çıkış
""")
    select = input("[?]: ")

    if select == '1':
        os.startfile('tarayici.py')

    if select == '2':
        os.startfile('notepad.py')

    if select == '3':
        os.startfile('explorer.pyw')

    if select == '4':
        os.startfile('time.pyw')

    if select == '5':
        quit()
        break

