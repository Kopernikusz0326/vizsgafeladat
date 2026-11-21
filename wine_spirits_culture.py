import re


def is_valid_bottle_code(code):
    pattern = r"ITAL-\d{4}"

    return re.fullmatch(pattern, code) is not None