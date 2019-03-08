import copy


class Point:
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def __repr__(self):
        return f'Point({self.x!r}, {self.y!r})'


class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright

    def __repr__(self):
        return (f'Rectangle({self.topleft!r}, '
                f'{self.bottomright!r})')


if __name__ == '__main__':
    a = Point(32, 42)
    b = copy.copy(a)
    print('a: ', a)
    print('b: ', b)
    print(a is b)
    print()
    rect = Rectangle(Point(0, 1), Point(5, 6))
    # shallow copy
    srect = copy.copy(rect)
    print('[1] rect: ', rect)
    print('[1] srect: ', srect)
    print(rect is srect)
    rect.topleft.x = 999
    print('[2] rect: ', rect)
    print('[2] srect: ', srect)
    print()

    # deep copy
    drect = copy.deepcopy(srect)
    drect.topleft.x = 222
    srect.topleft.x = 333
    print('[3] rect: ', rect)
    print('[3] srect: ', srect)
    print('[3] drect: ', drect)

