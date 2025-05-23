# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a 
# subject field, and use super() to call the base class constructor.


class Person:
    def __init__(self , name:str):
        self.name = name
        print(f"Teacher Name : {self.name}")



class Teacher(Person):
    def __init__(self ,name:str , subject :str ):
        super().__init__(name)
        self.subject = subject
        print(f"Miss {self.name} teaches {self.subject} subject" )


try:
    name = input("Enter name: ")
    subject = input("Enter subject field: ")

    if not name.isalpha() or not subject.isalpha():
        raise ValueError


    teacher = Teacher(name , subject)


except ValueError:
    print("Invalid input. Please enter a string.")