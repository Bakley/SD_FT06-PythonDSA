'''
Recap
-> Intro to python/ basics
* List, tuples, functions, variables, 
-> Data structures
-> Comprehension in python
** list, set, & dictionary
-> fundamentals in OOP
* Principles of OOP
** getter & setter
** Inheritance is 
** Encapsulation
** Abstraction
** Magic methods
** super keyword
** constructors __init__
Decorators
Anonymous functions - lambda

*********
scope
big O Notation
Nested objects 
'''

# #### Decorators
"""
1. Takes a function as an argument.
2. Has an inner function defined inside of it.
3. Returns the inner function.
"""

def time(func):
    def wrapper(*args):
        # invokes the function that has been passed
        # takes the function parameters
        print("I am the output that lets you know the function is about to be called.")
        some_var = func(*args)
        print(some_var, "I am the output that lets you know the function has been called.")


    return wrapper


@time
def addition(x,y):
    return x + y

@time
def even_digits(x) -> list[int]:
    new_Arry = [x[item] for item in range(len(x)) if x[item] % 2 == 0]
            
    return new_Arry


print(addition(2,3))
print(even_digits([2,3,44,55,66,777,88,324]))
