import json
from collections import namedtuple


def method1():
    Car = namedtuple('Car', 'color mileage')
    my_car = Car('red', 1234)
    print(my_car._asdict())

    # generate JSON-output
    json.dump(my_car._asdict())

    # create a copy of a tuple,
    # selectively replace some of its fields
    print(my_car._replace(color='blue'))

    # create a new instance of a namedtuple
    # from a sequence or iterable
    print(my_car._make(['red', 999]))


if __name__ == '__main__':
    method1()
