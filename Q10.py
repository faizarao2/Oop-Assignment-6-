# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints
#  a message including the dog's name.



class Dog:
    def __init__(self , name :str , breed : str):  #constructor method 
        self.name = name      #instance variable
        self.breed = breed    #instance variable


    def bark(self):    ## instance method
            print(f"{self.name} says Woof! I am a {self.breed}.")    

dog = Dog("Buddy" , "Golden Retriever")
dog.bark()  # Output: Buddy says Woof! I am a Golden Retriever.