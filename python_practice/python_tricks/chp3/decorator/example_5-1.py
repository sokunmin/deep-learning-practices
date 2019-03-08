

# ----------------- Debuggable Decorators ----------------- #
def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper


# [1] metadata attached to original function is hidden
def greet():
    """return a friendly greeting. """
    return 'Hi, there!'


print(greet.__name__)
print(greet.__doc__)

decorated_greet = uppercase(greet)
print(decorated_greet.__name__)
print(decorated_greet.__doc__)
