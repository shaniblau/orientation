import re


def save_data(file_name: str, objects: list):
    legal_types: bool = True
    for item in objects:
        if type(item) not in [bool, str, int, float]:
            legal_types = False
    if legal_types:
        with open(file_name, 'w') as file:
            file.writelines([str(item) + "," for item in objects])


def load_data(file_name: str) -> list:
    objects: list = []
    with open(file_name) as file:
        items = file.read().split(",")[:-1]
    for item in items:
        if item.isdigit():
            objects.append(int(item))
        elif item in ['True', 'False']:
            if item == 'True':
                objects.append(True)
            else:
                objects.append(False)
        elif re.match(r'^-?\d+\.\d+$', item):
            objects.append(float(item))
        else:
            objects.append(item)
    return objects
