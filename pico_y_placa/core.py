import datetime as dt
from typing import Optional
import utils
from dataclasses import dataclass


@dataclass
class CanDriveAroundResult:
    can_drive_around: bool
    message: Optional[str]


def is_pico_placa_active(time: dt.time) -> bool:
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


def can_drive_around(
    plate: str, date: dt.date, time: dt.time, restriction_table: dict
) -> CanDriveAroundResult:
    last_digit = utils.get_plate_digit(plate)
    permitted1, permitted2 = restriction_table[
        utils.get_day_name(date)
    ]  # Allowed plate digits during the given day.

    result = CanDriveAroundResult(can_drive_around=True, message=None)

    if last_digit == permitted1 or last_digit == permitted2:
        if is_pico_placa_active(time):
            result.can_drive_around = False
            result.message = "You can't drive right now. The restriction today is from 7:00AM to 9:30AM and from 16:00PM to 19:30PM."

        else:
            result.message = "You can drive right now, but you may have a restricion later. Remember NOT to drive from 7:00AM to 9:30AM and from 16:00PM to 19:30PM."
    else:
        result.message = (
            "No restrictions for you today! You can enjoy the highway at any time!"
        )

    return result
