# . Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance 
# variables should be used.



class MathUtils:


    @staticmethod
    def add(a , b):
        sum = a + b 
        return sum
    

sum = MathUtils.add(2 , 3)   #creating instance of MathUtils class
print("Sum of 2 and 3 is : ", sum)   #calling static method add