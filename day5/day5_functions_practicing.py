
# --------------------------------------
# Basic function without parameters
def greet():
    print("Hello, World!")
# To call:
greet()

# --------------------------------------
# Function with parameters
def greet_person(name):
    """Greet a specific person"""
    print(f"Hello, {name}!")
# To call the function above:
greet_person("Maamoun")

# --------------------------------------
# Function with return value
def add_numbers(a, b):
    """Add two numbers and return the result"""
    return a + b
# To call it:
result=add_numbers(3,4)
print(result)
# OR
print(add_numbers(5,3))

# --------------------------------------
# Function with default parameters
def create_profile(name, age=25, occupation="Developer"):
    """Create a user profile with some default values"""
    profile = {
        "name": name,
        "age": age,
        "occupation": occupation
    }
    return profile

# --------------------------------------
# Function with multiple return values
def get_min_max(numbers):
    """Return both minimum and maximum values from a list"""
    if not numbers:
        return None, None
    return min(numbers), max(numbers)
# To call:
get_min_max([3,4,5,6])

# --------------------------------------
# Function with variable number of arguments
def calculate_average(*numbers):
    """Calculate the average of any number of values"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
#To Call:
result = calculate_average(10, 20, 30, 40, 50)
print(result)

# --------------------------------------
# Demonstrating scope
print("\nDemonstrating scope:")
def scope_example():
    local_var = "I'm local" #(inside the function)
    print(f"Inside function: {local_var}")

    # This will access the global variable
    print(f"Inside function, global_var: {global_var}")

global_var = "I'm global" #global (outside), can be accessed by inside
scope_example()
print(f"Outside function, global_var: {global_var}")
# This would cause an error because local_var is not accessible here
# print(local_var)  # Uncomment to see the error
