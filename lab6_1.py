### Data Smoothing with Binning Algorithm

import csv

#function to calculate MEAN
def calc_mean(list):
    sum = 0
    for val in list:
        sum += val
    return sum/len(list)

#function to determine whether value is odd or even
def oddeven(num):
    return 'odd' if num%2 else 'even'

patients_data = []
bin_depth = int(input("Enter bin depth: "))

#fetch data from csv file
with open('patients.csv') as my_file:
    csv_read = csv.reader(my_file)
    next(csv_read)
    for line in csv_read:
        patients_data.append(int(line[2]))

# sort the list
patients_data.sort()

#binning of data
binned_data = [patients_data[i:i+bin_depth] for i in range(0, len(patients_data), bin_depth)]
print("Partition into bins of depth %i :" % bin_depth)

data_length = len(binned_data)
bin_length = len(binned_data[0])

#print binned data
for i in range(data_length):
    print ("Bin %i : "%i, binned_data[i])

#data smoothing by binning techniques
choice = True
while(choice):
    choice = int(input("\nType 1 for Smoothing by bin Mean\nType 2 for Smoothing by bin Median\nType 3 for Smoothing by bin Boundaries\nType 0 to exit\n"))
    if choice == 1:
        bin_mean = [[int(calc_mean(i)) for j in i] for i in binned_data]
        print("Smoothing by bin Means :\n", bin_mean)
    elif choice == 2:
        val = oddeven(bin_length)
        bin_median = []
        if val == 'odd':
            ind = int((bin_length+1)/2) - 1
            bin_median = [[i[ind] for j in i] for i in binned_data]
        elif val == 'even':
            ind1 = int(bin_length/2) - 1
            ind2 = ind1+1
            bin_median = [[int((i[ind1]+i[ind2])/2) for j in i] for i in binned_data]
        print("Smoothing by bin Median :\n", bin_median)
    elif choice == 3:
        bin_bound = [[i[0] if (j - i[0] <= i[len(i)-1] - j) else i[len(i)-1] for j in i] for i in binned_data]
        print("Smoothing by bin Boundaries :\n", bin_bound)
