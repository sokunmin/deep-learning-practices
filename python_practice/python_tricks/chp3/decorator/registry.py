registry = []


def register(func):
    print('> running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    return 'running f1()'


@register
def f2():
    return 'running f2()'


def f3():
    return 'running f3()'


def main():
    print('running main()')
    print('registry -> ', registry)
    print()
    print(f1())
    print(f2())
    print(f3())


if __name__ == '__main__':
    main()
