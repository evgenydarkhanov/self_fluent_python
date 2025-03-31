from collections import abc, UserDict


def dump(**kwargs):
    return kwargs


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == "__main__":
    print("##### kwargs #####")
    print(f"{dump(**{'x': 1}, y=2, **{'z': 3})}")
    tmp_dict = {
        'a': 0,
        **{'x': 1},
        'y': 2,
        **{'z': 3, 'x': 4}
    }
    print(f"{tmp_dict = }")
    print()

    print("##### merging #####")
    d1 = {'a': 1, 'b': 2}
    d2 = {'a': 1, 'b': 4, 'c': 6}
    print(f"{d1 | d2 = }")
    print()

    print("##### datatypes #####")
    my_dict = {}
    print(f"{isinstance(my_dict, abc.Mapping) = }")
    print(f"{isinstance(my_dict, abc.MutableMapping) = }")
    print(f"{UserDict.__dict__ = }")
    print()

    print("##### hashing #####")
    person = Person('Steve', 25)
    print(f"{id(person) = }")
    print(f"{hash(person) = }")
    print()
