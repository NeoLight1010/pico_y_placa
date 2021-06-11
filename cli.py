import datetime as dt
import utils


def input_date() -> dt.date:
    """
    Receives input from stdin and verifies the correct input of the Date (length and format). Returns the validated date object.
    """
    while True:
        try:
            return utils.str_to_date(
                input(
                    "Please enter the date you want to check in this format: DD-MM-YY (ex: 10-11-21):\n"
                )
            )
        except ValueError:
            print("Invalid input. Remember to use DD-MM-YY format.")
            continue


def input_plate() -> str:
    """
    Receives input from stdin and validates the plate string: its length and if its last digit can be cast into an integer.
    """
    while True:
        plate = input("Enter your plate number using this format: ABC1234:\n")

        if not utils.validate_plate(plate):
            print("Invalid input. Remember to use ABC1234 format. Try again.\n")
            continue
        return plate


def input_time() -> dt.time:
    """
    Receives input from stdin and validates if the time string can be cast into a dt.time object.
    """
    while True:
        try:
            return utils.str_to_time(
                input(
                    "Tell us what time you want to check. Use this format: HH:MM (ex: 08:30):\n"
                )
            )
        except ValueError:
            print("Ivalid input. Remeber to use HH:MM format.")
            continue
