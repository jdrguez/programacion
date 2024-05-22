import re


def is_valid_url(url: str) -> bool:
    valid_form = r'^https?:\//.+\.+.+'
    if m:= re.fullmatch(valid_form, url):
        return True
    return False

