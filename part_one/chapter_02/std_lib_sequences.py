from array import array
from random import random
from collections import deque


if __name__ == "__main__":
    print("##### array #####")
    floats = array('d', (random() for _ in range(10)))
    print(f"id floats before changing: {id(floats)}")
    print(f"{floats[-1] = }")
    print(f"{len(floats) = }")

    floats.append(12.0)     # appending
    floats[-2] = 99.0       # changing values

    print(f"{floats[-2] = }")
    print(f"{floats[-1] = }")
    print(f"id floats after changing: {id(floats)}")
    print(f"{len(floats) = }")
    print()

    print("##### memoryview #####")
    numbers = array('B', range(6))
    print(f"numbers before changing through memoryview: {numbers}")

    m1 = memoryview(numbers)
    print(f"{id(m1) = }")
    print(f"{m1.tolist() = }")

    # memorycast returning another object, but sharing the same memory
    m2 = m1.cast('B', [2, 3])   # bytes, shape == [2, 3]
    print(f"{id(m2) = }")
    print(f"{m2.tolist() = }")

    m3 = m1.cast('B', [3, 2])
    print(f"{id(m3) = }")
    print(f"{m3.tolist() = }")

    # changing values in memoryview
    m2[1, 1] = 22
    m3[1, 1] = 33
    print(f"numbers after changing through memoryview: {numbers}")
    print()

    print("##### deque #####")
    dq = deque(range(10), maxlen=10)    # limitation
    print(f"{dq = }")
    dq.rotate(3)
    print(f"{dq = }")
    dq.rotate(-4)
    print(f"{dq = }")
    dq.appendleft(-1)
    print(f"{dq = }")
    dq.extend([11, 22, 33])
    print(f"{dq = }")
    dq.append(-1)
    print(f"{dq = }")
    dq.extendleft([10, 20, 30, 40])
    print(f"{dq = }")
    print(f"{dq[6] = }")
    dq[6] = 100
    print(f"{dq[6] = }")
    print(f"{dq = }")
    print()

    print("##### sorting with 'key=int' and 'key=str' #####")
    l = [28, 14, '28', 5, '9', '1', 0, 6, '23', 19]
    print(f"{l = }")
    print(f"{sorted(l, key=int) = }")
    print(f"{sorted(l, key=str) = }")
