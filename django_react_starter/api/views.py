from django.shortcuts import render
from rest_framework import generics, status
from .models import (
    CalculationRule,
    Merchant,
    Mandate,
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
    showall_mandates = Mandate.objects.all()
    getmerchantid = request.GET.get("merchant_id")
    if getmerchantid != None and getmerchantid != "":
        showall_mandates = showall_mandates.filter(merchant__id=getmerchantid)
    result = list(showall_mandates.values())
    return JsonResponse({"data": result})


# function should get reference number
# slow api calls


def show_transactions(request):  # not working function!
    showall_transactions = MandateTransaction.objects.all()
    gettransaction = request.GET.get("reference_number")
    if gettransaction != None and gettransaction != "":
        showall_transactions = showall_transactions.filter(
            reference_number=gettransaction
        )
    result = list(showall_transactions.values())
    return JsonResponse({"data": result})
