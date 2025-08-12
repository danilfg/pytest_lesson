import pytest
from playwright.sync_api import sync_playwright

from clients.booking_client import BookingClient
from models.booking import Booking, BookingDates
from src.constant import BASE_URL, BookingData
from src.settings import settings


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="session")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()


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
