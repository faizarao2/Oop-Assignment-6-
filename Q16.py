# 16. Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" 
# before a function executes. Apply it to a function say_hello().



# Decorator function
def log_function_call(func):
    def wrapper(name):
        print("Function is being called")
        func(name)
    return wrapper

# Normal function
@log_function_call
def say_hello(name):
    print(f"Hello {name}!")

# Call the function
say_hello("Mirha")