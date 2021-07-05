from django.shortcuts import render
from rest_framework import generics, status
from .models import CalculationRule
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse, request


def show_calculations(request):
    showall = list(CalculationRule.objects.values())
    return JsonResponse({"data": showall})
