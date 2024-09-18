from DateCal import DateCal
class RoomCatalog:
    def __init__(self):
        self.__rooms_list = []
        self.__show_list = []

    def add_room(self, room):
        self.__rooms_list.append(room)

    def add_show_room(self, room):
        self.__show_list.append(room)

    def show_room(self, type):
        if type == "Stays":
            return self.__show_list
        elif type == "Rooms":
            temp_rooms_list = [room for room in self.__show_list if room.get_type() == "Room"]
            return temp_rooms_list
        elif type == "Suites":
            temp_rooms_list = [room for room in self.__show_list if room.get_type() == "Suite"]
            return temp_rooms_list
        
    def get_rooms_list(self):
        return self.__rooms_list
    
    def get_show_list(self):
        return self.__show_list
    

class SelectedRoom:
    def __init__(self, start_date, end_date, type, room_catalog):
        self.__type = type
        self.__start_date = start_date
        self.__end_date = end_date
        self.__room_number = self.get_available_room(room_catalog).get_room_number()
        self.__nights = DateCal().date_diff(start_date, end_date)
        self.__price = self.get_price(room_catalog)
        self.__total_cost = self.__price * self.__nights

    def get_price(self, room_catalog):
        for room_type in room_catalog.get_rooms_list():
            for room in room_type:
                if room.get_name() == self.__type:
                    return room.get_price()      
        raise ValueError(f"No room found for type '{self.__type}'")
    
    def get_available_room(self, room_catalog):
        for room_type in room_catalog.get_rooms_list():
            for room in room_type:
                if room.get_name() == self.__type and room.is_available(self.__start_date, self.__end_date):
                    return room
        raise ValueError (f"No room available for type '{self.__type}' on date {self.__start_date} to {self.__end_date}")
    
    def reserve(self, room_catalog):
        self.get_available_room(room_catalog).reserve(self.__start_date, self.__end_date)

    def get_total_cost(self):
        return self.__total_cost
    
    def get_start_date(self):
        return self.__start_date
    
    def get_end_date(self):
        return self.__end_date
    
    def get_nights(self):
        return self.__nights
    
    def get_type(self):
        return self.__type
    
    def get_room_number(self):
        return self.__room_number
    
    def get_room_price(self):
        return self.__price
    
