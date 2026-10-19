from employee_type import FullTimeEmployee, PartTimeEmployee

employees = [FullTimeEmployee('홍길동', '0001', 3000000), FullTimeEmployee('철수', '0002', 2800000), PartTimeEmployee('홍길동', '0001', 12000, 200)]

for employee in employees:
    print(f'사번 {employee.get_emp_id()} - {employee.get_name()}의 세전 임금은 {employee.calculate_salary():3,d}원 입니다.')