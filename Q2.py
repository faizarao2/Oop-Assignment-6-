# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count = 0  # Class variable to keep track of the number of objects

    def __init__(self, name, id, age, marks):
        self.name = name
        self.id = id
        self.age = age
        self.marks = marks
        Counter.count += 1

    @classmethod # Class method to access class variable
    def display_count(cls):
        print(f"Number of objects created: {cls.count}")

    def display(self):
        print(f"Name: {self.name}, ID: {self.id}, Age: {self.age}, Marks: {self.marks}")

# Creating objects of Counter class
c1 = Counter("Faiza", 101, 20, 90)
c2 = Counter("Rimsha", 102, 22, 85)
c3 = Counter("Mirha", 103, 21, 95)

# Displaying details of each object
c1.display()
c2.display()
c3.display()

# Displaying the count of objects created
Counter.display_count()
