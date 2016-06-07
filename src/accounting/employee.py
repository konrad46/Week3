class Employee:
    def __init__(self, employee, first, last, weekly_dues):
        self.__employee_id = employee
        self.__first_name = first
        self.__last_name = last
        self.__weekly_dues = weekly_dues

    def set_employee(self, employee):
        self.__employee_id = employee

    def set_first(self, first):
        self.__first_name = first

    def set_last(self, last):
        self.__last_name = last

    def get_weekly_dues(self):
        return self.__weekly_dues

    def get_full_name(self, last, first):
        print("Employee: " + last + ", " + first)