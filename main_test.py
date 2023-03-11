import main
import io
import sys
import re

# global rsum


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '2'
    # sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\W]*' + str(minval) + r'[\w,\W]*'
    # res = re.search(regex_string, lines[0])
    # regex_string = r'[\w,\W]*165[\w,\W]*'
    # res = re.search(regex_string, lines[0])
    # assert res != None
    # print(res.group())
    # assert main.main.rsum[0] == 65
    # assert main.main.rsum[1] == 115
    # assert main.main.rsum[2] == 165
    assert main.csum[0] == 63
    assert main.csum[1] == 66
    assert main.csum[2] == 69
    assert main.csum[3] == 72
    assert main.csum[4] == 75
