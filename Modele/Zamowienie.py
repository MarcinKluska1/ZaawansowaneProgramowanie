from Modele.Nieruchomosc import Nieruchomosc
from typing import List


class Zamowienie:
    def __init__(self, id: int,
                 nieruchomosci: List[Nieruchomosc],
                 kraj: str,
                 nazwaKlienta: str):
        self._id = id
        self._nieruchomosci = nieruchomosci
        self._kraj = kraj
        self._nazwaKlienta = nazwaKlienta

    @property
    def id(self) -> int:
        return self._id

    @property
    def nieruchomosc(self) -> List[Nieruchomosc]:
        return self._nieruchomosci

    @property
    def kraj(self) -> str:
        return self._kraj

    @property
    def nazwaKlienta(self) -> str:
        return self._nazwaKlienta

    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @nieruchomosc.setter
    def nieruchomosci(self, value: List[Nieruchomosc]) -> None:
        self._nieruchomosci = value

    @kraj.setter
    def kraj(self, value: str) -> None:
        self._kraj = value

    @nazwaKlienta.setter
    def nazwaKlienta(self, value: str) -> None:
        self._nazwaKlienta = value

    def wartoscZamowienia(self) -> float:
        wartosc: float = 0
        for i in self._nieruchomosci:
            wartosc += i.cenaZaMetr * i.metraz
        return round(wartosc, 2)

    def __str__(self):
        return f'Id: {self._id}\n' \
               f'Nieruchomosci:' \
               f' {[i.__str__() for i in self._nieruchomosci]}\n' \
               f'Kraj: {self._kraj}\n' \
               f'Nazwa klienta: {self._nazwaKlienta}\n' \
               f'Wartosc zamowienie: {self.wartoscZamowienia()}'
