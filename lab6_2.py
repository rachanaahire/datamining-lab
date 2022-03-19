### Data Normalization with Decimal Scaling

import csv

#fetch data from csv file
patients_data = []
with open('patients.csv') as my_file:
    csv_read = csv.reader(my_file)
    next(csv_read)
    for line in csv_read:
        patients_data.append(int(line[2]))

print("Before Decimal Scaling Normalisation:\n",patients_data)
maximum = max(patients_data)
j = len(str(maximum))
norm = [value/10**j for value in patients_data]
print("\nAfter Decimal Scaling Normalisation:\n",norm)