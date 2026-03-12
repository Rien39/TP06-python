def tarif(age): 
    if age >= 65:
        print ("senior")
    elif age >=18:
        print ("adulte")
    elif age >=12:
        print ("adolescent ")
    else:
        print ("enfant")
age = int(input("qu'elle est t'on age"))
tarif(age)