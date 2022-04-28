import random
class Login:
  username = "admin"
  password = "12345"
  
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
class Modulss:
  usr = "Created by "+Colors.BOLD+"Mr.Cryptix"+Colors.END
  
class Hello:
  Bolds =Colors.BOLD
  randoms = random.randrange(1000)
  print(f"ID LOGIN:{Bolds} {randoms}"+Colors.END)