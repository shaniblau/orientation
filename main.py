import datetime

from sections import name_to_digit, sum_items, remove_aeiou, count_appearances, load_data, save_data, \
    days_until_birthday, execute, copy_dir


def sec1(digit_name: str):
    print(name_to_digit(digit_name))


def sec2(numbers: list):
    print(sum_items(numbers))


def sec3(string: str):
    print(remove_aeiou(string))


def sec4(min_num: int, max_num: int):
    print(count_appearances(min_num, max_num))


def sec5(file_name: str, objects: list):
    save_data(file_name, objects)
    load_data(file_name)


def sec6(birthdate: datetime):
    print(days_until_birthday(birthdate))


def sec7(source: str, destination: str, extensions: list = None):
    copy_dir(source, destination, extensions)


def sec8():
    execute()


def main():
    sec1("two")


if __name__ == '__main__':
    main()


