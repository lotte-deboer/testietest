# p_input = str(input("Schrijf hier je woord waarvan je wilt weten of het een palindroom is:"))
# p_list = []
#
# for letter in p_input:
#     p_list.append(letter)
#
# while len(p_list) >= 1:
#     if p_list[0] == p_list[-1]:
#         p_list.pop(0)
#         p_list.pop(-1)
#         if len(p_list) <= 1:
#             print("Ja palindroom!")
#             break
#     else:
#         print("Nee geen palindroom")
#         break



p_input = str(input("Schrijf hier een zin waarvan je wilt weten of het een palindroom is:"))
p_list = []

for woord in p_input:
    p_list.append(woord)
    print(p_list)

print(p_list)
print(p_list[0])
while len(p_input) >= 1:
    if p_input[0] == p_input[-1]:
        p_input.pop(0)
        p_input.pop(-1)
        if len(p_input) <= 1:
            print("Ja palindroom!")
            break
    else:
        print("Nee geen palindroom")
        break

