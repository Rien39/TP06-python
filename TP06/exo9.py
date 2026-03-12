def calculateur(nombre1, nombre2, opérateur):
    if opérateur == "+":
        print (nombre1+nombre2)
    elif opérateur == "-":
        print (nombre1-nombre2)
    elif opérateur == "/":
        print (nombre1/nombre2)
    elif opérateur == "*":
        print (nombre1/nombre2)
nombre1 = int(input("donne moi un premier nombre "))
nombre2 = int(input("donne moi un second nombre "))
opérateur = input("dit moi qu'elle opération veut tu faire ")
calculateur(nombre1, nombre2, opérateur)