from magazine.utils import Property

class House(Property):
    def __init__(self, area, rooms: int, price, address, rozmiar_dzialki: int):
        super().__init__(area, rooms, price, address)
        self.rozmiar_dzialki: int = rozmiar_dzialki

    def __str__(self):
        return super() \
                   .__str__() + ' rozmiar dizalki : {}\n' \
                   .format(self.rozmiar_dzialki)