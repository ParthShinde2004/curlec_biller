from django.shortcuts import render
from rest_framework import generics, status
from .models import (
    CalculationRule,
    Merchant,
    MandateInstantPay,
    Mandate,
    Customer,
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
    # showall_mandates = list(Mandate.objects.filter(
    #     merchant_id=getmerchantid).values())
    return JsonResponse({"data": result})


def show_transactions(request):
    showall_transactions = MandateTransaction.objects.all()
    gettransaction = request.GET.get("merchant_id")
    if gettransaction != None and gettransaction != "":
        showall_transactions = showall_transactions.filter(
            merchant__id=gettransaction)
    result = list(showall_transactions.values())
    return JsonResponse({"data": result})

# def show_customers(request):
#     showall_customers = list(Customer.objects.values())
#     return JsonResponse(showall_customers, safe=False)

# def show_instantpay(request):
#     showall_instantpay = list(MandateInstantPay.objects.values())
#     return JsonResponse(showall_instantpay, safe=False)
