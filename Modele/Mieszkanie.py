from Modele.Nieruchomosc import Nieruchomosc
from Modele.Developer import Developer


class Mieszkanie(Nieruchomosc):
    def __init__(self, id: int,
                 developer: Developer,
                 adres: str,
                 metraz: int,
                 cenaZaMetr: int,
                 pietro: int):
        super().__init__(id, developer, adres, metraz, cenaZaMetr)
        self._pietro = pietro

    @property
    def pietro(self) -> int:
        return self._pietro

    def __str__(self):
        return f'{super().__str__()};Pietro: {self._pietro}\n'
