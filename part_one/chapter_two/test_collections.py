from collections import abc


if __name__ == "__main__":
    # container and flat sequences; mutable and immutable sequences
    print(f"{issubclass(tuple, abc.Sequence) = }")
    print(f"{issubclass(tuple, abc.MutableSequence) = }")
    print(f"{issubclass(list, abc.Sequence) = }")
    print(f"{issubclass(list, abc.MutableSequence) = }")
    print()

    # scope
    x = 'ABC'
    codes = [ord(x) for x in x]
    print(f"{x = }")
    print(f"{codes = }")
    codes = [last := ord(c) for c in x]
    print(f"{last = }")
    try:
        print(f"{c = }")
    except NameError as ne:
        print(ne)
    print()

    # cartesian
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    t_shirts = [(color, size) for color in colors for size in sizes]
    print(t_shirts)
    print()

    # genexp yields items one by one
    # six-item list of T-shirts is never built in memory
    for t_shirt in (f'{c} {s}' for c in colors for s in sizes):
        print(t_shirt)
