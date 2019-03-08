from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass


class Concrete:
    def foo(self):
        pass


if __name__ == '__main__':

    assert issubclass(Concrete, Base)

    c = Concrete()
    # TypeError: Can't instantiate abstract class Concrete
    # with abstract methods bar
