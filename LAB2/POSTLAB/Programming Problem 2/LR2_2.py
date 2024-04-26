def read_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []

def main():
    filename = input("Enter the filename: ")
    lines = read_lines(filename)

    while True:
        num_lines = len(lines)
        print(f"\nNumber of lines in the file: {num_lines}")

        try:
            line_number = int(input("Enter a line number (0 to quit): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if line_number == 0:
            print("Exiting the program.")
            break
        elif 1 <= line_number <= num_lines:
            print(f"Line {line_number}: {lines[line_number - 1].strip()}")
        else:
            print("Invalid line number. Please enter a number between 1 and", num_lines)

if __name__ == "__main__":
    main()
