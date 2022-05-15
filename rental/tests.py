from django.test import TestCase, Client
from .models import Rental, Reservation


class DisplayReservationsViewTests(TestCase):
    """
    Test class for DisplayReservationsView
    """

    def setUp(self):

        self.client = Client()

        self.rental_1 = Rental(name="Test Rental 1")
        self.rental_1.save()
        self.rental_2 = Rental(name="Test Rental 2")
        self.rental_2.save()

        self.reservation_1 = Reservation(
            rental_id=self.rental_1,
            checkin="2022-02-01",
            checkout='2022-02-05').save()

        self.reservation_2 = Reservation(
            rental_id=self.rental_1,
            checkin="2022-02-05",
            checkout='2022-02-09').save()

        self.reservation_3 = Reservation(
            rental_id=self.rental_2,
            checkin="2022-03-10",
            checkout='2022-04-05').save()

        self.reservation_4 = Reservation(
            rental_id=self.rental_2,
            checkin="2022-04-14",
            checkout='2022-04-17').save()

        self.reservation_5 = Reservation(
            rental_id=self.rental_1,
            checkin="2022-02-15",
            checkout='2022-02-20').save()

    def test_display_reservations_GET(self):
        """
        Test the request of DisplayReservations GET method
        """

        response = self.client.get('')

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'rental/index.html')

    def test_reservation_format(self):
        """
        Test for expected data in the GET context
        """
        response = self.client.get('')
        all_reservations = response.context['all_reservations']

        reservation_1 = all_reservations[0]
        self.assertEquals(reservation_1['rental_name'], 'Test Rental 1')
        self.assertEquals(reservation_1['reservation_id'], 'Res-1 1')
        self.assertEquals(reservation_1['checkin'], '2022-02-01')
        self.assertEquals(reservation_1['checkout'], '2022-02-05')
        self.assertEquals(reservation_1['previous_reservation'], ' - ')

    def test_previous_entry(self):
        """
        Test if previous entry of the same rental is returned
        """

        response = self.client.get('')
        all_reservations = response.context['all_reservations']

        reservation_1 = all_reservations[0]
        reservation_2 = all_reservations[1]
        reservation_5 = all_reservations[4]

        # Test case when no previous reservation exists
        self.assertEquals(reservation_1['previous_reservation'], ' - ')

        # When previous reservation exists
        self.assertEquals(reservation_2['previous_reservation'], "Res-1 1")

        # When previous reservation exists in-between other rentals
        self.assertEquals(reservation_5['previous_reservation'], "Res-2 1")
