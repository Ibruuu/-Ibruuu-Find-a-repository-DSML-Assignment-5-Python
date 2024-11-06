def read_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
filename = input("Enter the filename to read: ")
read_file(filename)

def copy_file(src_filename, dest_filename):
    try:
        with open(src_filename, 'r') as src_file:
            content = src_file.read()
        with open(dest_filename, 'w') as dest_file:
            dest_file.write(content)
        print(f"Contents of {src_filename} copied to {dest_filename}.")
    except FileNotFoundError:
        print(f"The file {src_filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
src_filename = input("Enter the source filename: ")
dest_filename = input("Enter the destination filename: ")
copy_file(src_filename, dest_filename)

def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        words = content.split()
        print(f"The total number of words in {filename} is: {len(words)}")
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
filename = input("Enter the filename to count words: ")
count_words_in_file(filename)

def convert_to_int():
    user_input = input("Enter a number: ")
    try:
        result = int(user_input)
        print(f"The number is: {result}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
convert_to_int()

def check_negative_numbers():
    user_input = input("Enter a list of integers (separated by spaces): ")
    try:
        numbers = [int(i) for i in user_input.split()]
        for num in numbers:
            if num < 0:
                raise ValueError(f"Negative number found: {num}")
        print("All numbers are non-negative.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
check_negative_numbers()

def compute_average():
    try:
        user_input = input("Enter a list of integers (separated by spaces): ")
        numbers = [int(i) for i in user_input.split()]
        if len(numbers) == 0:
            raise ValueError("The list cannot be empty.")
        average = sum(numbers) / len(numbers)
        print(f"The average is: {average}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Program execution completed.")

# Example usage:
compute_average()

def write_to_file():
    filename = input("Enter the filename to write to: ")
    content = input("Enter the content to write to the file: ")
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print("File written successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print("Welcome! The file has been written successfully.")
    finally:
        print("Program execution completed.")

# Example usage:
write_to_file()





