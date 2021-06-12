from django.shortcuts import render
from django.http import HttpRequest


def index(request: HttpRequest):
    return render(request, "pico_y_placa_app/index.html")
