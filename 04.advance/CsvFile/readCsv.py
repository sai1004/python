# import csv

# <===============  reading cvs data file using csv module  ====================>

# with open('python.txt') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',' )
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are: ' + ",".join(row) )
#             line_count += 1



# <===================reading cvs data file using pandas ====================>
 
# import pandas

# csvFile = pandas.read_csv('hrdata.csv')

# print(csvFile)
