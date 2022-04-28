import datetime as gf
import platform as ind
import time as count
import pyfiglet as fig
import socket as socks
from cd import Modulss
from cd import Login
import requests

class Colors:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
logo = fig.figlet_format('     T O O L S')
print(logo)
print("                             "+Modulss.usr+"\n")

print("[1] Check system")
print("[2] Scan ip address")
print("[3] Denial of service")
print("[4] Inject website code")
try:
  select_items = int(input("Select> "))

  if select_items == 1:
    count.sleep(2)
    print("[*] Payload...")
    count.sleep(2)
    print("[*] Checking...")
    count.sleep(2)
    print("[*] Show System...")
    count.sleep(2)

    checking = str(input("Are you sure want to continue Y/N "))
    count.sleep(2)
    if checking == 'y':
     systems = ind.system()
     print("System: "+Colors.BOLD+systems+Colors.END)
    elif checking == 'Y':
     systems = ind.system()
     print("System: "+Colors.BOLD+systems+Colors.END)
    elif checking == 'n':
      exit()
    elif checking == 'N':
      exit()
    elif checking == '':
     systems = ind.system()
     print("System: "+Colors.BOLD+systems+Colors.END)
  elif select_items == 2:
    url = input("Target: ")
    scans = socks.gethostbyname(url)
    count.sleep(3)
    print("Ip address:"+Colors.BOLD+scans+Colors.END)
  elif select_items == 3:
    url_target = input("Url target: ")
    host = socks.gethostbyname(url_target)
    if host == True:
      count.sleep(3)
    limits = int(input("Limit: "))
    for randoms in range(limits):
      print("Sending packet: ",url_target,randoms)
    else:
      exit()
  elif select_items > 4:
    print("Not found!")
  elif select_items == 4:
    try:
     urls = input("Target: ")
     scanning_url = requests.get(urls)
     print(scanning_url.text)
    except:
      print("Host only")
except:
  exit()
