# Decorator function
def greeting_decorator(func):
    def wrapper():
        print("----- Program Started -----")
        func()
        print("----- Program Ended -----")
    return wrapper

# Function to decorate
@greeting_decorator
def greet():
    print("Hello, Welcome to Python Decorators!")

# Calling the decorated function
greet()
