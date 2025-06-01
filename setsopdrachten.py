# ==========================================
# Opgave 2:
# Gegeven de verzamelingen {red, blue, green} en {yellow, blue, green}
# Zoek uit met behulp van wiskundige verzamelingsoperatoren of methodes:
# - Welke kleur zit wel in verzameling_kleuren_1 maar niet in verzameling_kleuren_2?
# - Welke kleuren zitten niet in beide sets? ('red' en 'yellow')
#
# Print de resultaten.
# ==========================================
# kleurset1 = {'red', 'blue', 'green'}
# kleurset2 = {'yellow', 'blue', 'green'}
# verschil = kleurset1 - kleurset2
# beide = kleurset1.symmetric_difference(kleurset2)
# print(beide)
# print(kleurset1)
# print(kleurset2)
# print(verschil)

#opdracht 3
# Opgave 3:
# Gegeven de verzamelingen {11, 22, 33} en {5, 11, 16, 22}
# Gebruik wiskundige verzamelingsoperatoren om de volgende verzamelingen te printen:
#     {33}
#     {5, 16}
#     {5, 11, 16, 22, 33}
#     {11, 22}
#
# (LET OP: De volgorde van de values in de verzamelingen is niet belangrijk, die kan namelijk veranderen omdat een set unordered is.)
# ==========================================

# v1 = {11, 22, 33}
# v2 = {5, 11, 16, 22}
# opdracht1 = v1.difference(v2)
# print(opdracht1)
#
# opdracht2 = v2.difference(v1)
# print(opdracht2)
#
# opdracht3 = v1 | v2
# print(opdracht3)
#
# opdracht4 = v1 & v2
# print(opdracht4)

# ==========================================
# Opgave 1:
# Gegeven de verzameling {3, 44, 17, 23, 58, 9, 36}
# Voer de volgende opdrachten uit:
# - Voeg de value 27 aan de verzameling toe.
# - Verwijder de value 23 uit de verzameling.
# - Druk alle values in de verzameling tussen 20 en 50 af. Gebruik hiervoor een for loop.
#
# Verwachte uitkomst: 36, 27, 44
# ==========================================

v = {3, 44, 17, 23, 58, 9, 36}
v.add(27)
# print(v)
v.remove(23)
# print(v)
for value in  v:
    if value >= 20 and value <=50:
        print(value)