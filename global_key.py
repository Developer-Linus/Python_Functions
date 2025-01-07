count = 0 # global variable

def increment_global():

    global count # The use of the keyword global.

    count += 1

increment_global()

print(count) # The output is 1 because the global variable has been modified.