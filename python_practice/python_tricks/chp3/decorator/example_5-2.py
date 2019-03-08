
import functools


# [2] copy lost metadata from undecorated function to
# the decorator closure using functools.wraps
def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper


@uppercase
def greet():
    """return a friendly greeting."""
    return 'Hi, there!'


print(greet.__name__)
print(greet.__doc__)

decorated_greet = uppercase(greet)
print(decorated_greet.__name__)
print(decorated_greet.__doc__)
