from Modele.Nieruchomosc import Nieruchomosc
from Modele.Developer import Developer


class Dom(Nieruchomosc):
    def __init__(self, id: int,
                 developer: Developer,
                 adres: str,
                 metraz: int,
                 cenaZaMetr: int,
                 liczbaPieter: int):
        super().__init__(id, developer, adres, metraz, cenaZaMetr)
        self._liczbaPieter = liczbaPieter

    @property
    def liczbaPieter(self) -> int:
        return self._liczbaPieter

    def __str__(self):
        return f'{super().__str__()};LiczbaPieter: {self._liczbaPieter}\n'
