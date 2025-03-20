invoice = """
0.....6.................................40........52...55........
1909  Pimoroni PiBrella                     $17.50    3    $52.50
1489  6mm Tactile Switch x20                 $4.95    2     $9.90
1510  Panavise Jr. - PV-201                 $28.00    1    $28.00
1601  PiTFT Mini Kit 320x240                $34.95    1    $34.95
"""


if __name__ == "__main__":
    # one can create slice object
    SKU = slice(0, 6)
    DESCRIPTION = slice(6, 40)
    UNIT_PRICE = slice(40, 52)
    QUANTITY = slice(52, 55)
    ITEM_TOTAL = slice(55, None)
    line_items = invoice.split('\n')[2:]

    for item in line_items:
        print(item[UNIT_PRICE], item[DESCRIPTION])

    weird_board = [['_'] * 3] * 3
    weird_board[1][2] = 'X'
    for elem in weird_board:
        print(elem)
    print()

    board = [['_'] * 3 for i in range(3)]
    board[1][2] = 'X'
    for elem in board:
        print(elem)
    print()

    t = (1, 2, [30, 40])
    try:
        t[2] += [50, 60]
    except TypeError as err:
        print(err)
