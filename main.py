import random


def getSumCol(numbers):
    """
    ################################################## 
    Code your program here
    ################################################## 
    """
    return result


def main():

    # Test 1
    numbers = [[11, 12, 13, 14, 15],
               [21, 22, 23, 24, 25],
               [31, 32, 33, 34, 35]]

    result = getSumCol(numbers)
    print(result)

    # Test 2
    rownum = random.randint(3, 6)
    colnum = random.randint(3, 7)
    numbers = [[0] * colnum for i in range(rownum)]
    for i in range(rownum):
        for j in range(colnum):
            numbers[i][j] = random.randint(0, 10)
        print(numbers[i])
    result = getSumCol(numbers)
    print('Your output', result)


if __name__ == '__main__':
    main()
