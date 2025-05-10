from typing import Optional

from pydantic import BaseModel


class BookingDates(BaseModel):
    checkin: str
    checkout: str


class Booking(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: Optional[str] = None

    def build(self):
        return self.model_dump()


class CreateBookingResponse(BaseModel):
    bookingid: int
    booking: Booking

    def build(self):
        return self.model_dump()
