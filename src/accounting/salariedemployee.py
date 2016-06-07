from src.accounting.employee import Employee


class SalariedEmployee(Employee):

    def __init__(self, employee_id, first_name, last_name, salary, commission_rate, weekly_dues):
        Employee.__init__(employee_id, first_name, last_name, weekly_dues)
        self.__salary = salary
        self.__commission_rate = commission_rate

    def get_full_name(self, last, first):
        print("Employee: " + last + ", " + first)