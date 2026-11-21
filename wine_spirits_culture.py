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
        tasting_price = (self.bottle_price / self.bottle_volume) * tasting_volume
        return tasting_price

