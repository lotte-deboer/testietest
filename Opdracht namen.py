list_names = ['lotte', 'erik', 'atlas', 'yue', 'boots']
eind_names = []



def hoofdletter_actie(lijst):
    eind_names[::] = lijst[-1:]
    list_names[::] = lijst[:-1]
    return ([name.capitalize() for name in lijst])


samen_names = ",".join(hoofdletter_actie(list_names))
samen_eind_names = "".join(hoofdletter_actie(eind_names))


print(f"Dit is de lijst met namen:", samen_names ,"en", samen_eind_names)

