from threading import Thread

LIST_OF_NUMEBRS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def calc_degree(degree: int) -> list[int]:
    result = []
    for num in LIST_OF_NUMEBRS:
        result.append(num**degree)
    print(result)

    # if degree == 2:    # этот код делает так, что интерпретатор автоматически
    #     time.sleep(1)  # создает новый поток и переключает управление на него
                         # в тот момент когда текущий поток спит, скорее всего
                         # он просто не успевает создать новый поток так как
                         # вычисления в текущем потоке ывполняются слишком быстро
    return result


def calc_in_threading(first_degree: int, second_degree: int) -> None:
    first_t = Thread(target=calc_degree, args=(first_degree,))
    second_t = Thread(target=calc_degree, args=(second_degree,))
    first_t.start()
    print("Процесс запущен: ", first_t.ident, "1")
    second_t.start()
    print("Процесс запущен: ", second_t.ident, "2")


if __name__ == "__main__":
    calc_in_threading(2, 3)
