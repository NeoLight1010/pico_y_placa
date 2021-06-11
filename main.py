import cli
import core


if __name__ == "__main__":
    _restrictions = {
        "Monday": (1, 2),
        "Tuesday": (3, 4),
        "Wednesday": (5, 6),
        "Thursday": (7, 8),
        "Friday": (9, 0),
        "Saturday": (10, 10),
        "Sunday": (10, 10),
    }

    plate = cli.input_plate()
    date = cli.input_date()
    time = cli.input_time()

    print(core.can_drive_around(plate, date, time, _restrictions).message)
