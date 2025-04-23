from menu import Menu

class Restaurant:

    def __init__(self,name):
        self.name = name
        self.employees = []        #database of Employees
        self.menu = Menu()         #this attr is a object of Menu class which can have list of item obj    

    def add_employee(self,employee):
        self.employees.append(employee)
        print(f'{employee.name} is added in the employee database!!')

    def view_employee(self):
        print('---Employee List---')
        for emp in self.employees:
            print(f'Name: {emp.name}, Email: {emp.email}, Address: {emp.address}, Phone: {emp.phone}, Age: {emp.age}, Designation: {emp.designation}, Salary: {emp.salary}')
