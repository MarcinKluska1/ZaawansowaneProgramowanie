from Modele.Developer import Developer


class Nieruchomosc:
    def __init__(self, id: int,
                 developer: Developer,
                 adres: str,
                 metraz: int,
                 cenaZaMetr: int):
        self._id = id
        self._developer = developer
        self._adres = adres
        self._metraz = metraz
        self._cenaZaMetr = cenaZaMetr

    @property
    def id(self) -> int:
        return self._id

    @property
    def developer(self) -> Developer:
        return self._developer

    @property
    def adres(self) -> str:
        return self._adres

    @property
    def metraz(self) -> int:
        return self._metraz

    @property
    def cenaZaMetr(self) -> int:
        return self._cenaZaMetr

    def __str__(self):
        return f'Id: {self._id};' \
               f'Developer: {self._developer};' \
               f'Adres: {self._adres};' \
               f'Metraz: {self._metraz};' \
               f'CenaZaMetr: {self._cenaZaMetr}'
