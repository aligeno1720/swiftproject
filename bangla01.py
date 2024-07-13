import getpass
import time
import socket
from datetime import datetime
import sys
from time import sleep

def login():
    dnsserverdomain = input("DNS SERVER DOMAIN : ")
    port = input("PORT : ")
    globalserverip = input("GLOBAL SERVER IP : ")
if __name__ == "__main__":
    login()

time.sleep(3)
def get_current_datetime():
    # Get the current date and time
    now = datetime.now()
    
    # Format the date and time as a string
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    return current_time

if __name__ == "__main__":
    current_time = get_current_datetime()
    print(f"{current_time}")
    
time.sleep(2)

print("")

def progress_bar(iteration, total, prefix='', suffix='', length=30, fill='█'):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()
total_iterations = 100

for i in range(total_iterations + 1):
    time.sleep(0.05)  # Simulate some work
    progress_bar(i, total_iterations, prefix='downloading', suffix='', length=100)

print("//connected")

time.sleep(2)

print("")
def fname(arg):
    pass

black = "\033[0;30m"
purple = "\033[0;35m"
blue = "\033[0;34m"
green = "\033[0;32m"
red = "\033[0;31m"
yellow = "\033[0;33m"
white = "\033[0;37m"

def clear():
	system('clear')

def scrollTxt(text, color, speed):
	if color == "":
		for char in text:
			sys.stdout.write(char)
			sys.stdout.flush()
			sleep(speed)
		print()
	else:
		print(color, end="")
		for char in text:
			sys.stdout.write(char)
			sys.stdout.flush()
			sleep(speed)
		print()
		print(white, end="")

def login():
    transactionreference = input("U-E-T-R : ")
    time.sleep(3)

if __name__ == "__main__":
    login()

time.sleep(2)
def get_current_datetime():
    # Get the current date and time
    now = datetime.now()
    
    # Format the date and time as a string
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    return current_time

if __name__ == "__main__":
    current_time = get_current_datetime()
    print(f"{current_time}")
    
time.sleep(2)
def print_colored(text, color, end='\n'):
    colors = {'red': '\x1b[31m', 'green': '\x1b[32m', 'white': '\x1b[33m', 'blue': '\x1b[34m',}
    reset = '\x1b[0m'
    sys.stdout.write(colors.get(color, '') + text + reset + end)

for i in range(101):
    time.sleep(0.09)
    sys.stdout.write("\r%d%%" % i)
    sys.stdout.flush()


print_colored('// show databases // -----------------------instant type and transmission-----------------------', color='red')

time.sleep(2)

print("")

import time
import sys
from time import sleep

DELAY: float = .05  # Change this to speed up/slow down typewriting speed

def typewrite(*paragraph: str) -> None:
    """This function mimics a typewriting effect by printing strings letter by letter.
    Args:
        *paragraph -- variable length args of sentences to typewrite
    """
    for sentence in paragraph:
        for char in sentence:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(DELAY)
        print()
        sleep(DELAY)
# Usage (you can put as many sentences as you want)
typewrite(
    "SENDER SWIFT CODE        : null",
    "BANK NAME                : DEUTSCHE BANK AG",
    "BANK ADDRESS             : TAUNUSANLAGE 12, 60524 FRANFURT AM MAIN GERMANY",

)

time.sleep(2)

typewrite(
    "RECEIVER SWIFT CODE      : DHBLBDDH",
    "RECEIVER BANK            : DHAKA BANK LIMITED",
    "RECEIVER BANK ADDRESS    : CDA AVENUE BRANCH, CHATTOGRAM,BANGLADESH",
)

time.sleep(2)

typewrite(
    "AMOUNT                   : null",
    "SENDER SWIFT CODE        : null",
    "RECEIVER SWIFT CODE      : DHBLBDDH",

)

print("")

def progress_bar(iteration, total, prefix='', suffix='', length=30, fill='█'):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()

# Example usage
total_iterations = 100

for i in range(total_iterations + 1):
    time.sleep(0.05)  # Simulate some work
    progress_bar(i, total_iterations, prefix='Progress:', suffix='Complete', length=50)

print("\ndownloading completed!")

def get_current_datetime():
    # Get the current date and time
    now = datetime.now()
    
    # Format the date and time as a string
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    return current_time

if __name__ == "__main__":
    current_time = get_current_datetime()
    print(f"{current_time}")
    
time.sleep(2)

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
time.sleep(20)