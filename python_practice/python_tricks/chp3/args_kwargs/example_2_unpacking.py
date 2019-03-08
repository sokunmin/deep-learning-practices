def print_vector(x, y, z):
    print('<%s, %s, %s>' % (x, y, z))


# [1]
print('--------- [1] ---------')
tuple_vec = (1, 0, 1)
list_vec = [1, 0, 1]

print_vector(1, 2, 3)
print_vector(*tuple_vec)

# [2]
print('--------- [2] ---------')
genexpr = (x * x for x in range(3))
print('[2-1] genexpr = ', genexpr)
print('[2-2] genexpr = ', type(genexpr))
# print('[2-3] genexpr = ', *genexpr)
print_vector(*genexpr)

# [3]
print('--------- [3] ---------')
dict_vec = {'y': 0, 'z': 1, 'x': 1}
print_vector(**dict_vec)
print_vector(*dict_vec)