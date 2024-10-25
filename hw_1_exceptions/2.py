def calc_2_nums(first: int | str, second: int | str) -> int:
    result = 0
    try:
        result = int(first) // int(second)
    except ZeroDivisionError:
        print("Ошибка деления на 0")
    except ValueError:
        print("Ошибка типа переданного значения")
    print(result)
    return result


def test_solution():
    assert calc_2_nums(10, 2) == 5
    assert calc_2_nums(1000, 500) == 2
    assert calc_2_nums(8, 0) == 0
    assert calc_2_nums(10, "two") == 0
    assert calc_2_nums("five", 14) == 0


if __name__ == "__main__":
    test_solution()
    calc_2_nums(
        int(input("Введите число: ")), int(input("Введите второе число: "))
    )
