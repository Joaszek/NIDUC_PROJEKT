import csv


#  Method for clearing file to save new data
def clear_file(filename):
    f = open(filename, "w")
    f.close()


#  Method for saving data to file
def save_to_file(filename, csv_data):
    f = open(filename, "a", newline="")
    writer = csv.writer(f, delimiter=";")
    for data in csv_data:
        writer.writerow(data)
    f.close()
