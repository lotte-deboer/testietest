# nieuwe_set = {'Rood', 'Wit','Blauw'}
# print(nieuwe_set)
#
# lege_set = set()
# print(lege_set)
# print(type(lege_set))
#
# lege_dictionary = {}
# print(lege_dictionary)
# print(type(lege_dictionary))
#
# getal_voorbeeld = set(range(1,11))
# print(getal_voorbeeld)
#
# set_lijst = set([1,2, "Rood", "Wit", "Blauw",100])
# print(set_lijst)

#Dubbele elementen worden automatisch verwijderd.
# dubbele_lijst = set([1,2, "Rood","Rood", "rood", "Wit", "Blauw",100])
# print(dubbele_lijst)
#
# # Zit element in set. In or not in
# print('Rood', 'Rood' in dubbele_lijst)
# print('Rood', 'Rood' not in dubbele_lijst)
#
# #aantal elementen in set
# print(len(dubbele_lijst))
#
# #toevoegen
# dubbele_lijst.add('Paars')
# print(dubbele_lijst)
#
# #verwijderen
# dubbele_lijst.remove('Wit')
# dubbele_lijst.remove('Blauw')
# dubbele_lijst.remove(100)
# dubbele_lijst.remove('rood')
# print(dubbele_lijst)
#
# #hele verzameling leeg maken
# dubbele_lijst.clear()
# print(dubbele_lijst)

#benaderen met index niet mogelijk
#hele set benaderen met for statement
# lijst = {"Dit", "Dat"}
# for l in lijst:
#     print(l.upper(), end= ' | ')

#frozenset = set die na aanmaak niet kan worden aangepast. Toevoegen kan wel, veranderen niet.
# frozen_lijst = frozenset({'dit', 'dat'})
# print(frozen_lijst)

#check of set onderdeel is van een andere sets.
# set1 = {'Dit', 'Dat', 'Daarom'}
# set2 = {'Dit', 'Daarom'}
# print(set2 <= set1)
# print(set1 <= set2)
#
# #andere methode om hetzelfde te checken.
# print(set2.issubset(set1))
#set1 is de superset, set2 is de deelverzameling
# print(set1.issuperset(set2))
# print(set2.issuperset(set1))

#2 sets samenvoegen
# set3 = set1 | set2
# print(set3)

#andere samenvoeg methode
# set4 = set1.union(set2)
# print(set4)

#Komt het voor in beide sets? Check welke elementen in beide voorkomen.
# check_beide = set1 & set2
# print(check_beide)

#andere methode check of in beide sets/list/ ect voorkomen
# check_beide2 = set1.intersection(set2)
# print(check_beide2)

#verschil tussen 2. Wel in A niet in B
# verschil_set = set1 - set2
# print(verschil_set)
#
# verschil_set2 = set1.difference(set2)
# print(verschil_set2)

#symetrisch verschil,of in A of in B voorkomen
# s_verschil = set1 ^ set2
# print(s_verschil)

# of zo
# s_verschil2 = set1.symmetric_difference(set2)
# print(s_verschil2)

# |=  A + B. Waarbij B wordt toegevoegd aan A
# &=
# -=
# ^=

# getallen = [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 10]
# even_getallen = {getal for getal in getallen if getal % 2 == 0}
# print(even_getallen)

