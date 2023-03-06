import csv


with open('C:\\dir\\school\\buaa\\graduation\\matrixth\\data\\train.csv') as f:
    writer = csv.writer(f)
    reader = csv.reader(f)
    for row in reader:
        print(row)
        writer.writerow(row)
