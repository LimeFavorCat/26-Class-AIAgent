from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, emp_id):
        self.__name = name
        self.__emp_id = emp_id

    def show_info(self):
        print(f'직원 이름 : {self.__name}, 사번 : {self.__emp_id}')

    def get_name(self):
        return self.__name

    def get_emp_id(self):
        return self.__emp_id
    
    @abstractmethod
    def calculate_salary():
        pass