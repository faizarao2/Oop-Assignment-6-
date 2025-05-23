# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.



class Employee:
    def __init__(self, name: str, salary: int, ssn: int):
        self.name = name   #public vatiable
        self._salary = salary  #protected variable
        self.__ssn = ssn     #private variable




employee = Employee("Mirha", 50000, 123456789)
print("Name: ", employee.name)   # Accessing public variable (works fine)
print("Salary: ", employee._salary)   # Accessing protected variable (works fine but not recommended)
# print("SSN: ", employee._Employee__ssn)   # Accessing private variable using name mangling (works fine)

print("SSN: ", employee.__ssn)   # Attempting to access private variable  (raise an AttributeError)

