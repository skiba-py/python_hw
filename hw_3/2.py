"""
Напишите программу, которая создаёт несколько потоков для выполнения функции,
которая выводит целые числа от 1 до 10 с задержкой в 1 секунду.
"""

import threading
import time
from concurrent.futures.thread import ThreadPoolExecutor


def output_number(num: int) -> None:
    print("Current number: ", num)
    time.sleep(1)


def set_threads(count: int) -> None:
    with ThreadPoolExecutor(count) as executor:
        for num in range(1, 11):
            executor.submit(output_number, num)
            print("Active threads: ", threading.active_count())
            print("Threads: ", threading.enumerate())


if __name__ == "__main__":
    set_threads(3)
    print("Active threads after work: ", threading.active_count())
