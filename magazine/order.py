from magazine.utils import Property


class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor: int = floor

    def __str__(self):
        return super().__str__() + ' floor: {}\n'.format(self.floor)