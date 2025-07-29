import sys

def main():
    # Checking the command-line argument
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    elif len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    else:
        file_name = sys.argv[1]

    # Check LOC
    print(loc(file_name))


# Calculate LOC
def loc(file_name):
    if not file_name.endswith('.py'):
        sys.exit('Not a Python file')

    # Open file
    try:
        with open(file_name) as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit('File not found')

    # Check number of lines in file
    line_count=0

    for line in lines:
        if line.strip().startswith('#'):
            line_count += 0
        elif line.startswith("'''") or line.endswith("'''"):
            line_count += 0
        elif line.isspace():
            line_count += 0
        else:
            line_count += 1

    return line_count






if __name__ == '__main__':
    main()
