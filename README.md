# Python_Functions
- Functions are reusable piece of code for performing specific tasks. 
- They assist in breaking down complex programs into smaller, manageable parts.

## Function Definition
- To create a function, I use the keyword **def** followed by the name I want to give my function. Then, I put parantheses (if any), followed by a colon. After that, I write the code for what I want my function to do, and i indent this code to show it's part of function. Check the file `function_definition.py` to see how this is done.

## Lambda Functions
- Also called **anonymous** functions because they do not need a name.
- used for writing simple, one-line expressions.
- useful when passing a simple function as an argument to another function, as in the `map()`, `filter()`, and `reduce()` functions.
- Only applicable to one line of code that is simple.
- Also used when you need to define a temporary function without need for defining a full function separately.
- check the file `lambda.py` to see how it is done.
## Parameters
- Are variables defined in the function declaration.
- They receive values when a function is called and they must be used within the function code's block. 
- They are of 4 types:
(a) **Positional**: passed based on their position in the function call.
(b) **Keyword**: passed with their corresponding variable names.
(c) **Default**: parameters with pre-defined default values.
(d) **Variable-length**: accept a variable number of arguments. 
Check the file `parameters.py` for an example.

## Arguments
- The actual values we pass when calling out a function are called **arguments**. 
## Keyword Arguments
- Instead of us relying on the position of arguments, we can explicitly specify which parameter should take which value by using keywords (parameter name) when calling the function.
- Useful for functions with many parameters. 
check file `keyword_args.py` for an example.

## Default Values
- Parameters can be passed with default values within function definition.
- check file `default_val.py` for an example.

## Return Values
- Are the values that a function sends back to the caller after execution.
- They are specified using **return** statement in Python.
check `return_val.py` file for an example.