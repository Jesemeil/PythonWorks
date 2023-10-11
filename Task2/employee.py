class Employee:
    emp_id_counter = 0

    def __init__(self, emp_name):
        Employee.emp_id_counter += 1
        self.__emp_id = Employee.emp_id_counter
        self.__emp_name = emp_name
        self.__emp_department = None
        self.__hourly_rate = 10
        self.__number_of_hours_worked = 0

    def set_number_of_hours_worked(self, hours):
        self.__number_of_hours_worked = hours

    def get_emp_id(self):
        return self.__emp_id

    def get_emp_name(self):
        return self.__emp_name

    def get_emp_department(self):
        return self.__emp_department

    def get_hourly_rate(self):
        return self.__hourly_rate

    def get_number_of_hours_worked(self):
        return self.__number_of_hours_worked

    def calculate_emp_salary(self):
        return self.__hourly_rate * self.__number_of_hours_worked

    def emp_assign_department(self, department):
        self.__emp_department = department

    def print_employee_details(self):
        details = f"Employee ID: {self.__emp_id}\nEmployee Name: {self.__emp_name}\nEmployee Department: {self.__emp_department}\nHourly Rate: ${self.__hourly_rate}\nNumber of Hours Worked: {self.__number_of_hours_worked}"
        return details
    
    



