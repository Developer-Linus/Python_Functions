def check_number(number):
    remainder = number%2
    if(remainder == 0):
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

check_number(7)