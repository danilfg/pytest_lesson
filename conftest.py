import pytest

from clients.booking_client import BookingClient
from models.booking import Booking, BookingDates
from src.constant import BookingData
from src.settings import settings


@pytest.fixture
def booking_client():
    return BookingClient(base_url=settings.base_url)


@pytest.fixture
def valid_booking_payload():
    return Booking(
        firstname=BookingData.FIRSTNAME.value,
        lastname=BookingData.LASTNAME.value,
        totalprice=1000,
        depositpaid=True,
        bookingdates=BookingDates(checkin="2026-01-01", checkout="2026-01-01"),
        additionalneeds="Breakfast",
    )


@pytest.fixture
def headers():
    return {"Content-Type": "application/json"}


@pytest.fixture
def created_booking(booking_client, valid_booking_payload, headers):
    response = booking_client.create_booking(valid_booking_payload.build(), headers)
    data = response.json()
    yield data
    booking_client.delete_booking(data["bookingid"], headers)


@pytest.fixture
def auth_token(booking_client):
    response = booking_client.get_token()
    data = response.json()
    return data["token"]
