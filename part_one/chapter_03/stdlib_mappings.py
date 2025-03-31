import builtins
from collections import ChainMap, UserDict
from types import MappingProxyType


class CustomDict(UserDict):
    pass


if __name__ == "__main__":
    print(f"##### ChainMap #####")
    d1 = dict(a=1, b=2)
    d2 = {'a': 2, 'b': 4, 'c': 6}
    chain = ChainMap(d1, d2)
    print(f"{chain = }")
    print(f"{chain['a'] = }")
    print(f"{chain['b'] = }")

    # chain only stores refs
    print(f"{len(chain) = }")

    for elem in chain:
        print(f"{elem = }, {chain[elem] = }")

    # updates only affects the first input
    print(f"{chain['c'] = }")
    chain['c'] = -1
    print(f"{d1 = }")
    print(f"{d2 = }")
    print(f"{chain['c'] = }")
    # pylookup = ChainMap(locals(), globals(), vars(builtins))
    # print(f"{pylookup = }")
    print()

    print("##### UserDict #####")
    user_dict = UserDict()
    custom_dict = CustomDict()
    print(f"{user_dict.data = }, {type(user_dict.data) = }")
    print(f"{custom_dict.data = }, {type(custom_dict.data) = }")
    print(f"{isinstance(user_dict, dict) = }")
    print(f"{issubclass(UserDict, dict) = }")
    print(f"{issubclass(dict, UserDict) = }")
    print()

    print("##### MappingProxyType #####")
    d = {1: 'A'}
    d_proxy = MappingProxyType(d)
    print(f"{id(d) = }, {id(d_proxy) = }")
    print(f"{d = }, {d_proxy = }")

    # changing
    try:
        d_proxy[1] = 'B'
    except TypeError as e:
        print(e)

    # updating
    try:
        d_proxy[2] = 'B'
    except TypeError as e:
        print(e)

    d[2] = 'b'
    print(f"{id(d) = }, {id(d_proxy) = }")
    print(f"{d = }, {d_proxy = }")
    print()
