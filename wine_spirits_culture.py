import re


def is_valid_bottle_code(code):
    pattern = r"ITAL-\d{4}"
    return re.fullmatch(pattern, code) is not None


class Beverage:

    def __init__(self, code, name, origin, bottle_volume, bottle_price):
        self.code = code
        self.name = name
        self.origin = origin
        self.bottle_volume = bottle_volume
        self.bottle_price = bottle_price

    def calculate_tasting_price(self, tasting_volume):
        kostolo_ar = (self.bottle_price / self.bottle_volume) * tasting_volume
        return kostolo_ar


class Wine(Beverage):

    def __init__(self, code, name, origin, bottle_volume, bottle_price, grape_variety, vintage):
        super().__init__(code, name, origin, bottle_volume, bottle_price)
        self.grape_variety = grape_variety
        self.vintage = vintage
        self.tasting_volume = 100

    def calculate_tasting_price(self):
        return super().calculate_tasting_price(self.tasting_volume)

    def describe(self):
        return (
            f"Azonosító: {self.code}, "
            f"Név: {self.name}, "
            f"Származás: {self.origin}, "
            f"Palackméret: {self.bottle_volume} ml, "
            f"Palackár: {self.bottle_price} Ft, "
            f"Szőlőfajta: {self.grape_variety}, "
            f"Évjárat: {self.vintage}"
        )


class Palinka(Beverage):

    def __init__(self, code, name, origin, bottle_volume, bottle_price, fruit):
        super().__init__(code, name, origin, bottle_volume, bottle_price)
        self.fruit = fruit
        self.tasting_volume = 20

    def calculate_tasting_price(self):
        return super().calculate_tasting_price(self.tasting_volume)

    def describe(self):
        return (
            f"Azonosító: {self.code}, "
            f"Név: {self.name}, "
            f"Származás: {self.origin}, "
            f"Palackméret: {self.bottle_volume} ml, "
            f"Palackár: {self.bottle_price} Ft, "
            f"Gyümölcs: {self.fruit}"
        )
