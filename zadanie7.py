import pandas

class Brewery:
    def __init__(
            self,
            id: int,
            name: str,
            brewery_type: str,
            street: str,
            adress_2,
            adress_3,
            city: str,
            state:str,
            county_province,
            postal_code: str,
            country:str,
            longitude:str,
            latitude:str,
            phone:str,
            website_url:str,
            updated_at:str,
            created_at:str):
        self.id: int= id
        self.name: str=name
        self.brewery_type: str= brewery_type
        self.street: str = street
        self.adress_2 =adress_2
        self.adress_3 = adress_3
        self.city: str = city
        self.state: str = state
        self.county_province = county_province
        self.postal_code: str = postal_code
        self.country: str = country
        self.longitude: str = longitude
        self.latitude: str = latitude
        self.phone: str = phone
        self.website_url: str = website_url
        self.updated_at: str = updated_at
        self.created_at: str = created_at

    def __str__(self):
        return

