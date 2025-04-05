import copy


if __name__ == "__main__":
    print("##### tuple #####")
    t1 = (1, 2, 3)
    t2 = tuple(t1)
    t3 = t1[:]
    t4 = copy.copy(t1)
    t5 = (1, 2, 3)
    t6 = tuple([1, 2, 3])
    print(f"{t2 is t1 = }")
    print(f"{t3 is t1 = }")
    print(f"{t4 is t1 = }")
    print(f"{t5 is t1 = }")
    print(f"{t6 is t1 = }")
    print()

    print("##### str #####")
    s1 = 'ABC'
    s2 = str(s1)
    s3 = s1[:]
    s4 = copy.copy(s1)
    s5 = 'ABC'
    s6 = str(['A', 'B', 'C'])
    print(f"{s2 is s1 = }")
    print(f"{s3 is s1 = }")
    print(f"{s4 is s1 = }")
    print(f"{s5 is s1 = }")
    print(f"{s6 is s1 = }")
    print()

    print("##### bytes #####")
    b1 = bytes('ABC', encoding='utf8')
    b2 = b1[:]
    b3 = copy.copy(b1)
    b4 = bytes('ABC', encoding='utf8')
    b5 = bytes(''.join(['A', 'B', 'C']), encoding='utf8')
    print(f"{b2 is b1 = }")
    print(f"{b3 is b1 = }")
    print(f"{b4 is b1 = }")
    print(f"{b5 is b1 = }")
    print()

    print("##### frozenset #####")
    fs1 = frozenset([1, 2, 3])
    fs2 = frozenset(fs1)
    fs3 = fs1.copy()
    fs4 = copy.copy(fs1)
    fs5 = frozenset({1, 2, 3})
    fs6 = frozenset([1, 2, 3])
    print(f"{fs2 is fs1 = }")
    print(f"{fs3 is fs1 = }")
    print(f"{fs4 is fs1 = }")
    print(f"{fs5 is fs1 = }")
    print(f"{fs6 is fs1 = }")
    print()
