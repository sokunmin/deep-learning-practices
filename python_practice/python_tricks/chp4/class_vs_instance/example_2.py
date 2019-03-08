
class CountedObject:
    # When the class is declared, it initializes
    # the counter to zero and then leaves it alone.
    num_instances = 0

    def __init__(self):
        self.__class__.num_instances += 1


def method1():
    print(CountedObject.num_instances)
    print(CountedObject().num_instances)
    print(CountedObject().num_instances)
    print(CountedObject().num_instances)
    print(CountedObject.num_instances)


# WARNING: This implementation contains a bug
class BuggyCountedObject:
    num_instances = 0

    def __init__(self):
        self.num_instances += 1  # !!!


def method2():
    print(BuggyCountedObject.num_instances)
    print(BuggyCountedObject().num_instances)
    print(BuggyCountedObject().num_instances)
    print(BuggyCountedObject().num_instances)
    print(BuggyCountedObject.num_instances)


if __name__ == '__main__':
    method1()
    print()
    method2()