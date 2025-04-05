import copy


class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


class HauntedBus:
    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


class TwilightBus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


if __name__ == "__main__":
    print("##### Bus #####")
    bus1 = Bus(['Alice', 'Bill', 'Charlie', 'David'])
    bus2 = copy.copy(bus1)
    bus3 = copy.deepcopy(bus1)
    print(f"{id(bus1)=}, {id(bus2)=}, {id(bus3)=}")
    bus1.drop('Bill')
    print(f"{bus2.passengers = }")
    print(f"{id(bus1.passengers)=}, {id(bus2.passengers)=}, {id(bus3.passengers)=}")
    print(f"{bus3.passengers = }")
    print()

    print("##### HauntedBus #####")
    bus1 = HauntedBus(['Alice', 'Bill'])
    print(f"{bus1.passengers = }")
    bus1.pick('Charlie')
    bus1.drop('Alice')
    print(f"{bus1.passengers = }")
    bus2 = HauntedBus()
    bus2.pick('Carrie')
    print(f"{bus2.passengers = }")
    bus3 = HauntedBus()
    print(f"{bus3.passengers = }")
    bus3.pick('Dave')
    print(f"{bus2.passengers = }")
    print(f"{bus2.passengers is bus3.passengers = }")
    print(f"{bus1.passengers = }")
    print()

    print("##### TwilightBus #####")
    basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
    bus = TwilightBus(basketball_team)
    bus.drop('Tina')
    bus.drop('Pat')
    print(f"{basketball_team = }")
    print()
