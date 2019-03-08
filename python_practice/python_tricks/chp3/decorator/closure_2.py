import inspect


def make_averager():
    print('> ', inspect.stack()[0][3])
    series = []

    def averager(new_value):
        print('> ', inspect.stack()[0][3])
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))

print('[1] ', avg.__code__.co_varnames)
print('[2] ', avg.__code__.co_freevars)
print('[3] ', avg.__closure__)
print('[4] ', avg.__closure__[0].cell_contents)
