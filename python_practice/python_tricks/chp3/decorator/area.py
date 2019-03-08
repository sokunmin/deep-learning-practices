# @classmethod vs. @staticmethod
# https://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod


class Area(object):
    def __init__(self, default_x, default_y):
        # pass
        self.default_x = default_x
        self.default_y = default_y

    def calc(self, x, y):
        return x * y

    @classmethod
    def calc_cls(cls, x, y):
        return x * y

    @staticmethod
    def calc_static(x, y):
        return x * y


# area = Area(10, 10)
# print(Area.calc(10, 10))

def print_func(func):
    print('> ', func.__name__)

    def wrapper():
        return func
    return wrapper()


@print_func
def f3(x, y, z):
    v = x**2 + y**2 + z**2
    return v


@print_func
def f2(x, y):
    z = (x + y) * 10
    return f3(x, y, z)


@print_func
def f1(x):
    return f2(x, 3)


print(f1(10))