#/usr/bin/python3
def read_file_content(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "The file does not exist."
    except Exception:
        return "An unexpected error occurred."
# Get filename input from user
user_file = input("Enter the filename: ")
# Call the function and print the result
content = read_file_content(user_file)
print(content)
