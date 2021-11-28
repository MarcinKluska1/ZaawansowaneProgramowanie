class Library:
    def __init__(self,
                 city: str,
                 street: str,
                 zip_code: str,
                 open_hours: str,
                 phone: str):
        self.city: str = city
        self.street: str = street
        self.zip_code: str = zip_code
        self.open_hours: str = open_hours
        self.phone: str = phone

    def __str__(self):
        return 'city: {}\n' \
               ' street: {}\n' \
               ' zip code: {}\n' \
               ' open hours: {}\n' \
               ' phone: {}\n'.format(self.city,
                                     self.street,
                                     self.zip_code,
                                     self.open_hours,
                                     self.phone)
