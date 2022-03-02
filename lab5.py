#Created Dictionary with 11 entries
dict_data = {
    "Name" : ["Anvi Shah", "Aman Gupta", "Debina Bose", "Akshay Kamble", "Anita Singh", "Manish Patil","Sushmita Pal", "Raj Bhosale", "Priti Pole", "Sheela Ram", "Nimmi Sen"],
    "Age": [42, 34, 26, 26, 0, 31, 0, 36, 32, 22, 37],
    "Gender": ["F", "M", "F", "M", "F", "M", "F", "M", "F", "F", "F"],
    "experience": [20, 10, 3, 5, 2, 8, 12, 9, 0, 14],
    "salary": [65000, 40000, 28000, 0, 25000, 35000, 59000, 38000, 0, 61000]
}


#function to calculate MEAN
def calc_mean(list):
    sum = 0
    for val in list:
        sum += val
    return sum/len(list)

#function to calculate STANDARD DEVIATION
def calc_sd(list, mean):
    diff = [(value - mean)**2 for value in list]
    sum_diff = sum(diff)
    sd = (sum_diff/(len(list) - 1)) ** 0.5
    return sd

#function to calculate ZSCORES
def calc_zscores(list):
    mean = calc_mean(list)
    sd = calc_sd(list, mean)
    zscores = [round((value - mean) / sd, 2) for value in list]
    return zscores

#function to calculate min max scaling
def calc_minmax(list):
    norm = [round((float(i)-min(list))/(max(list)-min(list)),2) for i in list]
    return norm



#Print before replacement
print("\nBEFORE dictionary ===============================>")
print(dict_data.items())

# Logic to replace data
for key in dict_data.keys():
    for index in range(len(dict_data[key])):
        value = dict_data[key][index]
        if value == "NA":
            dict_data[key][index] = dict_data[key][index-1]
        elif value == 0:
            mean = calc_mean(dict_data[key])
            dict_data[key][index] = int(mean)
        elif value == "F" or value == "M":
            dict_data[key][index] = 1 if value == "F" else 0

#Print after Replacement
print("\n\nAFTER dictionary ===============================>")
print(dict_data.items())



# Get input choice from User
choice = int(input("\n\nEnter choice to normalize\n1 for Z score\n2 for Min Max scaling\n"))
age = dict_data["Age"]
exp = dict_data["experience"]
sal = dict_data["salary"]

# Noramlise logic
if choice == 1:
    zscores_age = calc_zscores(age)
    zscores_exp = calc_zscores(exp)
    zscores_sal = calc_zscores(sal)
    print("Age : ", zscores_age)
    print("Experience : ", zscores_exp)
    print("Salary : ", zscores_sal)
elif choice == 2:
    norm_age = calc_minmax(age)
    norm_exp = calc_minmax(exp)
    norm_sal = calc_minmax(sal)
    print("Age : ", norm_age)
    print("Experience : ", norm_exp)
    print("Salary : ", norm_sal)





""" def calc_mean(list):
    sum = 0
    for val in list:
        sum += val
    return sum/len(list)

print("Replace it with numerical value (Male=0, Female=1)")
print("Before =====> \n",dict_data["Gender"])

for key in dict_data.keys():
    for index in range(len(dict_data[key])):
        value = dict_data[key][index]
        if value == "F" or value == "M":
            dict_data[key][index] = 1 if value == "F" else 0

print("After =====> \n",dict_data["Gender"]) """

