def count_appearances(min_num: int, max_num: int) -> int:
    return sum(str(num).count('8') or str(num).count('0') for num in range(min_num, max_num + 1))