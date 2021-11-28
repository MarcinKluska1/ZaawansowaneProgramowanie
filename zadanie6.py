def PolaczListy(lista1: list, lista2: list) -> list:
    lista1.extend(lista2)
    return list(set([i * i * i for i in lista1]))


wynik: list = PolaczListy([1, 2, 1], [4, 5, 6])
for i in wynik:
    print(i)
