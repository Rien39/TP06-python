def connexion(login, mdp):
    if login == "root" and mdp == "py":
        print("connexion réussi")
    elif login != "root" and mdp == "py":
        print("identifiant incorrecte")
    elif login == "root" and mdp != "py":
        print("mots de passe incorrecte")
    else:
        print("connexion échoué")
        
login = input("Entrée l'identifiant")
mdp = input("Entrée le mots de passe")
connexion(login, mdp)