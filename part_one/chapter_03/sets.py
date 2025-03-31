from collections.abc import Collection, Set, MutableSet


if __name__ == "__main__":
    a = list(range(3))
    b = tuple(range(4, 7))
    c = set(range(8, 11))
    d = {*a, *b, *c}
    e = frozenset(d)
    print(f"{d = }, {e = }")
    print(f"{id(d) = }, {id(e) = }")
    print(f"{isinstance(d, Set) = }, {isinstance(e, Set) = }")
    print(f"{isinstance(d, MutableSet) = }, {isinstance(e, MutableSet) = }")
    print(f"{isinstance(d, Collection) = }, {isinstance(e, Collection) = }")
    print()

    d1 = dict(a=1, b=2, c=3)
    d2 = {'b': 3, 'c': 4, 'd': 5}
    print(f"{d1.keys() & d2.keys() = }")
    print(f"{type(d1.keys() & d2.keys()) = }")
