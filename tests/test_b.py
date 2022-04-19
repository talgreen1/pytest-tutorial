import time


# run tests in parallel: pytest -n4 --dist loadscope
def test_1():
    time.sleep(5)
    print('\n>>> Module B - Test 1\n')


def test_2():
    time.sleep(5)
    print('\n>>> Module B - Test 2\n')


def test_3():
    time.sleep(5)
    print('\n>>> Module B - Test 3\n')


def test_4():
    time.sleep(5)
    print('\n>>> Module B - Test 4\n')
