class DateCal:
    def is_leap(self, year):
        if year % 400 == 0:
            return True
        elif year % 100 != 0 and year % 4 == 0:
            return True
        else: return False


    def day_of_year(self, day, month, year):
        day_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap(year):
            day_in_month[2] = 29
        day_of_years = int(day) + sum(day_in_month[0 : int(month)])
        return day_of_years


    def day_in_year(self, year):
        return 366 if self.is_leap(year) else 365


    def date_diff(self, start_date, end_date):
        day_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        date1_list = [int(date) for date in start_date.split("-")]
        date2_list = [int(date) for date in end_date.split("-")]
        day_list = [date1_list, date2_list]

        for i in range(2):
            month_index = day_list[i][1]
            day = day_list[i][0]
            if self.is_leap(day_list[i][2]):
                day_in_month[1] = 29
            if month_index > 12 or month_index < 1:
                return -1
            if day > day_in_month[month_index] or day < 1:
                return -1

        days = 0

        for i in range(date1_list[2], date2_list[2]):
            days += self.day_in_year(i)

        days -= self.day_of_year(date1_list[0], date1_list[1], date1_list[2])
        days += self.day_of_year(date2_list[0], date2_list[1], date2_list[2])

        return days + 1