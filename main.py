from typing import List


class Magazyn:
    def __init__(self, id_magazynu: int, nazwa_magazynu: str, adres: str, powierzchnia: int, typ_magazynu: str):
        self._id_magazynu = id_magazynu
        self._nazwa_magazynu = nazwa_magazynu
        self._adres = adres
        self._powierzchnia = powierzchnia
        self._typ_magazynu = typ_magazynu

    @property
    def id_magazynu(self) -> int:
        return self._id_magazynu

    @property
    def nazwa_magazynu(self) -> str:
        return self._nazwa_magazynu

    @property
    def adres(self) -> str:
        return self._adres

    @property
    def powierzchnia(self) -> int:
        return self._powierzchnia

    @property
    def typ_magazynu(self) -> str:
        return self._typ_magazynu

    def __str__(self) -> str:
        return f'{self._id_magazynu},{self._nazwa_magazynu};{self._adres};{self._powierzchnia};{self._typ_magazynu}'


class Produkt:
    def __init__(self, cena: int, nazwa: str, data_produkcji, magazyn: Magazyn, marka: str):
        self._cena = cena
        self._nazwa = nazwa
        self._data_produkcji = data_produkcji
        self._magazyn = magazyn
        self._marka = marka

    @property
    def cena(self) -> int:
        return self._cena

    @property
    def nazwa(self) -> str:
        return self._nazwa

    @property
    def data_produkcji(self) -> str:
        return self._data_produkcji

    @property
    def magazyn(self) -> Magazyn:
        return self._magazyn

    @property
    def marka(self) -> str:
        return self._marka

    def __str__(self) -> str:
        return f'{self._cena},{self._nazwa};{self._data_produkcji};{self._magazyn};{self._marka}'


class Klient:
    def __init__(self, id_klienta: int, adres: str, numer_telefonu: str, kraj: str, karta_stalego_klienta: bool):
        self._id_klienta = id_klienta
        self._adres = adres
        self._numer_telefonu = numer_telefonu
        self._kraj = kraj
        self._karta_stalego_klienta = karta_stalego_klienta

    @property
    def id_klienta(self) -> int:
        return self._id_klienta

    @property
    def adres(self) -> str:
        return self._adres

    @property
    def numer_telefonu(self) -> str:
        return self._numer_telefonu

    @property
    def kraj(self) -> str:
        return self._kraj

    @property
    def karta_stalego_klienta(self) -> bool:
        return self._karta_stalego_klienta

    def __str__(self) -> str:
        return f'{self._id_klienta};{self._adres};{self._numer_telefonu},{self._kraj},{self._karta_stalego_klienta}'


class KlientDetaliczny(Klient):
    def __init__(self, id_klienta: int, adres: str, numer_telefonu: str, kraj: str, karta_stalego_klienta: bool,
                 imie_nazwisko: str):
        super().__init__(id_klienta, adres, numer_telefonu, kraj, karta_stalego_klienta)
        self._imie_nazwisko = imie_nazwisko

    @property
    def imie_nazwisko(self) -> str:
        return self._imie_nazwisko

    def __str__(self) -> str:
        return f'{super().__str__()};{self._imie_nazwisko}'


class KlientBiznesowy(Klient):
    def __init__(self, id_klienta: int, adres: str, numer_telefonu: str, kraj: str, nazwa_firmy: str,
                 karta_stalego_klienta: bool):
        super().__init__(id_klienta, adres, numer_telefonu, kraj, karta_stalego_klienta)
        self._nazwa_firmy = nazwa_firmy

    @property
    def nazwa_firmy(self) -> str:
        return self._nazwa_firmy

    def __str__(self) -> str:
        return f'{super().__str__()};{self._nazwa_firmy}'


class Zamowienie:
    @property
    def id_zamowienia(self) -> int:
        return self._id_zamowienia

    @id_zamowienia.setter
    def id_zamowienia(self, value: int) -> None:
        self._id_zamowienia = value

    @property
    def klient(self) -> Klient:
        return self._klient

    @klient.setter
    def klient(self, value: Klient) -> None:
        self._klient = value

    @property
    def produkty(self) -> List[Produkt]:
        return self._produkty

    @produkty.setter
    def produkty(self, value: List[Produkt]) -> None:
        self._produkty = value

    @property
    def data_realizacji(self) -> str:
        return self._data_realizacji

    @data_realizacji.setter
    def data_realizacji(self, value: str) -> None:
        self._data_realizacji = value

    @property
    def data_zamowienia(self) -> str:
        return self._data_zamowienia

    @data_zamowienia.setter
    def data_zamowienia(self, value: str) -> None:
        self._data_zamowienia = value

    def __str__(self) -> str:
        return f'Id zamowienia: {self._id_zamowienia}\nKlient: {self._klient}\nLista produktow: {[i.__str__() for i in self._produkty]}\nData realizacji: {self._data_realizacji}\nData zamowienia: {self._data_zamowienia}\n'

    def wartoscZamowienia(self) -> float:
        wartosc: float = 0
        for i in self._produkty:
            wartosc += i.cena
        wartosc = wartosc + wartosc * 0.23  # zakładając że VAT na elektronikę wynosi 23%
        return round(wartosc, 2)

    def adresKlienta(self) -> str:
        return self._klient.adres


zbyszek: KlientDetaliczny = KlientDetaliczny(2, 'adres', '666-666-666', 'Polska', True, 'Zbyszek Wodecki')
magazyn_produktow: Magazyn = Magazyn(3, 'magazyn', 'polna 2', 5, 'zwykly')
zamowione_produkty: List[Produkt] = [Produkt(5, 'podzespol1', '20-03-2-20', magazyn_produktow, 'marka1'),
                                     Produkt(3, 'podzespol2', '20-03-2-20', magazyn_produktow, 'marka2'),
                                     Produkt(6, 'podzespol3', '20-03-2-20', magazyn_produktow, 'marka3')]

nowe_zamowienie: Zamowienie = Zamowienie()
nowe_zamowienie.id_zamowienia = 3
nowe_zamowienie.klient = zbyszek
nowe_zamowienie.produkty = zamowione_produkty
nowe_zamowienie.data_realizacji = '20-03-2-20'
nowe_zamowienie.data_zamowienia = '20-03-2-20'

print(nowe_zamowienie)
print(nowe_zamowienie.wartoscZamowienia())
print(nowe_zamowienie.adresKlienta())
