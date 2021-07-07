from django.urls import path
from . import views

urlpatterns = [
    path('showcalculations', views.show_calculations),
    path('showmerchants', views.show_merchants),
]
