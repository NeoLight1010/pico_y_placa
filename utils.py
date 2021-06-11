import datetime as dt


def str_to_date(date_str: str) -> dt.date:
    return dt.datetime.strptime(date_str, "%d-%m-%y").date()


def str_to_time(time_str: str) -> dt.time:
    return dt.datetime.strptime(time_str, "%H:%M").time()


def validate_plate(plate: str) -> bool:
    """
    Returns True if plate string is valid.

    The format must be: ABC1234
    """
    if len(plate) != 7:
        return False

    for i in range(3):
        if not plate[i].isalpha:
            return False

    for i in range(3, 7):
        if not plate[i].isnumeric():
            return False

    return True


def get_day_name(date: dt.date) -> str:
    """
    Returns the name of the day given a date object.
    """
    return date.strftime("%A")
