"""
Напишите программу, которая использует многопроцессность для вычисления
факториала целых чисел от 1 до 10. Каждый процесс должен вычислять факториал одного числа.
"""

from multiprocessing import Pool


def calc_factorial(num: int) -> int:
    fact = 0
    for n in range(1, num + 1):
        if fact == 0:
            fact = n
        else:
            fact = fact * n
    return fact


def run_calc_fact(nums: list[int]) -> list[int]:
    with Pool(processes=5) as pool:
        result = pool.map(calc_factorial, nums)
        print(pool)
        return result


def main() -> list[int]:
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return run_calc_fact(nums)


if __name__ == "__main__":
    print(*main())
