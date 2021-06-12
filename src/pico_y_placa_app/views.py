from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from .forms import PicoPlacaForm
from modules.pico_y_placa import core


def index(request: HttpRequest):
    form = None
    result_msg = ""

    if request.method == "POST":
        form = PicoPlacaForm(request.POST)

        if form.is_valid():
            result = core.can_drive_around(
                form.cleaned_data["plate"],
                form.cleaned_data["date"],
                form.cleaned_data["time"],
            )
            result_msg = result.message
            HttpResponseRedirect(request.path_info)

    if request.method == "GET":
        form = PicoPlacaForm()

    return render(
        request, "pico_y_placa_app/index.html", {"form": form, "result": result_msg}
    )
