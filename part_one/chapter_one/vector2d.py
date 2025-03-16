import math


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # dunder-method for getting the string representation of the object
    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r})"

    def __abs__(self):
        return math.hypot(self.x, self.y)

    # if __bool__ is not implemented, Python tries to invoke x.__len__()
    # len(x) --> 0 --> False, otherwise --> True
    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == "__main__":
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    print(f"{v1 + v2 = }")

    v = Vector(3, 4)
    print(f"{abs(v) = }")
    print(f"{v * 3 = }")
    print(f"{abs(v * 3) = }")
