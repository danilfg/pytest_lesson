from models.booking import CreateBookingResponse
from src.constant import BookingData


def test_create_booking(created_booking):
    try:
        parsed = CreateBookingResponse(**created_booking)
    except Exception as e:
        raise AssertionError(f"Структура ответа не соответствует данным: {e}")

    assert parsed.booking.bookingdates.checkin == "2026-01-01"

    assert created_booking["booking"]["firstname"] == BookingData.FIRSTNAME.value, (
        "Вернулось не корректное имя\n"
        f"Response:\n{created_booking}\n"
        f"Ожидаемое имя: {BookingData.FIRSTNAME}"
    )
    assert created_booking["booking"]["lastname"] == BookingData.LASTNAME.value, (
        "Вернулось не корректная фамилия\n"
        f"Response:\n{created_booking}\n"
        f"Ожидаемое имя: {BookingData.LASTNAME}"
    )


def test_update_booking(
    booking_client, created_booking, auth_token, headers, valid_booking_payload
):
    booking_id = created_booking["bookingid"]
    headers.update({"Cookie": f"token={auth_token}"})
    payload = valid_booking_payload.build()
    payload.update({"firstname": BookingData.UPDATE_FIRSTNAME.value})
    update_response = booking_client.update_booking(booking_id, headers, payload)
    assert update_response.json()["firstname"] == BookingData.UPDATE_FIRSTNAME.value
