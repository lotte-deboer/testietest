puzzel = ["Albatros", "poncho", "vlinder"]
coordinaten = [(0,0),(2,0),(0,-2),(1,3),(0,3),(2,4),(1,-1)]
letters = []
for woord, letter in coordinaten:
    letters.append(puzzel[woord][letter])

print("".join(letters))







