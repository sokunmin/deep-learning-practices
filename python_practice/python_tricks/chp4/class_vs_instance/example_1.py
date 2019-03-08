"""

Class variables are declared inside the class definition (but outside of any instance methods).
They’re not tied to any particular instance of a class. Instead, class variables store their
contents on the class itself, and all objects created from a particular class share access to
the same set of class variables. This means, for example, that modifying a class variable
affects all object instances at the same time.

Instance variables are always tied to a particular object instance. Their contents are not
stored on the class, but on each individual ob- ject created from the class. Therefore, the
contents of an instance vari- able are completely independent from one object instance to
the next. And so, modifying an instance variable only affects one object instance at a time.

"""


class Dog:
    num_legs = 4 # <- Class variable

    def __init__(self, name):
        self.name = name # <- Instance variable


def method1():
    jack = Dog('Jack')
    jill = Dog('Jill')
    print(jack.name, jill.name)
    print(Dog.num_legs, jack.num_legs, jill.num_legs)

    # Error: if you try to access an instance variable through the class,
    # it’ll fail with an AttributeError.

    # Instance variables are specific to each object instance and are created
    # when the __init__ constructor runs—they don’t even exist on the class itself.
    # TODO: uncoment it and test.
    # print(Dog.name)

    # add legs to the Dog
    Dog.num_legs = 6
    addr = lambda r: hex(id(r)) # get memory address
    print(Dog.num_legs, jack.num_legs, jill.num_legs)
    print(addr(Dog.num_legs), addr(jack.num_legs), addr(jill.num_legs))

    Dog.num_legs = 4
    jack.num_legs = 6
    print(Dog.num_legs, jack.num_legs, jill.num_legs)
    print(addr(Dog.num_legs), addr(jack.num_legs), addr(jill.num_legs))

    # And now the new num_legs instance variable “shadows” the
    # class variable of the same name, overriding and
    # hiding it when we access the object instance scope:
    print(jack.num_legs, jack.__class__.num_legs)
    print(addr(jack.num_legs), addr(jack.__class__.num_legs))



if __name__ == '__main__':
    method1()