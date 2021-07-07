from django.shortcuts import render
from rest_framework import generics, status
from .models import CalculationRule, Merchant, MandateInstantPay, Mandate, Customer
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse, request


def show_calculations(request):
    showall = list(CalculationRule.objects.values())
    return JsonResponse(showall, safe=False)


def show_merchants(request):
    showall_merchants = list(Merchant.objects.values())
    return JsonResponse(showall_merchants, safe=False)


def show_mandates(request):
    showall_mandates = list(Mandate.objects.values())
    return JsonResponse(showall_mandates, safe=False)


def show_customers(request):
    showall_customers = list(Customer.objects.values())
    return JsonResponse(showall_customers, safe=False)


def show_instantpay(request):
    showall_instantpay = list(MandateInstantPay.objects.values())
    return JsonResponse(showall_instantpay, safe=False)
