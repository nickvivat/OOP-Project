class Room:
    def __init__(self, name='', type='', room_price='', room_number=0, bed_type='', size='', toilet_type='', complimentary='', speaker='', bathrobes='', details='', highlights='', description=''):
        self.__name = name
        self.__type = type
        self.__room_price = room_price
        self.__room_number = room_number
        self.__bed_type = bed_type
        self.__size = size
        self.__toilet_type = toilet_type
        self.__complimentary = complimentary
        self.__speaker = speaker
        self.__coffee_machine = True
        self.__bathrobes = bathrobes
        self.__details = details
        self.__highlights = highlights
        self.__description = description
        self.__contact = "48 Oriental Avenue, Bangkok 10500, Thailand +66 (0) 2 659 9000 mobkk-reservations@mohg.com"
        self.__reservations = []

    def convert_price(self):
        show_price = '฿{:,}'.format(self.__room_price)
        return show_price

    def reserve(self, start_date, end_date):
        if self.is_available(start_date, end_date):
            self.__reservations.append((start_date, end_date))
            print(f"Room {self.__room_number} has been reserved from {start_date} to {end_date}.")
            return True
        else:
            print(f"Room {self.__room_number} is not available for the selected dates.")
            return False

    def is_available(self, start_date, end_date):
        for reservation in self.__reservations:
            if start_date < reservation[1] and end_date > reservation[0]:
                return False
        return True

    def get_name(self):
        return self.__name

    def get_room_number(self):
        return self.__room_number

    def get_type(self):
        return self.__type

    def get_price(self):
        return self.__room_price

    def get_bed_type(self):
        return self.__bed_type

    def get_size(self):
        return self.__size

    def get_toilet_type(self):
        return self.__toilet_type

    def get_complimentary(self):
        return self.__complimentary

    def get_speaker(self):
        return self.__speaker

    def get_coffee_machine(self):
        return self.__coffee_machine

    def get_bathrobes(self):
        return self.__bathrobes

    def get_details(self):
        return self.__details

    def get_highlights(self):
        return self.__highlights

    def get_description(self):
        return self.__description
    
    def get_reservations(self):
        return self.__reservations

    def set_description(self, data):
        self.__description = data

    def set_price(self, price):
        self.__room_price = price

    def __str__(self):
        return f"{self.__name}\nPrice: {self.convert_price()}\n{self.__bed_type}\nSize: {self.__size}\n{self.__toilet_type}\n{self.__speaker}\n{self.__bathrobes}\nHighlights: {self.__highlights}\nDescription: {self.__description}\n"
