# File Head Display
# Author: Avery Mitchell
# COSC 1010 - Programming Assignment: Files
#
# This program asks the user for the name of a file and displays only the
# first five lines of the file's contents. If the file has fewer than five
# lines, it displays the entire file.

# Constant for the number of lines to display
MAX_LINES = 5


def main():
    print("File Head Display")
    print("-----------------")

    # Ask the user for the name of the file
    filename = input("Enter the name of a file: ")

    try:
        # Open the file for reading
        with open(filename, "r") as infile:
            line_count = 0

            # Read and display lines until we reach MAX_LINES or the end of the file
            for line in infile:
                print(line.rstrip("\n"))
                line_count += 1
                if line_count == MAX_LINES:
                    break

        print()
        if line_count < MAX_LINES:
            print(f"End of file reached. The file contains only {line_count} line(s).")
        else:
            print(f"Displayed the first {MAX_LINES} lines of {filename}.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")


# Call the main function
main()
