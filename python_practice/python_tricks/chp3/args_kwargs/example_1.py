import functools


# [1]
def foo(required, *args, **kwargs):
    print(required)
    if args:
        # tuple
        print(args)

    if kwargs:
        # dictionary
        print(kwargs)


def foo2(x, *args, **kwargs):
    kwargs['name'] = 'Alex'
    new_args = args + ('extra',)
    foo(x, *new_args, **kwargs)


foo('hello', 1, 2, 3, key1='value', key2=999)
print('----------------------')
foo2('hello', 1, 2, 3, key1='value', key2=999)


# [2]
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


class AlwaysBlueCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = 'blue'


print(AlwaysBlueCar('green', 1234).color)


# [3]

def trace(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        print(f'`{f}`, `{args}`, `{kwargs}`')
        result = f(*args, **kwargs)
        print(f'result={result}')

    return decorated_function


@trace
def greet(greeting, name):
    return '{}, {}!'.format(greeting, name)


greet('Hello', 'Chun-Ming')