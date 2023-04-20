import functools


def sum_items(numbers: list) -> int:
    return functools.reduce(lambda a, b: a+b, numbers) if len(numbers) > 0 else 0
