import os
import sys
import file
import hashlib
from getpass import getpass

command = ""

verrouille = True
while verrouille:
  
  pswd = getpass("Type password : ")
  entre = entre.encode()
    
  entre_chiffre = hashlib.sha1(entre).hexdigest()
  if entre_chiffre == mot_de_passe_chiffre:
    verrouille = False
  else:
    print("Incorrect password.")
        
print("Mot de passe accepté."

print("PySh v0.1 - A simple and portable Shell in Python and for Python.\nType \"help <command>\" for help.")
while command is not "exit":
  

sys.exit(0)
