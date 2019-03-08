from python_practice.chp3.first_class.example_1 import bark


def _example2():
    funcs = [
        bark,  # output UPPERCASE
        str.lower,  # output lowercase
        str.capitalize  # output Capitalize
    ]

    # [1]
    print('[1] ', funcs)

    # [2]
    for f in funcs:
        print('[2]', f, f('Hello'))

    # [3]
    print('[3] ', funcs[0]('Hello'))


if __name__ == '__main__':
    _example2()
