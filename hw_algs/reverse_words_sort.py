"""
Напишите программу для ввода нескольких слов (строковой переменной, слова
разделены пробелами) и выведите каждое слово в отдельной строке с обратным
следованием букв в слове, список должен быть упорядочен по алфавиту.
"""


def sort_words(line: str) -> list[str]:
    sorted_words = []
    for word in line.split():
        i = 0
        while i < len(sorted_words) and sorted_words[i] < word[::-1]:
            i += 1
        sorted_words.insert(i, word[::-1])
    return sorted_words


def main() -> None:
    line = input("Введите слова через пробел: ")
    sorted_words = sort_words(line)
    [print(word) for word in sorted_words]


if __name__ == "__main__":
    main()
