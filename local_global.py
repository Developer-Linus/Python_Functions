count = 0 # Global variable
def increment():
    count += 1 # This refers to the local count within a function.

    increment()

print(count) # Remains unchanged because it is a global variable.