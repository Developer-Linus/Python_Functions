def outer_function():
    x = 10 # Variable in the enclosing function

    def inner_function():
        nonlocal x # Using the keyword nonlocal to modify x from enclosing function
        x += 5

    inner_function()
    print(f"The modified value of x from inner function: ", x)
outer_function()