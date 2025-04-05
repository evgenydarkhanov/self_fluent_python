import weakref


def bye():
    print('...like tears in the rain.')


if __name__ == "__main__":
    s1 = {1, 2, 3}
    s2 = s1
    ender = weakref.finalize(s1, bye)
    print(f"{ender.alive = }")
    del s1
    print(f"{ender.alive = }")
    s2 = 'spam'
    print(f"{ender.alive = }")
