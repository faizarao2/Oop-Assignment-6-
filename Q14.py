# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object
#  store a reference to an Employee object that exists independently of it.



class Department:
    def get_department_name(self):
        return "Hr"


class Employee:    
    def __init__(self , department , employee):
        self.department = department
        self.employee = employee


    def display(self):
        print(f"{self.employee.capitalize()} works in the {self.department.get_department_name()} department")


depart = Department()
employee = Employee(depart , "mirha")
employee.display()