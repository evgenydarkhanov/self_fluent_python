if __name__ == "__main__":
    # tuples as records
    lax_coords = (33.9425, -118.408056)
    city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)

    traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
    for passport in traveler_ids:
        print('%s/%s' % passport)
    print()

    for country, _ in traveler_ids:
        print(country)
    print()

    metro_areas = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]

    # works in Python >= 3.10
    print(f'{"":15} | {"latutide":>9} | {"longitude":>9}')
    for record in metro_areas:
        match record:
            case [name, _, _, (lat, lon)] if lon <= 0:
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')
