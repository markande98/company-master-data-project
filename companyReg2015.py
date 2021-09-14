import csv
import matplotlib.pyplot as plt

# result will contain the mapping of zip code to their corresponding district
result = {}
# to find the district of registration by zip code
district_of_reg_by_zip = {}
# count the registration by district
count_of_reg_by_district = {}
# storing the distict names
district = []
# storing the count of company registraion
count_of_reg = []


# reading the zip-code and district csv file
def read_zip_dist_csv():
    with open("zip_dist.csv", 'r', encoding="latin1") as file:
        reader = csv.DictReader(file)

        for row in reader:
            result[row['Zip-code']] = row['District']


# Reading the csv file, mapping the registration
# of district to its corresponding zip-code and
# counting the registration by district in 2015.
def read_csv():
    with open("Maharashtra.csv", encoding="latin1", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            dor = row['DATE_OF_REGISTRATION']
            if len(dor) == 8:
                val = int(dor[6:])
                val += 2000
                # only considering 2015 year
                if val == 2015:
                    Address = row['Registered_Office_Address']
                    zip_code = Address[len(Address) - 6:]
                    if result.get(zip_code) is not None:
                        district_of_reg_by_zip[zip_code] = result.get(zip_code)
                        if result.get(zip_code) in count_of_reg_by_district:
                            count_of_reg_by_district[result.get(zip_code)] += 1
                        else:
                            count_of_reg_by_district[result.get(zip_code)] = 1


# separating the disrtict and its corresponding
# companies registrations.
def dist_count_of_reg(count_of_reg_by_district, district, count_of_reg):
    for key in count_of_reg_by_district.keys():
        district.append(key)
        count_of_reg.append(count_of_reg_by_district[key])


# only showing the top 10 district
def plot_bar():
    plt.bar(district[:10], count_of_reg[:10])
    plt.xlabel("District")
    plt.ylabel("Count Of Registration in 2015 year")
    plt.xticks(fontsize=5)
    plt.show()


if __name__ == '__main__':
    read_zip_dist_csv()
    read_csv()
    # Showing zip-code and its corresponding district
    print(district_of_reg_by_zip)
    # Showing district and its count of company registration
    print(count_of_reg_by_district)
    dist_count_of_reg(count_of_reg_by_district, district, count_of_reg)
    plot_bar()
