class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms: int = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return 'area: {} \n rooms: {}\n price: {}\n address: {}\n'.format(
            self.area, self.rooms, self.price, self.address)
