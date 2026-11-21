from wine_spirits_culture import is_valid_bottle_code


def test_ervenyes_azonosito():
    assert is_valid_bottle_code("ITAL-1234") is True


def test_hibas_elotag():
    assert is_valid_bottle_code("BOR-1234") is False


def test_tul_rovid_azonosito():
    assert is_valid_bottle_code("ITAL-123") is False


def test_tul_hosszu_azonosito():
    assert is_valid_bottle_code("ITAL-12345") is False