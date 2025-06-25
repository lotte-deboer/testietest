alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
code = []
oplossing = []


def encrypt(woord, number):
    position = 0
    for letter in woord:
        l_index = alphabet.index(letter)
        code.insert(position,alphabet[l_index + number])
        position += 1
        # print("location index", l_index)
        # print("letter", letter)
        # print("position", position)
        # print("number", number)

    return (woord)

def decrypt(woord, number):
    position = 0
    for letter in woord:
        l_index = alphabet.index(letter)
        oplossing.insert(position,alphabet[l_index - number])
        position += 1
        # print("location index", l_index)
        # print("letter", letter)
        # print("position", position)
        # print("number", number)

    return (woord)


while True:

    menu = int(input("Keuze menu Caesar Cipher\n\n"
                     "Kies 1 voor encoderen\n"
                     "Kies 2 voor decoderen\n"
                     "Kies 3 om het menu te sluiten\n"))

    if menu == 1:
        e_input = str(input("Schrijf hier het woord wat je wilt encrypten:\n"))
        s_number = int(input("Schrijf het nummer van hoeveel letters je wilt laten verschuiven.\n"))
        encrypt(e_input, s_number)
        print(''.join(code))
        terug = str(input("Wil je terug naar het menu? Ja of Nee\n"))

        if terug == "Ja":
            continue

        elif terug == "Nee":
            break


    elif menu == 2:
        d_input = str(input("Schrijf hier het woord wat je wilt ontcijferen:\n"))
        d_number = int(input("Schrijf het nummer van hoeveel letters je wilt laten verschuiven.\n"))
        decrypt(d_input, d_number)
        print(''.join(oplossing))
        terug = str(input("Wil je terug naar het menu? Ja of Nee\n"))

        if terug == "Ja":
            continue

        elif terug == "Nee":
            break

    elif menu == 3:
        break

    continue




#iteratief process
# code_samen = []
# def encrypt(woord, number):
#     for letter in woord:
#         code.append(letter)
#
#     return(woord)


# def encrypt(woord, number):
#     for letter in woord:
#         if letter in alphabet:
#             code.insert(number,alphabet[number])
#             number = number +1
#
#     return (woord)

# def encrypt(woord, number):
#     position = 0
#     for letter in woord:
#         if letter in alphabet:
#             code.insert(position,alphabet[number])
#             number += 1
#             position += 1
#             print("position", position)
#             print("number", number)
#     return (woord)