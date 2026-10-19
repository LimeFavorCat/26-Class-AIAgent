class Employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary

    def work(self):
        print(f'사번 {self.emp_id} 번이 출근하여 업무중')