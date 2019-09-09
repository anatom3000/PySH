while true_password:
  pswd = getpass("Type password : ")
  entre = entre.encode()
    
  entre_chiffre = hashlib.sha1(entre).hexdigest()
  if entre_chiffre == mot_de_passe_chiffre:
    verrouille = False
  else:
    print("Incorrect password.")
        
print("Mot de passe accepté.")
