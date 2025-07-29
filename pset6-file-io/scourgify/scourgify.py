import sys
import csv


def main():
    old, new = file_check()
    scourgify(old, new)



def file_check():
    # Argument check
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    elif len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    else:
        old_filename = sys.argv[1]
        new_filename = sys.argv[2]

    # File check
    if old_filename.endswith('.csv') and new_filename.endswith('.csv'):
        old_file = old_filename
        new_file = new_filename
    else:
        print('Not the right format')

    return old_file, new_file



def scourgify(old_file, new_file):
    students = []

    # Read file
    with open(old_file) as file:
        reader = csv.reader(file)
        next(reader, None)  # ignore headers
        for row in reader:
            last, first = row[0].split(',') # split name into first and last
            house = row[1]
            students.append({"first": first.strip(), "last": last.strip(), "house": house.strip()})

    # Write new file
    with open(new_file, 'w') as file:
        writer = csv.DictWriter(file, fieldnames = ['first', 'last', 'house'])
        writer.writeheader()    # include headers
        for student in students:
            writer.writerow({"first": student['first'], "last": student['last'], "house": student['house']})


if __name__ == "__main__":
    main()
