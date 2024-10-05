def change_type(string):
    result = 0
    try:
        result = float(string)
    except ValueError:
        print("Передана неподходящая строка")
    print(result)
    return result


def test_solution():
    assert change_type("1.5") == 1.5
    assert change_type("1.354545") == 1.354545
    assert change_type("1,3545") == 0


if __name__ == "__main__":
    test_solution()
    change_type(input("Введите число: "))
