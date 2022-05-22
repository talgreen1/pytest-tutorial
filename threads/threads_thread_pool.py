import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ThreadPoolExecutor() as exeutor:
    f1 = exeutor.submit(do_something, 5)
    f2 = exeutor.submit(do_something, 5)
    print (f1.result())
    print (f2.result())



finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')