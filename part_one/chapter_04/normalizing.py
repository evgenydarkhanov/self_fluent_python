from unicodedata import normalize, name


if __name__ == "__main__":
    s1 = 'café'
    s2 = 'cafe\N{COMBINING ACUTE ACCENT}'
    print(f"{s1 = }, {s2 = }")
    print(f"{len(s1) = }, {len(s2) = }")
    print(f"{s1 == s2 = }")
    print()

    print(f"{len(normalize('NFC', s1)) = }, {len(normalize('NFC', s2)) = }")
    print(f"{len(normalize('NFD', s1)) = }, {len(normalize('NFD', s2)) = }")
    print(f"{normalize('NFC', s1) == normalize('NFC', s2) = }")
    print(f"{normalize('NFD', s1) == normalize('NFD', s2) = }")
    print()

    micro = 'µ'
    print(f"{micro = }")
    print(f"{name(micro) = }")
    micro_cf = micro.casefold()
    print(f"{micro_cf = }")
    print(f"{name(micro_cf) = }")

    eszett = 'ß'
    print(f"{eszett = }")
    print(f"{name(eszett) = }")
    eszett_cf = eszett.casefold()
    print(f"{eszett_cf = }")
