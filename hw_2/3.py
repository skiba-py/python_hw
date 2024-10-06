def calc_words(input_file: str) -> int:
    with open(input_file) as file:
        sum = 0
        for line in file:
            splited = line.split(" ")
            for word in splited:
                if word != "—":
                    sum += 1
    print(sum)
    return sum


if __name__ == "__main__":
    calc_words("files_hw_2/text_file.txt")
