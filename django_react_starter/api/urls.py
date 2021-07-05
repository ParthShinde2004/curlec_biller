from django.urls import path
from . import views
# from .views import show_calculations

# urlpatterns = [
#     path('showcalculations/', show_calculations)
# ]

urlpatterns = [
    path('showcalculations', views.show_calculations)
]
