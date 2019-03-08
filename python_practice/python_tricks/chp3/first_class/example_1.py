
def yell(text):
    return text.upper() + '!'


print(yell('Hello'))

bark = yell


def _example1():
    # [1]
    print(bark('Hello'))

    # [2]
    # del yell
    # print(yell('Hello'))
    print('[2]', bark('Hello'))

    # [3]
    print('[3-1] ', bark.__name__)
    print('[3-2] qualified name: ', bark.__qualname__)


if __name__ == '__main__':
    _example1()