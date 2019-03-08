class Base:
    def foo(self):
        raise NotImplementedError

    def bar(self):
        raise NotImplementedError


class Concrete:
    def foo(self):
        return 'foo() called'

    # Oh no, we forgot to override bar()...
    # def bar(self):
    #     return "bar() called"


if __name__ == '__main__':
    # [1] base class
    b = Base()
    b.foo() # Error

    # [2] derived class
    c = Concrete()
    c.foo()
    # c.bar() # Error
