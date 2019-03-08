from collections import namedtuple


def method1():
    Car = namedtuple('Car', 'color mileage')

    class MyCarWithMethods(Car):
        def hexcolor(self):
            if self.color == 'red':
                return '#ff0000'
            else:
                return '#000000'

    c = MyCarWithMethods('red', 1234)
    print(c.hexcolor())


def method2():
    Car = namedtuple('Car', 'color mileage')
    ElectricCar = namedtuple('ElectricCar', Car._fields + ('change',))
    print(ElectricCar('red', 1234, 45.0))


if __name__ == '__main__':
    method1()
    method2()
