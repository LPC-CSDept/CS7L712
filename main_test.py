import main
import io
import sys
import re

# global rsum


def test_main_1():
    numbers = [[11, 12, 13, 14, 15],
               [21, 22, 23, 24, 25],
               [31, 32, 33, 34, 35]]

    result = main.getSumCol(numbers)
    print('Your output ', result)
    assert len(result) == 5
    assert result[0] == 63
    assert result[1] == 66
    assert result[2] == 69
    assert result[3] == 72
    assert result[4] == 75


def test_main_2():
    import random
    rownum = random.randint(3, 6)
    colnum = random.randint(3, 7)

    numbers = [[0] * colnum for i in range(rownum)]
    for i in range(rownum):
        for j in range(colnum):
            numbers[i][j] = random.randint(0, 10)
        print(numbers[i])
    result = main.getSumCol(numbers)
    print('Your output', result)

    assert len(result) == colnum
    translist = list(zip(*numbers))
    for i in range(len(translist)):
        assert result[i] == sum(translist[i])
