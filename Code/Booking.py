import uuid
from Room import Room 
from SearchRoom import SelectedRoom   

class Booking:
    existing_booking_ids = set()
    counter = 0

    def __init__(self, payment, select_room):
        self.__id = Booking.generate_booking_id()
        self.__start_date = select_room.get_start_date()
        self.__end_date = select_room.get_end_date()
        self.__status = "PENDING"
        self.__room_number = Room().get_room_number()
        self.__payment_info = payment
        Booking.counter += 1
        self.__number = Booking.counter

    
    @classmethod
    def generate_booking_id(cls):
        while True:
            booking_id = str(uuid.uuid4().hex)[:8]
            if booking_id not in cls.existing_booking_ids:
                cls.existing_booking_ids.add(booking_id)
                return booking_id
            

    def make_payment(self, payment):
        # Make a payment for the total cost of the booking
        if payment.get_amount() != self.__total_cost:
            raise ValueError('Payment amount does not match total cost of booking')
        payment.process_payment()
        self.__status = 'CONFIRMED'
        self.__payment = payment

    
    def cancel_booking(self, room_catalog):
        if self.__status == "CANCELLED":
            raise ValueError("Booking is already cancelled.")
        self.__status = "CANCELLED"
        # Release the room assigned to the booking
        room_catalog.release_room(self.__room_number)

    def get_booking_id(self):
        return self.__id
    
    def get_booking_status(self):
        return self.__status
    
    def get_room_number(self):
        return self.__room_number
    
    def get_payment_info(self):
        return self.__payment_info
    
    def get_number(self):
        return self.__number
    
    def get_booking_detail(self):
        return self
    
    def __str__(self):
        return f"Booking ID: {self.__id}\n"\
               f"Room Number: {self.__room_number}\n"\
               f"Start Date: {self.__start_date}\n"\
               f"End Date: {self.__end_date}\n"\
               f"Status: {self.__status}\n"\
               f"Payment Info: {self.__payment_info}\n"\
               f"Booking Number: {self.__number}"


class BookingHistory:
    def __init__(self):
        self.__list = []

    def add_book(self, booking):
        self.__list.append(booking)

    def __str__(self):
        if not self.__list:
            return "No bookings yet"
        else:
            return "\n".join(str(booking) for booking in self.__list)