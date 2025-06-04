# lijst = [1, 5, 7, 12]
# print(lijst)
# print(type(lijst))
#
# lege_lijst = []
# print(lege_lijst)

#gebruik index om specifieke locaties aan te spreken. Begint bij 0. Werkt alleen met hele waardes.
# print(lijst[0])
# print(lijst[1])

#vanaf achtere indexeren
# print(lijst[-1])
# print(lijst[-2])

# check of waarde in je list zit
list = [1, 2, 3, 4, 5]
# print(2 in list)
# print(6 in list)
# print(6 not in list)

# zoeken eerste voorkomende waarde zoeken op welke index het staat. index(X)
# print(list.index(3))

# aantal elementen opvragen. len(X)
# print(len(list))

# waarde wijzigen. Geef index en daarna waarde die je wilt.
# list[0] = 10
# print(list)
#
# print(list[1] + list[2])

# Hele lijst optellen
# print(sum(list))

# of

# sum_list = 0
# for x in list:
#     sum_list = sum_list + x
# print(sum_list)

#Toevoegen aan einde vd list
list.append(6)
print(list)

#meerdere waardes toevoegen aan einde vd list
list.extend([7, 8, 9, 10])
print(list)

#2 lists samenvoegen
list2 = [11, 12]
print(list + list2)

#list repeaten
print(list2 *3)

#toevoegen op specifieke index
list2.insert(1, 13)
print(list2)

#verwijderen
list2.remove(13)
print(list2)

#meerdere keren die waarden verwijderen uit de hele lijst met for loop

#verwijderen op index
del list2[0]
print(list2)

#automatisch list aanmaken met specifieke range
# range1 = 1
# range2 = 10
# list_range = list(range(range1,range2))
# print(list_range)

# omdraaien list
list2.extend([13,14,15,16])
list2.reverse()
print(list2)

#sorteren
list2.sort()
print(list2)

