def czyParzysta(liczba: int) -> bool:
    return not bool(liczba % 2)


wynikCzyParzysta: bool = czyParzysta(44)
if (wynikCzyParzysta):
    print('Liczba parzysta')
else:
    print('Liczba nieparzysta')
