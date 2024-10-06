def unique_lines(input_file: str, output_file: str) -> None:
    with open(input_file) as file:
        with open(output_file, "w") as destination:
            unique_lines = []
            for line in file:
                if line not in unique_lines:
                    unique_lines.append(line)
                    destination.write(line)


if __name__ == "__main__":
    unique_lines("files_hw_2/input.txt", "files_hw_2/unique_output.txt")
