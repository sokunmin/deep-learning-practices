import copy


def builtin_copy():
    """
        This won't work for custom objects
        It only creates `shallow copies`
    """
    original_list = [1, 2, 3]
    original_dict = {'a': 1, 'b': 2, 'c': 3}
    original_set = {'a', 'b', 'c'}
    new_list = list(original_list)
    new_dict = list(original_dict)
    new_set = list(original_set)


def shallow_copy():
    """
        We only created a shallow copy of the original list, ys still
        contains references to the original child objects stored in xs.
        These children were not copied.

        They were merely referenced again in the copied list.
    """
    xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ys = list(xs) # make a shallow copy
    zs = copy.copy(xs)
    xs.append(['new list'])
    print('[1] xs: ', xs)
    print('[1] ys: ', ys)
    print('[1] zs: ', zs)
    print('----- modify one of children -----')
    xs[1][0] = 'X'
    print('[2] xs: ', xs)
    print('[2] ys: ', ys)
    print('[2] zs: ', zs)


def deep_copy():
    xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ys = copy.deepcopy(xs)
    print('[1] xs: ', xs)
    print('[1] ys: ', ys)
    print('----- modify one of children -----')
    xs[1][0] = 'X'
    print('[2] xs: ', xs)
    print('[2] ys: ', ys)


if __name__ == '__main__':
    # builtin_copy()
    shallow_copy()
    print()
    deep_copy()