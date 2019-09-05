# import csv

# with open('python.txt') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',' )
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are: ' + ",".join(row) )
#             line_count += 1
import pandas

df = pandas.read_csv('hrdata.csv')

print(df)