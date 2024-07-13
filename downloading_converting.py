import getpass
import time
import socket
from datetime import datetime


print("--------------------------------------------WELCOME TO SWIFT--------------------------------------------------------------")
time.sleep(1)

print("$ global_server/start")
time.sleep(1)

def login():
    Login = input("Login: ")
    Password = input("Password: ")

if __name__ == "__main__":
    login()
    
def fname(arg):
    pass
print("")
time.sleep(1)
print("CONNECTED")
time.sleep(1)

import sys
total = []

print("---------------------------------------------------")
print("**************welcome to SWIFT*********************")
print("---------------------------------------------------")

scrollTxt("|----------------------------------------------------|", blue, 0.02)
scrollTxt("| no |  catagory   | user id                         |", blue, 0.02)
scrollTxt("|----------------------------------------------------|", blue, 0.02)
scrollTxt("| 01 |  Profile    | Kongali1720&GatotKaca - 10229   |", blue, 0.02)
scrollTxt("|----------------------------------------------------|", blue, 0.02)
scrollTxt("| 02 |  swift      | Kongali1720&GatotKaca - 19010   |", blue, 0.02)
scrollTxt("|----------------------------------------------------|", blue, 0.02)
scrollTxt("| 03 |  gpi        | Kongali1720&GatotKaca - 17321   |", blue, 0.02)
scrollTxt("|----------------------------------------------------|", blue, 0.02)
scrollTxt("| 04 |  ipip       | Kongali1720&GatotKaca - 10972   |", blue, 0.02)
scrollTxt("|----------------------------------------------------|", blue, 0.02)
scrollTxt("| 05 |  fin        | Kongali1720&GatotKaca - 41100   |", blue, 0.02) 
scrollTxt("|----------------------------------------------------|", blue, 0.02)

    kode = int(input("Select Catagory  : "))
    if kode == 1:
        jumlah1 = int(input("Input YOUR SWIFT CODE: "))
        total1 = 23000 * jumlah1
        total.append(total1)
        tanya()
    elif kode == 2:
        jumlah2 = int(input("Input YOUR SWIFT CODE: : "))
        total2 = 41100 * jumlah2
        total.append(total2)
        tanya()
    elif kode == 3:
        jumlah3 = int(input("Input IPIP : "))
        total3 = 59000 * jumlah3 
        total.append(total3)
        tanya()
    elif kode == 4:
        jumlah4 = int(input("Input FIN : "))
        total4 = 23000 * jumlah4
        total.append(total4)
        tanya()
   
    return

def tanya():
    print("\n---------------------------------------------")
    tanya = input("Are you sure? [YES/NO] : ")
    print("-----------------------------------------------")
    if tanya == "y":
        daftar_barang()
    elif tanya == "t":
        akhir()
    else:
        print("Pilihan yang anda masukan salah!")

def akhir():
    for harga in total:
        print("SubTotal         : ", sum(total))
        diskon = 0
        a = sum(total)
        if a > 500000:
            diskon = a * 8/100
        elif a > 300000:
            diskon = a * 5/100
        elif a > 200000:
            diskon = a * 3/100
        elif a > 100000:
            diskon = a * 1/100
        else:
            diskon = 0
        print("Potongan Harga   : ", diskon)
        totalakhir = a - diskon
        print("Total            : ", totalakhir)
        print("-------------------------------------------")
        bayar = int(input("Bayar            :  "))
        kembalian = bayar - totalakhir
        print("Kembalian        : ", kembalian)
        print("-------------------------------------------")
        print("          Terima Kasih         ")
        print("-------------------------------------------")

daftar_barang()

def get_current_datetime():
    # Get the current date and time
    now = datetime.now()
    
    # Format the date and time as a string
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    return current_time

if __name__ == "__main__":
    current_time = get_current_datetime()
    print(f"{current_time}")
    
