def foo(value):
    if value:
        return value
    else:
        return None


def foo2(value):
    """Bare return statement implies `return None`"""
    if value:
        return value
    else:
        return


def foo3(value):
    """Missing return statement implies `return None`"""
    if value:
        return value


print('[1-1] ', type(foo(0)))
print('[1-2] ', (foo(0)))
print('[2-1] ', type(foo2(0)))
print('[2-2] ', (foo2(0)))
print('[3-1] ', type(foo3(0)))
print('[3-2] ', (foo3(0)))