import uuid
from register import Account
from Payment import Payment
from SearchRoom import SelectedRoom
from Booking import Booking
class User:
    def __init__(self, email, password, status):
        self._email = email
        self._password = password
        self._status = status

    def watch_rooms(self, room_catalog, type):
        return room_catalog.show_room(type)
    


class Member(User):
    existing_member_ids = set()
    counter = 0

    def __init__(self, fname = '', lname = '', email = '', password = '', phone_number = ''):
        self.__fname = fname
        self.__lname = lname
        self.__status = "ACTIVE"
        self.__email = email
        self.__password = password
        self.__phone_number = phone_number
        self.__member_id = Member.generate_member_id()
        Member.counter += 1
        self.__member_number = Member.counter
        self.__bookings = []
        self.__payment_history = []

    @classmethod
    def generate_member_id(cls):
        while True:
            member_id = str(uuid.uuid4().hex)[:8]
            if member_id not in cls.existing_member_ids:
                cls.existing_member_ids.add(member_id)
                return member_id
    
    def payment(self, method, info):
        payment = Payment(info, method, self)
        payment_successful = payment.process_payment(method)

        if payment_successful:
            booking = Booking(payment, info)
            self.__bookings.append(booking)
            self.__payment_history.append(payment)
            return booking
        else:
            return None

    @staticmethod
    def select_room(start_date, end_date, room_type, catalog):
        selected_room = SelectedRoom(start_date, end_date, room_type, catalog)
        return selected_room
    
    def view_booking(self):
        return self.__bookings
    
    def view_payment(self):
        return self.__payment_history

    def get_name(self):
        return self.__fname + " " + self.__lname
    
    def get_phone(self):
        return self.__phone_number
    
    def get_email(self):
        return self.__email
    
    def get_member_id(self):
        return self.__member_id


class Admin(User):
    def __init__(self, email, password, status):
        User.__init__(self, email, password, status)
    
    
    def add_room(self, room_catalog, room):
        room_catalog.add_room(room)

    def add_show_room(self, room_catalog, room):
        room_catalog.add_show_room(room)

    def update_price(self, room, price):
        room.set_price(price)