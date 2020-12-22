import csv


def parse_csv_to_dict():
    file_name = 'AMLibrary.csv'

    rows = []

    # Reading csv file
    with open(file_name, 'r') as csvfile:
        # Creating a csv reader object
        csvreader = csv.reader(csvfile)

        # Extracting each data row one by one
        for row in csvreader:
            rows.append(row)

    # Printing out the first 5 rows
    #for row in rows[:5]:
        #print(row)

    #

    return rows
