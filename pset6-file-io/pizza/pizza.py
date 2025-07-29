import sys
from tabulate import tabulate


def main():
    csv_file = csv_file_check()
    print(read_menu_csv(csv_file))



def csv_file_check():
    # Checking the command-line argument
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    elif len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    else:
        file_name = sys.argv[1]

    # Identify CSV file
    if 'regular' in file_name:
        csv_file = 'regular.csv'
    elif 'sicilian' in file_name:
        csv_file = 'sicilian.csv'

    # Check file type
    if not file_name.endswith('.csv'):
        sys.exit('Not a CSV file')

    return csv_file



def read_menu_csv(csv_file):

    # Open file
    try:
        with open(csv_file) as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit('File does not exist')

    # Retrieve list of lists of each line
    csv_list = []

    for line in lines:
        line_list = line.strip().split(',')
        csv_list.append(line_list)

    csv_header = csv_list[0]
    csv_prices = csv_list[1:]

    return tabulate(csv_prices, csv_header, tablefmt="grid")





if __name__ == '__main__':
    main()
