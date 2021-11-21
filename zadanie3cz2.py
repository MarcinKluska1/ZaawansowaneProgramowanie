class Property:
    def __init__(self, area, rooms: int,  price, address):
        self.area= area
        self.rooms :int = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return 'area: {} \n rooms: {}\n price: {}\n address: {}\n'.format((self.area,self.rooms,self.price,self.address))

class House(Property):
    def __init__(self,area, rooms: int,  price, address, rozmiar_dzialki: int):
        super().__init__(area, rooms, price, address)
        self.rozmiar_dzialki : int = rozmiar_dzialki


    def __str__(self):
        return super(House, self).__str__()+' rozmiar dizalki : {}\n'.format(self.rozmiar_dzialki)

class Flat(Property):
    def __init__(self,area, rooms: int,  price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor : int = floor

    def __str__(self):
        return super(Flat, self).__str__()+' floor: {}\n'.format(self.floor)

