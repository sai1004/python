import csv 

# <==========================writing file ==========================>

with open('csvWrite.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name', 'Rank']

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    writer.writerow({'Rank':'B','first_name':'jane','last_name':'doe'})

print("writing complete ")