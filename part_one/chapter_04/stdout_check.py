import sys
from unicodedata import name


if __name__ == "__main__":
    print(f"{sys.version = }")
    print()
    print(f"{sys.stdout.isatty() = }")
    print(f"{sys.stdout.encoding = }")
    print()

    test_chars = [
        '\N{HORIZONTAL ELLIPSIS}',
        '\N{INFINITY}',
        '\N{CIRCLED NUMBER FORTY TWO}',
    ]

    for char in test_chars:
        print(f"trying to output {name(char)}: {char}")
