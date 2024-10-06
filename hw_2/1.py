def rewrite_file(input_file: str, output_file: str) -> None:
    with open(input_file) as file:
        with open(output_file, "w") as destination:
            destination.write(file.read())


if __name__ == "__main__":
    rewrite_file("files_hw_2/source.txt", "files_hw_2/destination.txt")
