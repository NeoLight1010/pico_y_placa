from . import cli
from . import core


if __name__ == "__main__":

    plate = cli.input_plate()
    date = cli.input_date()
    time = cli.input_time()

    print(core.can_drive_around(plate, date, time).message)
