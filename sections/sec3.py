import re


def remove_aeiou(string: str) -> str:
    return re.sub('[aeuio]', '', string)