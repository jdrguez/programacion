import re


def is_valid_float(number: str) -> bool:
    valid_float = r'(-*\d_?)*[.e]+[\d|_]*'
    return re.fullmatch(valid_float, number) is not None
