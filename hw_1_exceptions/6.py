import math


def calc_sqrt(num: int):
    result = 0
    try:
        if num < 0:
            raise ValueError("Некорректное число")
        result = math.sqrt(num)
    except ImportError:
        print("Модуль math не может быть импортирован")
    except ValueError as e:
        print(str(e))
    print(result)
    return result


def test_solution():
    assert calc_sqrt(4) == 2
    assert calc_sqrt(25) == 5
    assert calc_sqrt(-2) == 0


if __name__ == "__main__":
    test_solution()
    calc_sqrt(int(input("Введите число: ")))
