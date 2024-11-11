def reversed_words_in_line(line: str) -> str:
    new_line = ""
    for word in line.split():
        new_word = word[::-1]
        new_line += new_word + " "
    return new_line


def main():
    line = "Hello Kate! What a beautiful day today!"
    line_2 = "Привет Катя! Какой чудесный сегодня день!"
    print("Начальная строка: ", line)
    print("Реверсивные слова: ", reversed_words_in_line(line), "\n")
    print("Начальная строка 2: ", line_2)
    print("Реверсивные слова 2: ", reversed_words_in_line(line_2))


if __name__ == "__main__":
    main()
