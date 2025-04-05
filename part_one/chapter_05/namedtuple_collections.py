from collections import namedtuple


City = namedtuple('City', 'name country population coordinates')
Coordinate = namedtuple('Coordinate', 'lat lon')

if __name__ == "__main__":
    tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
    print(f"{tokyo = }")
    print(f"{tokyo[1] = }")
    print(f"{City._fields = }")

    delhi_data = ('Delhi NCR', 'IN', 21.935, Coordinate(28.613889, 77.208889))
    delhi = City._make(delhi_data)
    print(f"{delhi._asdict() = }")

