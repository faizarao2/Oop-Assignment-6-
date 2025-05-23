# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another
#  message when it is destroyed (destructor).


class Logger:


    def __init__(self ,message : str , exit_message : str ):
        self.message = message
        self.exit_message = exit_message

        print(f"Logger created : {self.message}")

     
    def __del__(self):
        print(f"Logger destroyed : {self.exit_message}")    


logger = Logger("Your account has been logged in." , "Your account has been logged out.")    

del logger  # deleting the logger