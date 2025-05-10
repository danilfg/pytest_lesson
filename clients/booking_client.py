import requests

from src.settings import settings


class BookingClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def create_booking(self, data: dict, headers: dict) -> requests.Response:
        return requests.post(url=f"{self.base_url}/booking", json=data, headers=headers)

    def delete_booking(self, booking_id: int, headers: dict) -> requests.Response:
        return requests.delete(
            f"{self.base_url}/booking/{str(booking_id)}", headers=headers
        )

    def get_token(self) -> requests.Response:
        return requests.post(
            f"{self.base_url}/auth",
            json={"username": settings.username, "password": settings.password},
        )

    def update_booking(self, booking_id: int, headers: dict, data) -> requests.Response:
        return requests.put(
            f"{self.base_url}/booking/{str(booking_id)}", headers=headers, json=data
        )
