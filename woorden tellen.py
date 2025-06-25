zin = "dit is een testzin om te testen of dit programma werkt hallo hallo "
zin_gebruikers = str(input("Schrijf hier je zin, waarvan je het aantal woorden wilt weten:"))

def aantal_woorden(x):
    return(len(x.split()))

print(aantal_woorden(zin))
print(aantal_woorden(zin_gebruikers))