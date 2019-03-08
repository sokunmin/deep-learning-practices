from collections import namedtuple


def run_regular_tuple():
    tup = ('hello', object(), 42)
    print(tup)
    print(tup[2])
    # tup[2] = 33 # Error


def run_namedtuples():
    Car = namedtuple('Car', 'color mileage')
    # [1] parse this into a list of field names
    print('color mileage'.split())

    # [2]
    Car = namedtuple('Car', [
        'color',
        'mileage'
    ])

    # [3] test
    my_car = Car('red', 3812.4)
    print('[3-1] ', my_car.color)
    print('[3-2] ', my_car.mileage)
    print('[3-3] ', my_car[0])
    print('[3-4] ', tuple(my_car))
    color, mileage = my_car
    print('[3-5] ', color, mileage)
    print('[3-6] ', *my_car)
    print('[3-7] ', my_car)

    # [4] namedtuples are immutable, it raises an error
    # if you try to overwrite one of the fields.
    my_car.color = 'blue'


if __name__ == '__main__':
    run_namedtuples()