def Powitanie(name: str, surname: str) -> str:
    return 'Cześć {} {}'.format(name, surname)


wynikPowitania: str = Powitanie('Marcin', 'Kluska')
print(wynikPowitania)
