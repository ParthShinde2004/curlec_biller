from django.urls import path
from . import views

urlpatterns = [
    path('showcalculations', views.show_calculations),
    path('showmerchants', views.show_merchants),
    path('showmandates', views.show_mandates),
    path('showcustomers', views.show_customers),
]
