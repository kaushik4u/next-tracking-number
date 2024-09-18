from django.urls import path
from .views import get_next_tracking_number

urlpatterns = [
    path('next-tracking-number/', get_next_tracking_number, name='next_tracking_number'),
]
