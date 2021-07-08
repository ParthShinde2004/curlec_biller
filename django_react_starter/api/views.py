from django.shortcuts import render
from rest_framework import generics, status
from .models import (
    CalculationRule,
    Merchant,
    # MandateInstantPay,
    Mandate,
    # Customer,
    MandateTransaction,
)
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse, request


def show_calculations(request):
    showall = list(CalculationRule.objects.values())
    return JsonResponse({"data": showall})


def show_merchants(request):
    showall_merchants = list(Merchant.objects.values())
    return JsonResponse({"data": showall_merchants})


def show_mandates(request):
    showall_mandates = list(Mandate.objects.values())
    return JsonResponse({"data": showall_mandates})


def show_transactions(request):
    showall_transactions = list(MandateTransaction.objects.values())
    return JsonResponse({"data": showall_transactions})

# def show_customers(request):
#     showall_customers = list(Customer.objects.values())
#     return JsonResponse(showall_customers, safe=False)

# def show_instantpay(request):
#     showall_instantpay = list(MandateInstantPay.objects.values())
#     return JsonResponse(showall_instantpay, safe=False)
