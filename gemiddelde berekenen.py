grades = {"Java": 7, "Python": 8, "C#": 6, "HTML": 9, "CSS": 8}

def gem(x):
    list = grades.values()
    return(sum(list) / len(list))

print(gem(grades))


