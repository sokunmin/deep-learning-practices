import timeit

# ----------------- Example 1: Decorator Basics ----------------- #
def null_decorator(func):
    print('> null_decorator is executed')
    return func


# ----------------- Modify Behavior ----------------- #
# The wrapper closure has access to undecorated input function
# and it is free to execute additional code before and after
# calling the input function.
def uppercase(func):
    print('> before calling wrapper closure.')
    # Define a new function on the fly. Use it to wrap
    # the input function in order to modify its behavior at call time.

    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper


@uppercase
def greet():
    return 'Hi, there!'

print(greet())

# print reference addresses
print(greet)
print(null_decorator(greet))
print(uppercase(greet))