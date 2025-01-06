def user_info(name, age = None):
    # Print user information
    print(f"Name: {name}")
    if(age):
        print(f"Age: {age}")

user_info(name = "Bob", age = 30) # This is how keyword arguments is assigned. 