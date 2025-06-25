# #eigenschappen:
# - Geen specifieke volgorde
# - Geen index
# - Key + value = een pair
# -  datatype: int, float, str
#
# key = 'Naam': x
# key = 2018: verhuizing, baan

# nieuwe_dictionary = {'Voorbeeld':'dit', 'Ander_voorbeeld':1}
# print(nieuwe_dictionary)
#
# leeg_dict = {}

#Dict kan je ook maken met de dic functie, dan ziet de aanmaak er wat anders uit!

# Vergelijken met elkaar, alleen true als key en value exact hetzelfde is als andere key en value. De volgorde maakt hierbij niet uit.
# print(nieuwe_dictionary == leeg_dict)

# check of key in dict zit.
# nieuwe_dictionary = {'Voorbeeld':'dit', 'Ander_voorbeeld':1}
# print('Voorbeeld' in nieuwe_dictionary)
# print('Voorbeeld' not in nieuwe_dictionary)
#
# if 'Voorbeeld' in nieuwe_dictionary:
#     print("Ja")
# else:
#     print("Nee")

# Elke sleutel moet uniek zijn. Als je 2 keer zelfde key aanmaakt, vervangt het de eerste key met de pair van de volgende input.


# lengte
# dict = {'Huis': 1, 'Straat':['naam1', 'naam2'], 'Stad': 'Amsterdam'}
# print(dict)
# print(len(dict))
#
# len(naam_dict)


# Richten op specifiek key pair in dict.
# print(dict['Straat'])


# Opzoeken of waarde erin zet, anders none melding
# print(dict.get('Straat'))
# print(dict.get('Strat'))
# # zelf melding schrijven als het niet voorkomt in de dict
# print(dict.get('Strat', 'Staat er niet in'))


# Waarde pair veranderen of toevoegen
# dict['Stad'] = 'Utrecht'
# print(dict)
#
# dict['Land'] = 'Nederland'
# print(dict)


# Andere methode add of update
# dict.update(Stad = 'Leiden')
# print(dict)

# Verwijderen
# del dict['Stad']
# print(dict)

#loopen in een dictionary
# for x in dict:
#     dict.update(Land = 'nederland')
#     print(dict)
#
# for key in dict.items():
#     if x == 'nederland':
#         print(dict)


# voorbeeld_dict = {'Kat':2, 'Huis':1, 'Fietsen': 4}
# for key,value in voorbeeld_dict.items():
#     if value > 1:
#         value += 1
#         voorbeeld_dict ['Huis'] = 5
#         print(key,value)

#Alleen selecteren keys of values
# print(voorbeeld_dict.keys())
# print(voorbeeld_dict.values())

#hele set selecteren is .items()

#dict veranderen naar set om duplicates eruit te halen. met set(naam dict)

#een dict veranderen naar een list
# dic_list = list(voorbeeld_dict.values())
# print(dic_list)
# print(dic_list[0])

# student_grades = {'Erik': [2.3, 8, 6.4, 1], 'Lotte':[3.3, 5.6, 7.4, 9.1], 'Atlas':[1, 3]}
# final_grade = {student: round(sum(grades)/len(grades),1) for student,grades in student_grades.items()}
# for name, grade in final_grade.items():
#     if grade < 5.5:
#         final_grade[name] = 5.5
#
# print(final_grade)