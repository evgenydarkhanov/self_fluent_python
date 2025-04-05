from dataclasses import dataclass, field
from typing import ClassVar


@dataclass
class DemoDataClass:
    a: int
    b: float = 1.1
    c = 'spam'


@dataclass
class ClubMember:
    name: str
    guests: list[str] = field(default_factory=list)


@dataclass
class HuckerClubMember(ClubMember):
    all_handles: ClassVar[set[str]] = set()     # for mypy
    handle: str = ''

    def __post_init__(self):
        cls = self.__class__
        if self.handle == '':
            self.handle = self.name.split()[0]
        if self.handle in cls.all_handles:
            msg = f'handle {self.handle!r} already exists'
            raise ValueError(msg)
        cls.all_handles.add(self.handle)


if __name__ == "__main__":
    print("##### dataclass #####")
    print(f"{DemoDataClass.__annotations__ = }")
    print(f"{DemoDataClass.__doc__ = }")
    try:
        print(f"{DemoDataClass.a = }")
    except AttributeError as err:
        print(err)
    print(f"{DemoDataClass.b = }")
    print(f"{DemoDataClass.c = }")
    print()

    print("##### field, default factory #####")
    try:
        @dataclass
        class ClubMember:
            name: str
            guests: list = []
    except ValueError as err:
        print(err)
