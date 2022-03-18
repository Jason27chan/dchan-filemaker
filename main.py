from csv import reader

print("running main")
# open file
with open("testdata.csv", "r") as my_file:
    # pass the file object to reader()
    file_reader = reader(my_file)

    # do this for all the rows
    for row in file_reader:
        # print the row
        print(row)
