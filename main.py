import datetime as dt
import cli
import utils


def get_plate_digit(plate: str) -> int:
    """
    Returns the last digit of the plate as an integer.
    """
    return int(plate[-1])


def _is_pico_y_placa_activated(time: dt.time) -> bool:
    """
    Returns True if Pico y Placa is active at the given time.

    Pico y placa is active at: 7:00am - 9:30am / 16:00pm - 19:30.
    """
    hour = time.hour
    minutes = time.minute

    if time.hour < 7:
        return False

    if hour >= 19 and minutes >= 30:
        return False

    if hour == 9 and minutes >= 30:
        return False

    if hour > 9 and hour < 16:
        return False

    return True


def pico_y_placa(week: dict):
    """
    Returns the information about the Pico & placa pronostic and show a message to the user.
    """
    date = cli.input_date()
    plate = cli.input_plate()
    time = cli.input_time()

    plate_last_digit = get_plate_digit(plate)
    target_day = utils.get_day_name(date)
    pico_placa_is_active = _is_pico_y_placa_activated(time)
    number1, number2 = week[target_day]

    if pico_placa_is_active and (
        plate_last_digit == number1 or plate_last_digit == number2
    ):
        if pico_placa_is_active:
            print(
                "Pico & Placa is activated, you can't drive right now, remember not to do it on this hours (7:00am - 9:30am / 16:00pm - 19:30)."
            )
            return 1
        else:
            print(
                "Pico y Placa is not activated at this time, but you have restriction today so remember not to drive on this hours (7:00am - 9:30am / 16:00pm - 19:30)."
            )
            return 2
    else:
        print(
            "Your car does not have Pico y Placa today, you may enjoy the highway at any time."
        )
        return 0


if __name__ == "__main__":
    _week = {
        "Monday": (1, 2),
        "Tuesday": (3, 4),
        "Wednesday": (5, 6),
        "Thursday": (7, 8),
        "Friday": (9, 0),
        "Saturday": (10, 10),
        "Sunday": (10, 10),
    }
    pico_y_placa(_week)
