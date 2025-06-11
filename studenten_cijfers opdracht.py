# students = [("Alice", 8.5), ("Bob", 7.0), ("Charlie", 6.2), ("Diana", 9.1)]
# grades = []
#
# for name in students:
#     print(name[0], end=' - ')
#     print(name[1])
#
# sum_grade = 0
#
# for grade in students:
#     sum_grade += grade[1]
#     grades.append(grade)
#
# def avg():
#     return(round(sum_grade/ len(students),1))
#
# print(f"\nHet gemiddelde van de studenten is ", avg())
#
# highest_grade = max(grades)
#
# print(f"De beste student is {highest_grade[0]} met een cijfer van {highest_grade[1]}!")


# # Toevoegen naam
# print(f"\nSchrijf de naam van student om deze toe te voegen:")
# new_name = input()
# students.append(new_name)
#
# #Toevoegen cijfer
# print(f"\nWelk cijfer heeft {students[-1]}?")
# new_grade = input()
# students.append(new_grade)
#
# #check toevoegen werkt
# print(students)



#Versie 2.0
# Toevoegen naam
# print(f"\nSchrijf de naam van student om deze toe te voegen:")
# new_name = input()
# print(f"\nWelk cijfer heeft {new_name}?")
# new_grade = input()
# students.append((new_name, new_grade))
#
# print(students)

# zoeken op student

# search = str(input(f"Van welke student wil je het cijfer zien?\n"))
#
# if search in students:
#     print(grades)
#
# result = search in students
# print(result)

#Versie 2.0
# search_input = str(input(f"Van welke student wil je het cijfer zien?\n"))
# [(name, grade) for name in students if name[0] == search_input]
# print(grade[1])



# Sorteer de lijst op cijfers
# for cijfer,name in students:
#
#
# print(cijfer)

# sorted_grades = sorted(cijfer)
# print(sorted_grades)