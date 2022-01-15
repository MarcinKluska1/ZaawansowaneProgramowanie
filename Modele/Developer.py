class Developer:
    def __init__(self, id: int, adres: str, telefon: str, nazwaFirmy: str):
        self._id = id
        self._adres = adres
        self._telefon = telefon
        self._nazwaFirmy = nazwaFirmy

    @property
    def id(self) -> int:
        return self._id

    @property
    def adres(self) -> str:
        return self._adres

    @property
    def telefon(self) -> str:
        return self._telefon

    @property
    def nazwaFirmy(self) -> str:
        return self._nazwaFirmy

    def __str__(self):
        return f'Id: {self._id};' \
               f'Adres: {self._adres};' \
               f'Telefon: {self._telefon};' \
               f'Nazwa firmy: {self._nazwaFirmy}'
