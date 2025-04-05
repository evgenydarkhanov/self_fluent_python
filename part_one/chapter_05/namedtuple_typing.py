from typing import NamedTuple


class DemoPlainClass:
    a: int
    b: float = 1.1
    c = 'spam'


class DemoNTClass(NamedTuple):
    a: int
    b: float = 1.1
    c = 'spam'


if __name__ == "__main__":
    print("##### Type Hints #####")
    print(f"{DemoPlainClass.__dict__ = }")
    print(f"{DemoPlainClass.__annotations__ = }")
    try:
        print(f"{DemoPlainClass.a = }")
    except AttributeError as err:
        print(err)
    print()

    print("##### NamedTuple #####")
    print(f"{DemoNTClass.__dict__ = }")
    print(f"{DemoNTClass.__annotations__ = }")
    print(f"{DemoNTClass.a = }")
    print(f"{DemoNTClass.b = }")
    print(f"{DemoNTClass.c = }")
    print(f"{DemoNTClass.__doc__ = }")

    nt = DemoNTClass(8)
    try:
        nt.a = 9
    except AttributeError as err:
        print(err)
    try:
        nt.b = 9.1
    except AttributeError as err:
        print(err)
    try:
        nt.c = 'nospam'
    except AttributeError as err:
        print(err)
    try:
        nt.z = 9
    except AttributeError as err:
        print(err)
