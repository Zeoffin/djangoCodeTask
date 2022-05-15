from .models import Reservation
from django.shortcuts import render
from rest_framework.views import APIView


class DisplayReservationsView(APIView):
    """
    A view for returning data in table format.
    """

    def get(self, request):
        """
        HTTP GET method for all reservations made
        :param request: HTTP request parameter
        :return all_reservations: All reservations
        :rtype: dict
        """

        # Get all reservations
        all_reservations = Reservation.objects.all()

        # Create return dictionary
        reservations = {
            'all_reservations': []
        }

        for reservation in all_reservations:

            # Filter for the same rental and get all previous reservations
            same_rental_filter = all_reservations.filter(rental_id=reservation.rental_id)
            same_rental_filter = same_rental_filter.filter(id__lt=reservation.id)

            # Get previous reservation
            previous_reservation = str(same_rental_filter.last()) if same_rental_filter.last() is not None else " - "

            reservation_dict = {
                'rental_name': reservation.rental_id.name,
                'reservation_id': reservation.__str__(),
                'checkin': str(reservation.checkin),
                'checkout': str(reservation.checkout),
                'previous_reservation': previous_reservation
            }

            reservations['all_reservations'].append(reservation_dict)

        return render(request, 'rental/index.html', reservations)
