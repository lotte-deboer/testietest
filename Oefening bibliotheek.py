#List1

# print(set_groep1)
# print(set_groep2)
#vraag1
# print(f"Wel in set 1 niet in set 2", set_groep1 - set_groep2)
# print(f"\nWel in set 2 niet in set 1", set_groep2 - set_groep1)

#vraag2
# print(f"\nBoeken die geleend zijn door beide groepen", set_groep1 & set_groep2)

#vraag3
# vraag3 = set_groep1.difference(set_groep2)
# print(f"\nGeleend door groep 1 en niet door groep2, {vraag3}")
# vraag3b = set_groep2.difference(set_groep1)
# print(f"\nWel geleend door groep 2 maar niet door groep 1, {vraag3b}")

#List2
list_groep1 = ["Harry Potter", "De Hobbit", "De Da Vinci Code", "De Hobbit", "De Da Vinci Code", "Twilight",
          "De Vijfde Golf", "Harry Potter", "De Hobbit"]
list_groep2 = ["De Da Vinci Code", "De Alchemist", "Harry Potter", "De Hobbit", "Twilight", "The Hunger Games",
          "Gone Girl", "Twilight", "De Hobbit"]


set_groep1 = set(list_groep1)
set_groep2 = set(list_groep2)

#vraag4

dict_groep1 = {}
for boeknaam in set_groep1:
    hoevaak = list_groep1.count(boeknaam)
    dict_groep1[boeknaam] = hoevaak
print(dict_groep1)

dict_groep2 = {}
for boeknaam in set_groep2:
    hoevaak =  list_groep2.count(boeknaam)
    dict_groep2[boeknaam] = hoevaak
# print(dict_groep2)

aantal_geleend = 0
meestboek = ''
for boek, aantal in dict_groep1.items():
    if aantal > aantal_geleend:
        aantal_geleend = aantal
        meestboek = boek

print(meestboek)





#Mijn poging
#Maak dict groep1. boeken zijn keys
# dict_boek = {}
# for boek, aantal in list_groep1:
#     boek.append(+= boek)
#     aantal = len(boek)
# print(boek)
# print(aantal)



