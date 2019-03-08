class Car1:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


# [1]
my_car = Car1('red', 1234)
print(my_car)


# output: <__main__.Car1 object at 0x102a2a0f0>


# [2]
class Car2:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f'a {self.color} car'


my_car = Car2('red', 1234)
print(my_car)


# [3]
class Car3:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return '__str__ for Car3'

    def __repr__(self):
        return '__repr__ for Car3'


my_car = Car3('blue', 1234)
print(str(my_car))

# print result at Python interpreter session.
print([my_car])
# containers like lists or dicts always use
# the result of __repr__ to represent the object they contain

# it's best to use the built-in str() and repr() functions
# using them is preferable over calling the object's __str__ and __repr__.
print(str(my_car))
print(repr(my_car))

# [4] create datetime.date to find out how to
#  use __str__ and __repr__ to control string conversion.
import datetime

today = datetime.date.today()
print(str(today))
print(repr(today))


# [4]
class Car4:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        # [4-1]
        # return f'[4-1] {self.__class__.__name__}({self.color}, {self.mileage})'

        # [4-2]
        return f'[4-2] {self.__class__.__name__}({self.color!r}, {self.mileage!r})'

    def __str__(self):
        return f'[4-str] a {self.color} car'


my_car = Car4('black', 1234)
print(my_car)
print(repr(my_car))
print(str(my_car))
