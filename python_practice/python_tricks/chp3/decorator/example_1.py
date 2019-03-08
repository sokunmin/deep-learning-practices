

# ----------------- Decorator Basics ----------------- #
def null_decorator(func):
    print('> null_decorator is executed from ', func.__name__)
    return func


# def undecorated_greet():
#     return 'Hi, there!'


@null_decorator
def decorated_greet():
    return 'Hi, there!'


# [1]
# greet = null_decorator(undecorated_greet)
# print(greet())

# [2]
print(decorated_greet())