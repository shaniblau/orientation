from typing import Union


def name_to_digit(digit_name: str) -> Union[int, bool]:
    digits: dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    return digits[digit_name] if digit_name in digits else False
