import os
from csv import reader


def generate_files_from_csv(filename):
    # open file
    with open(filename, "r") as my_file:
        # pass the file object to reader()
        file_reader = reader(my_file)

        # do this for all the rows
        for row in file_reader:
            # print the row
            print(row)

            if len(row) > 0:
                if not os.path.exists('./data'):
                    os.mkdir('data')
                prospective_file_name = row[0]
                new_file = open(f'./data/{prospective_file_name}.csv', 'w')
                new_file.close()
