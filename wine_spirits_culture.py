import re


# 1. FELADAT - ITALAZONOSITO ELLENORZESE

def is_valid_bottle_code(code):
    pattern = r"ITAL-\d{4}"
    return re.fullmatch(pattern, code) is not None


# 2. FELADAT - ALAPOSZTALY

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


# 3. FELADAT - BOR OSZTALY

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


# 3. FELADAT - PALINKA OSZTALY

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


# 4. FELADAT - KOSTOLO REGISZTRALASA

def register_tasting(ital):
    kostolo_ar = ital.calculate_tasting_price()
    return ital, kostolo_ar


# 4. FELADAT - MAIN PROGRAM

def main():

    italok = []

    print("===== BORKÓSTOLÓ NYILVÁNTARTÓ =====")

    while True:

        print("\nMilyen italt szeretnél rögzíteni?")
        print("1. Bor")
        print("2. Pálinka")
        print("stop - Rögzítés befejezése")

        valasztas = input("Választás: ").strip().lower()

        if valasztas == "stop":
            break

        if valasztas not in ["1", "2"]:
            print("Hibás választás! Próbáld újra!")
            continue

        kod = input("Add meg az ital azonosítóját: ").strip()

        while not is_valid_bottle_code(kod):
            print("Hibás azonosító! Példa: ITAL-1234")
            kod = input("Add meg újra az azonosítót: ").strip()

        nev = input("Add meg az ital nevét: ")
        szarmazas = input("Add meg a származási helyet: ")

        while True:
            try:
                palack_terfogat = float(input("Palack térfogata (ml): "))
                if palack_terfogat <= 0:
                    print("A térfogatnak pozitív számnak kell lennie!")
                    continue
                break
            except ValueError:
                print("Hibás adat! Számot adj meg!")

        while True:
            try:
                palack_ar = float(input("Palack ára (Ft): "))
                if palack_ar <= 0:
                    print("Az árnak pozitív számnak kell lennie!")
                    continue
                break
            except ValueError:
                print("Hibás adat! Számot adj meg!")

        if valasztas == "1":

            szolofajta = input("Szőlőfajta: ")

            while True:
                try:
                    evjarat = int(input("Évjárat: "))
                    if evjarat <= 0:
                        print("Az évjáratnak pozitív számnak kell lennie!")
                        continue
                    break
                except ValueError:
                    print("Hibás évjárat! Egész számot adj meg!")

            ital = Wine(
                kod, nev, szarmazas,
                palack_terfogat, palack_ar,
                szolofajta, evjarat
            )

        else:

            gyumolcs = input("Gyümölcs: ")

            ital = Palinka(
                kod, nev, szarmazas,
                palack_terfogat, palack_ar,
                gyumolcs
            )

        bejegyzes = register_tasting(ital)
        italok.append(bejegyzes)

        print("Az ital sikeresen rögzítve!")

    print("\n===== RÖGZÍTETT ITALOK =====")

    if len(italok) == 0:
        print("Nem rögzítettél egyetlen italt sem.")

    for ital, kostolo_ar in italok:
        print("\n" + ital.describe())
        print("Kóstolóadag ára:", kostolo_ar, "Ft")


if __name__ == "__main__":
    main()
