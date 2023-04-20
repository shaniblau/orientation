import datetime


def days_until_birthday(birthdate: datetime) -> str:
    current_date: datetime.date = datetime.date.today()
    closest_birthday: datetime.time = birthdate.replace(year=current_date.year)
    if (closest_birthday - current_date).days < 0:
        closest_birthday: datetime.time = birthdate.replace(year=current_date.year + 1)
    return str((closest_birthday - current_date)).split(", ")[0]
