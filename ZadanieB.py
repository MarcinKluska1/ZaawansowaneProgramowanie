def PomnozLiczby(liczby: list):
    wynik: list = []
    for liczba in liczby:
        wynik.append(liczba * 2)
    return wynik


def PomnozLiczbyAleInaczej(liczby: list):
    return [i * 2 for i in liczby]
