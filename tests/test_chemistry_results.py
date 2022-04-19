import time


# run tests in parallel: pytest -n4
def test_result_1_completes_as_expected():
    time.sleep(5)
    print('\n>>>Result 1 has completed\n')


def test_result_2_completes_as_expected():
    time.sleep(5)
    print('\n>>>Result 2 has completed\n')


def test_result_3_completes_as_expected():
    time.sleep(5)
    print('\n>>>Result 3 has completed\n')


def test_result_4_completes_as_expected():
    time.sleep(5)
    print('\n>>>Result 4 has completed\n')
