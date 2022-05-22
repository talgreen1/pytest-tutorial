import threading
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

threads = []

for _ in range(10):
    t = threading.Thread(target=do_something, args=(6,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')
