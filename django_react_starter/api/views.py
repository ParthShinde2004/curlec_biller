from django.shortcuts import render
from rest_framework import generics, status
from .models import CalculationRule


def show_calculations(request):
    showall = CalculationRule.objects.all()
    return render(request, "index.html", {"data": showall})
