"""
Напишите программу, которая асинхронно обрабатывает список чисел, вычисляя их
квадрат. Каждая операция обработки должна имитировать задержку в 1 секунду.
"""

import asyncio


async def calc_square(num: int) -> int:
    print("Сoroutines:", asyncio.current_task())
    await asyncio.sleep(1)
    return num**2


def main(numbers: list[int]) -> list[int]:
    new_list = []
    for num in numbers:
        new_list.append(asyncio.run(calc_square(num)))
    return new_list


if __name__ == "__main__":
    print(*main([1, 2, 3, 4, 5]))