print("SWIFT-ACKS-COM-121213000490++DEUTSCHE BANK AG") 
time.sleep(2)
print("..........................................................................................................................")
time.sleep(4)

print("$ global_server/downloads/blockchain/converting/usdt")
time.sleep(3)
def login():
    TRANSACTIONREFERENCENUMBER = input("TRANSACTION REFERENCE NUMBER: ")
    BANKOPERATIONCODE = input("BANK OPERATION CODE: ")
    BANKSENDER = input("BANK SENDER: ")
    ACCOUNTNUMBERIBAN =input("ACCOUNT NUMBER/IBAN: ")
    
if __name__ == "__main__":
    login()
    
def fname(arg):
    pass
print("")
time.sleep(8)
print("CONNECTED")
time.sleep(1)

def get_current_datetime():
    # Get the current date and time
    now = datetime.now()
    
    # Format the date and time as a string
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    return current_time

if __name__ == "__main__":
    current_time = get_current_datetime()
    print(f"{current_time}")
    
time.sleep(5)

print("CURRENCY/AMOUNT   : EURO 5,137,653,123.00")
time.sleep(8)

print("-----------------------------------------------CONVERTING-----------------------------------------------------------------")
time.sleep(12)
import math

def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = '█' * int(percent) + '-' * (100 - int(percent))
    print(f"\r|{bar}| {percent:.2f}%", end="\r")
            
numbers = [x * 5 for x in range(2000, 3000)]
results = []


progress_bar(0, len(numbers))
for i, x in enumerate(numbers):
    results.append(math.factorial(x))
    progress_bar(i + 1, len(numbers))

print("---------------------------------------------------100--------------------------------------------------------------------")
time.sleep(8)

print("Other addresses for www.db.com (scanned)")
print("92.123.103.97 2a02:26f0:d8::1740:c30 2a02:26f0:d8::1740:c49r")
time.sleep(0.1)
print("DNS record for 92.123.103.82: a92-123-103-82.deploy.static.akamaitechnologies.com") 
time.sleep(0.1)
print("DNS record for 92.123.103.82: a92-123-103-82.deploy.static.akamaitechnologies.com")
time.sleep(0.1)
print("Discovered open port 146/tcp on 92.123.103.82")
time.sleep(0.1)
print("Discovered open port 146/tcp on 92.123.103.82")
time.sleep(0.1)
print("Discovered open port 3998/tcp on 92.123.103.82")
time.sleep(0.1)
print("Discovered open port 8899/tcp on 92.123.103.82")
time.sleep(0.1)
print("Discovered open port 500/tcp on 92.123.103.82")
time.sleep(0.1)
print("Discovered open port 6565/tcp on 92.123.103.82")
time.sleep(0.1)
print("Discovered open port 2022/tcp on 92.123.103.82")
time.sleep(0.1)
print("Discovered open port 6129/tcp on 92.123.103.82")
time.sleep(0.1)
print("500/tcp   open  isakmp")
time.sleep(0.1)
print("514/tcp   open  shell")
time.sleep(0.1)
print("545/tcp   open  ekshell")
time.sleep(0.1)
print("554/tcp   open  rtsp")
time.sleep(0.1)
print("2042/tcp  open  csis")
time.sleep(0.1)
print("2048/tcp  open  dls-monitor")
time.sleep(0.1)
print("2049/tcp  open  nfs")
time.sleep(0.1)
print("2065/tcp  open  dlsrpn")
time.sleep(0.1)
print("2099/tcp  open  h2250-annex-g")
time.sleep(0.1)
print("2100/tcp  open  amiganetfs")
time.sleep(0.1)
print("6666/tcp  open  irc")
time.sleep(0.1)
print("6580/tcp  open  parsec-master")
time.sleep(0.1)
print("49400/tcp open  compaqdiag")
time.sleep(0.1)
print("correction done: 1 IP address (1 host up) scanned in 36.06 seconds")
time.sleep(0.1)
print("finished")