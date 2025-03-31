import re
import sys
from collections import defaultdict


def print_index(index, k: int = 5) -> None:
    for i, word in enumerate(sorted(index, key=str.upper)):
        if i > k:
            break
        print(word, index[word])


WORD_RE = re.compile(r'\w+')


if __name__ == "__main__":
    print("##### index by dict #####")
    index = {}

    with open(sys.argv[1], encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, start=1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)
                # ugly moment
                occurences = index.get(word, [])
                occurences.append(location)
                index[word] = occurences

    print_index(index)
    print()

    print("##### index by dict.setdefault() #####")
    index = {}

    with open(sys.argv[1], encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, start=1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)
                # better
                index.setdefault(word, []).append(location)

    print_index(index)
    print()

    print("##### index by defaultdict #####")
    index = defaultdict(list)

    with open(sys.argv[1], encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, start=1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)
                # best
                index[word].append(location)

    print_index(index)
    print(f"{index.default_factory = }")
    print()
