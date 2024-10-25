def check_index(lst, index):
    result = 0
    try:
        result = lst[index]
    except IndexError:
        print("Индекс выходит за пределы списка")
    print(result)
    return result


def test_solution():
    assert check_index([1, 2, 3, 4, 5, 6], 5) == 6
    assert check_index(["1", 2, "4", 245, [23, 2356]], 4) == [23, 2356]
    assert check_index([8, {1: 2}, [1, 2, 3], 45], 4) == 0


if __name__ == "__main__":
    test_solution()
    check_index(int(input("Введите индекс: ")))
