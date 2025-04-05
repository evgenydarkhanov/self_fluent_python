from collections import namedtuple
from typing import NamedTuple
from dataclasses import dataclass


class Coordinate:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


CoordinateNT = namedtuple('CoordinateNT', 'lat lon')
CoordinateNT_ = NamedTuple('CoordinateNT_', [('lat', float), ('lon', float)])


class CoordinateMeta(NamedTuple):
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


@dataclass(frozen=True)
class CoordinateDataclass:
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


if __name__ == "__main__":
    print("##### class #####")
    moscow = Coordinate(55.76, 37.62)
    print(f"{moscow = }")
    location = Coordinate(55.76, 37.62)
    print(f"{location == moscow = }")
    print(f"{(location.lat, location.lon) == (moscow.lat, moscow.lon) = }")
    print()

    print("##### namedtuple #####")
    print(f"{issubclass(CoordinateNT, tuple) = }")
    moscow = CoordinateNT(55.756, 37.617)
    print(f"{moscow = }")
    location = CoordinateNT(55.756, 37.617)
    print(f"{location == moscow = }")
    print()

    print("##### NamedTuple #####")
    print(f"{issubclass(CoordinateNT_, tuple) = }")
    moscow = CoordinateNT_(55.756, 37.617)
    print(f"{moscow = }")
    location = CoordinateNT_(55.756, 37.617)
    print(f"{location == moscow = }")
    print()

    print("##### NamedTupleMeta #####")
    print(f"{issubclass(CoordinateMeta, tuple) = }")
    moscow = CoordinateMeta(55.756, 37.617)
    print(f"{moscow = }")
    print(f"{str(moscow) = }")
    location = CoordinateMeta(55.756, 37.617)
    print(f"{location == moscow = }")
    print()

    print("##### dataclass #####")
    print(f"{issubclass(CoordinateDataclass, tuple) = }")
    moscow = CoordinateDataclass(55.756, 37.617)
    print(f"{moscow = }")
    print(f"{str(moscow) = }")
    location = CoordinateDataclass(55.756, 37.617)
    print(f"{location == moscow = }")
    print()
