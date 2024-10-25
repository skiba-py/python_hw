class NumberError(Exception):
    pass


class NumberError2(Exception):
    pass


def sum_of_nums(nums: list) -> int:
    result = 0
    for num in nums:
        if num < 0:
            raise NumberError("Число меньше 0")
        elif (num % 2) == 0:
            raise NumberError2("Число четное")
        else:
            result += num
    return result


def test_solution():
    try:
        assert sum_of_nums([1, 2, 3, 5, 5]) == 14
    except (NumberError, NumberError2) as e:
        print(e)
    try:
        assert sum_of_nums([101, -13]) == 102
    except (NumberError, NumberError2) as e:
        print(e)
    try:
        assert sum_of_nums([8, 0]) == 0
    except (NumberError, NumberError2) as e:
        print(e)
    try:
        assert sum_of_nums([1, 2]) == 0
    except (NumberError, NumberError2) as e:
        print(e)


if __name__ == "__main__":
    test_solution()
