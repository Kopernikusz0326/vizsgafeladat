from wine_spirits_culture import is_valid_bottle_code, Beverage


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