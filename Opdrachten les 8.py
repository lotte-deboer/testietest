# ==========================================
# Opdracht 1:
# Print de tafel van 5 met behulp van een for-loop en een functie (genaamd 'print_tafel_regel').
# De factor en for-loop zijn al gegeven. Schrijf de functie om de regel van de tafel te printen.
#
# Verwachte uitkomst:
# 1  x  5  =  5
# 2  x  5  =  10
# 3  x  5  =  15 enz.
# ==========================================

# factor = 5
# for nummer in range(1,11,1):
#     uitkomst = nummer * factor
#     print(f" {nummer} x {factor} = {uitkomst}")




#------------------------------------------------------------------------------------------
# ==========================================
# Opdracht 2:
# Maak een dobbelsteen met de volgende deelopdrachten.
#
# Opdracht 2a:
# Maak met behulp van de library 'random' een functie die een willekeurig getal tussen 1 en 6 genereert.
# Zorg dat de functie twee argumenten ontvangt, namelijk 'min' en 'max'. Voor het minimum (1) en maximum (6).
# Voer de functie 10 keer uit (met een for-loop). Als het willekeurige getal is gegenereert print je het getal.
#
# Opdracht 2b;
# Maak een variabele aan 'aantal_keer_zes' en zet deze op 0. Schrijf een functie die aan het eind print hoe vaak er een 6 is gegooid.
# De variabele 'aantal_keer_zes' moet in de print statement worden gebruikt.
#
# Verwachte uitkomst (voorbeeld):
# 3 7 2 6 1 4 5 6 2 1
# Er is 2 keer een 6 gegooid
# ==========================================

# import random
# def dobbelsteen(min=1, max=6):
#     return random.randint(min,max)
#
# for aantal in range(1,10):
#     print(dobbelsteen(), end=' ')



# Opdracht 2b
# import random
#
# aantal_keer_zes =  0
#
# for aantal in range(1,11):
#     uitkomst_worp = random.randint(1, 6)
#     dobbelsteen = uitkomst_worp
#     if dobbelsteen == 6:
#         aantal_keer_zes += 1
#
#     print(dobbelsteen, end=' ')
#
# # print("")
# print(f"\nEr is {aantal_keer_zes} keer 6 gegooid")


#--------------------------------------------------------------------------------------
# ==========================================
# Opdracht 3:
# Omrekenen van Fahrenheit naar Celsius. Gegeven zijn temperaturen van drie steden in Fahrenheit.
#
# Schrijf een functie die de temperatuur in Fahrenheit ontvangt als argument en deze omrekent naar Celsius.
# De formule voor de conversie is als volgt: celsius = (fahrenheit - 32) * 5/9
# Schrijf ook een functie die de temperatuur afrond in hele getallen.
# print de temperatuur in Celsius afgerond op hele getallen.
#
# Verwachte uitkomst:
# 18
# 24
# 40
# ==========================================

temp_in_fahr_stockholm = 65
temp_in_fahr_sydney = 75
temp_in_fahr_cairo = 104

# def C(F):
#     return afronden((F - 32) * 5 / 9)
#
# def afronden(F):
#     return (round(F))
#
# print(C(temp_in_fahr_stockholm))
# print(C(temp_in_fahr_sydney))
# print(C(temp_in_fahr_cairo))

def celcius(fahrenheit):
    return afronden((fahrenheit - 32) * 5/9)

def afronden(celcius):
    return (round(celcius))

print(celcius(temp_in_fahr_stockholm))
print(celcius(temp_in_fahr_sydney))
print(celcius(temp_in_fahr_cairo))

