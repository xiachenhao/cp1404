FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer
        data.append(parts)
    input_file.close()
    return data


def print_subject_details(data):
    for subject in data:
        code, lecturer, num_students = subject
        print(f"{code} is taught by {lecturer} and has {num_students} students")


main()
