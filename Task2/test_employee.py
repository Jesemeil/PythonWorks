import unittest
from employee import Employee


class EmployeeTest(unittest.TestCase):

    def setUp(self):
        self.employee1 = Employee("Daniel Regha")
        self.employee2 = Employee("Akpan Udoh")
        self.employee3 = Employee("Joe Eric")
        self.employee1.set_number_of_hours_worked(40)

    def test_employee_id_increases(self):
        self.assertEqual(self.employee1.get_emp_id(), 1)
        self.assertEqual(self.employee2.get_emp_id(), 2)
        self.assertEqual(self.employee3.get_emp_id(), 3)

    def test_initial_employee_details(self):
        self.assertEqual(self.employee1.get_emp_name(), "Daniel Regha")
        self.assertEqual(self.employee1.get_emp_department(), None)
        self.assertEqual(self.employee1.get_hourly_rate(), 10)
        self.assertEqual(self.employee1.get_number_of_hours_worked(), 40)

    def test_calculate_employee_salary(self):
        self.assertEqual(self.employee1.calculate_emp_salary(), 400)

    def test_employee_assign_department(self):
        self.employee1.emp_assign_department("Physics")
        self.assertEqual(self.employee1.get_emp_department(), "Physics")

    def test_print_employee_details(self):
        expected_output = "Employee ID: 1\nEmployee Name: Daniel Regha\nEmployee Department: None\nHourly Rate: $10\nNumber of Hours Worked: 40"
        self.assertEqual(self.employee1.print_employee_details(), expected_output)


