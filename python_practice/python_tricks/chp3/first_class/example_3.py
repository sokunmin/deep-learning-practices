# [1]
def make_adder(n):
    def add(x):
        return x + n

    return add


plus_3 = make_adder(3)
plus_5 = make_adder(5)

print(plus_3(4))
print(plus_5(4))


# [2]
class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x


plus_3 = Adder(3)
plus_3(4)

print(callable(plus_3))
print(callable('Hello'))


# [3]
def make_adder2(n):
    return lambda x: x + n


plus_3 = make_adder2(3)
plus_5 = make_adder2(5)


print(plus_3(4))
print(plus_5(4))
