def calc_price(input_file: str) -> int:
    with open(input_file) as file:
        sum = 0
        for line in file:
            splited = line.strip().split("\t")
            sum += int(splited[1]) * int(splited[2])
    print(sum)
    return sum


if __name__ == "__main__":
    calc_price("files_hw_2/prices.txt")
