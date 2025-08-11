import allure

from models.booking import CreateBookingResponse
from src.constant import BookingData

pytestmark = [allure.parent_suite("Тест API"), allure.suite("Тестирование брони")]


@allure.title("Создание записи брони")
def test_create_booking(created_booking):
    try:
        with allure.step("Валидация ответа после создания брони"):
            parsed = CreateBookingResponse(created_booking)
    except Exception as e:
        raise AssertionError(f"Структура ответа не соответствует данным: {e}")
    with allure.step("Проверка даты заезда"):
        assert parsed.booking.bookingdates.checkin == "2026-01-01"
    with allure.step("Проверка имени клиента"):
        assert created_booking["booking"]["firstname"] == BookingData.FIRSTNAME.value, (
            "Вернулось не корректное имя\n"
            f"Response:\n{created_booking}\n"
            f"Ожидаемое имя: {BookingData.FIRSTNAME}"
        )
    with allure.step("Проверка фамилии клиента"):
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
