from django import forms
from django.core.exceptions import ValidationError
from modules.pico_y_placa import utils


def _validate_plate(plate: str):
    if not utils.validate_plate(plate):
        raise ValidationError("Invalid plate. Use format ABC1234.")


class PicoPlacaForm(forms.Form):
    plate = forms.CharField(
        min_length=7, max_length=7, label="Placa", validators=[_validate_plate]
    )
    date = forms.DateField(input_formats=["%d-%m-%y"])
    time = forms.TimeField(input_formats=["%H:%M"])
