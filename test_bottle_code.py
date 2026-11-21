from wine_spirits_culture import is_valid_bottle_code, Beverage, Wine, Palinka


def test_ervenyes_azonosito():
    assert is_valid_bottle_code("ITAL-1234") is True


def test_hibas_elotag():
    assert is_valid_bottle_code("BOR-1234") is False


def test_tul_rovid_azonosito():
    assert is_valid_bottle_code("ITAL-123") is False


def test_tul_hosszu_azonosito():
    assert is_valid_bottle_code("ITAL-12345") is False


def test_kostolo_ar_kiszamitasa():
    ital = Beverage("ITAL-1234", "Egri Bikavér", "Eger", 1000, 10000)

    assert ital.calculate_tasting_price(100) == 1000


def test_bor_kostolo_ar():
    bor = Wine("ITAL-1234", "Egri Bikavér", "Eger", 1000, 10000, "Kékfrankos", 2020)

    assert bor.calculate_tasting_price() == 1000


def test_palinka_kostolo_ar():
    palinka = Palinka("ITAL-1235", "Szilvapálinka", "Szatmár", 1000, 10000, "Szilva")

    assert palinka.calculate_tasting_price() == 200


def test_bor_leirasa():
    bor = Wine("ITAL-1234", "Egri Bikavér", "Eger", 1000, 10000, "Kékfrankos", 2020)

    assert "Kékfrankos" in bor.describe()
    assert "2020" in bor.describe()


def test_palinka_leirasa():
    palinka = Palinka("ITAL-1235", "Szilvapálinka", "Szatmár", 1000, 10000, "Szilva")

    assert "Szilva" in palinka.describe()