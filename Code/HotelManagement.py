from enum import Enum

class BookingStatus(Enum):
    PENDING, CONFIRMED, CANCELLED = 1, 2, 3
    

class RoomStatus(Enum):
    AVAILABLE, UNAVAILBLE = 1, 2


class PaymentStatus(Enum):
    UNPAID, PENDING, COMPLETE, CANCELLED, REFUNDED = 1, 2, 3, 4, 5


class Stays:
    def __init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, number_of_room, contact):
        self._name = name
        self._room_number = room_number
        self._bed_type = bed_type
        self._size = size
        self._toilet_type = toilet_type
        self._complimentary = complimentary
        self._speaker = speaker
        self._coffee_machine = coffee_machine
        self._bathrobes = bathrobes
        self._details = details
        self._highlights = highlights
        self._description = description
        self._number_of_room = number_of_room
        self._contact = contact


class Rooms(Stays):
    def __init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, number_of_room, contact):
        Stays.__init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, number_of_room, contact)
        self._reserved_room = []
    pass


class Suites(Stays):
    def __init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, number_of_room, contact, bedroom, connecting, powder_room):
        Stays.__init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, number_of_room, contact)
        self._bedroom = bedroom
        self._connecting = connecting
        self._powder_room = powder_room
        self._reserved_room = []
    pass


class RoomCatalog:
    def __init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, room_count, contact):
        Stays.__init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, room_count, contact)
        self.__room_list = []
    pass


class Contact:
    def __init__(self, header_info, general_enquires, reservation, sales_marketing, dining, weddings, events, spa):
        self.__header_info = header_info
        self.__general_enquires = general_enquires
        self.__reservation = reservation
        self.__sales_marketing = sales_marketing
        self.__dining = dining
        self.__weddings = weddings
        self.__events = events
        self.__spa = spa
    pass


class Payment:
    def __init__(self, first_name, last_name, email, email_confirmation, country, phone_number, street_address, city, state_province, postal_code,date_of_birth, additional_info, terms_conditions, unpaid):
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._email_confirmation = email_confirmation
        self._country = country
        self._phone_number = phone_number
        self._street_address = street_address
        self._city = city
        self._state_province = state_province
        self._postal_code = postal_code
        self._date_of_birth = date_of_birth
        self._additional_info = additional_info
        self._terms_conditions = terms_conditions
        self._unpaid = unpaid
    pass


class Booking:
    def __init__(self, calendar, check_in, check_out, room_price, total_price, currency):
        self.__calendar = calendar
        self.__check_in = check_in
        self.__check_out = check_out
        self.__room_price = room_price
        self.__total_price = total_price
        self.__currency = currency
    pass


class CreditPayment:
    def __init__(self, card_number, cardholder_name, expiration_date):
        self.__card_number = card_number
        self.__cardholder_name = cardholder_name
        self.__expiration_date = expiration_date
    pass


class SpecialCode:
    def __init__(self, iata_number, promo_code, group_code):
        self.__iata_number = iata_number
        self.__promo_code = promo_code
        self.__group_code = group_code
    pass


class Hotel:
    def __init__(self, name, branch, location):
        self.__name = name
        self.__branch = branch
        self.__location = location
    pass


class User:
    def __init__(self, email, password, status):
        self._email = email
        self._password = password
        self._status = status
    pass


class Member(User):
    def __init__(self, email, password, status, member_id):
        User.__init__(self, email, password, status)
        self.__member_id = member_id
    pass


class Guest(User):
    def __init__(self, email, password, status):
        User.__init__(self, email, password, status)
    pass


class Admin(User):
    def __init__(self, email, password, status):
        User.__init__(self, email, password, status)
    pass


class BookingHistory:
    def __init__(self, room_number, date, nights):
        self.__room_number = room_number
        self.__date = date
        self.__nights = nights
    pass

