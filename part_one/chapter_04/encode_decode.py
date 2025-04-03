if __name__ == "__main__":
    print("##### encode, decode #####")
    s = 'café'
    print(f"{len(s) = }")
    b = s.encode('utf8')
    print(f"{b = }, {len(b) = }")
    print(f"{b.decode('utf8') = }")
    print()

    print("##### bytes, bytearray #####")
    cafe = bytes('café', encoding='utf-8')
    print(f"{cafe = }, {type(cafe) = }")
    print(f"{cafe[0] = }")      # integer 0-255
    print(f"{chr(cafe[0]) = }")
    print(f"{cafe[:1] = }")     # binary sequence

    cafe_arr = bytearray(cafe)
    print(f"{cafe_arr = }, {type(cafe_arr) = }")
    print(f"{cafe_arr[-1] = }")     # integer 0-255
    print(f"{cafe_arr[-1:] = }")    #   binary sequence
    cafe_arr[0] = 100
    print(f"{cafe_arr = }")
    print()

    print("##### codecs #####")
    for codec in ['latin_1', 'utf_8', 'utf_16']:
        print(codec, 'El Niño'.encode(codec), sep='\t')
    print()

    print("##### UnicodeEncodeError #####")
    city = 'São Paulo'
    print(f"{city = }")
    for codec in ['utf_8', 'utf_16', 'iso8859_1', 'cp437']:
        try:
            print(f"{codec = }, {city.encode(codec) = }")
        except UnicodeEncodeError as err:
            print(f"{codec = }, {err = }")
    print()
    for handler in ['ignore', 'replace', 'xmlcharrefreplace']:
        try:
            print(f"{handler = }, {city.encode('cp437', errors=handler) = }")
        except UnicodeEncodeError as err:
            print(f"{handler = }, {err = }")
    print()

    print("##### UnicodeDecodeError #####")
    octets = b'Montr\xe9al'
    print(f"{octets = }")
    for codec in ['cp1252', 'iso8859_7', 'koi8_r', 'utf_8']:
        try:
            print(f"{codec = }, {octets.decode(codec) = }")
        except UnicodeDecodeError as err:
            print(f"{codec = }, {err = }")
    print(f"{octets.decode('utf_8', errors='replace') = }")
    print()
