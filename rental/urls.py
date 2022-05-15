from django.urls import path

from .views import DisplayReservationsView

# Make the landing page to get the view for the table of reservations
urlpatterns = [
    path('', DisplayReservationsView.as_view(), name='DisplayReservations'),
]