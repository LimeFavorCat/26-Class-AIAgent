from employee import Employee

class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.__monthly_salary = monthly_salary

    def get_monthly_salary(self):
        return self.__monthly_salary

    def calculate_salary(self):
        return self.__monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hourly_wage, hours):
        super().__init__(name, emp_id)
        self.__hourly_wage = hourly_wage
        self.__hours = hours

    def get_hours(self):
        return self.__hours

    def get_hourly_wage(self):
        return self.__hourly_wage

    def calculate_salary(self):
        return self.__hourly_wage * self.__hours
