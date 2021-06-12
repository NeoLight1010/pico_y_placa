from django.shortcuts import render
from django.http import HttpRequest
from .forms import PicoPlacaForm


def index(request: HttpRequest):
    form = None

    if request.method == "POST":
        form = PicoPlacaForm(request.POST)

        if form.is_valid():
            print("Form is valid!")

    if request.method == "GET":
        form = PicoPlacaForm()

    return render(request, "pico_y_placa_app/index.html", {"form": form})
