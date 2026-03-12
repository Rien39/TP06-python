def verifier_majorite(age):
    if age >= 18:
        print("majeur")
    else:
        print("mineur")
age = int(input("qu'elle est t'on age"))
verifier_majorite(age)