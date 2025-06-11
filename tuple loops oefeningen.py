# Schrijf een programma dat de tafel van een getal afdrukt.
# De gebruiker voert een getal in en het programma drukt de tafel van dat getal af.
# De tafel van 7 ziet er bijvoorbeeld als volgt uit:
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70

# Probeer het eerst zonder loop,
# print(f"{invoer_getal} X 1=", invoer_getal*1)
# print(f"{invoer_getal} X 2=", invoer_getal*2)
# print(f"{invoer_getal} X 3=", invoer_getal*3)
# print(f"{invoer_getal} X 4=", invoer_getal*4)
# print(f"{invoer_getal} X 5=", invoer_getal*5)
# print(f"{invoer_getal} X 6=", invoer_getal*6)
# print(f"{invoer_getal} X 7=", invoer_getal*7)
# print(f"{invoer_getal} X 8=", invoer_getal*8)
# print(f"{invoer_getal} X 9=", invoer_getal*9)
# print(f"{invoer_getal} X 10=", invoer_getal*10)


# Probeer het nu met een loop.
# invoer_getal = int(input('Schrijf hier je cijfer '))
# for getal in range(1,11):
#     print(f"{invoer_getal} x {getal} =", invoer_getal * getal)


#-------------------------------------------------------------------------------
# Optellen
# Schrijf een programma dat de som van alle getallen tot een bepaalde limiet berekent.
# getal = (1,5,8,9,10,12,9,15)
# som_getal = sum(getal)
# if som_getal < 100:
#     print(som_getal)
#
# else:
#     print("Buiten Limiet")

# cijfers = sum(range(1,10))
# print(cijfers)

# cijfer = 1
# for C in cijfer:
#     cijfer = cijfer + 1
#
#     if sum(cijfer) < 20:
#         print("check")
#
#     else:
#         print("not check")


# Bijvoorbeeld: de som van alle getallen tot 3 is 6 (1 + 2 + 3 = 6)


#--------------------------------------------------------------
# Dit is een klassieke programmeeroefening die vaak wordt gebruikt in sollicitatiegesprekken.
# FizzBuzz

# Schrijf een programma dat de getallen van 1 tot 100 afdrukt.
# Maar voor veelvouden van drie, druk "Fizz" af in plaats van het getal.
# En voor veelvouden van vijf, druk "Buzz" af.
# Voor veelvouden van zowel drie als vijf, druk "FizzBuzz" af.


# for getal in range(1,101):
#
#     if getal % 3 == 0:
#
#         if getal % 5 ==0:
#             print("FizzBuzz")
#         else:
#             print("Fizz")
#
#     elif getal % 5 ==0:
#         print("Buzz")
#
#     else:
#         print(getal)



#-----------------------------------------
# Fibonacci-reeks

# De eerste twee getallen van de Fibonacci-reeks zijn 0 en 1.
# Elk volgend getal is de som van de twee voorgaande.
# De eerste 10 getallen van de Fibonacci-reeks zijn:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# 0A + 1B = 1X
# 1X + 1B = 2
# 1 + 2 = 3
# 2 + 3 = 5
# 3 + 5 = 8
# 5 + 8 = 13
# 8 + 13 = 21
# 13 + 21 = 34

i = int(input("Hoeveel Fibonacci-getallen wil je zien? "))

a = 0
b = 1
fgetal = [0,1]
for x in range(i-2):
    fgetal.append(fgetal[-1] + fgetal[-2])
print(fgetal)




