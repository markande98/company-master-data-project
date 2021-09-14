import csv
import matplotlib.pyplot as plt

result = {}
year = []
number_of_company_reg = []


# Reading the csv file and only considering year 2001 to 2021
def read_csv():
    with open('Maharashtra.csv', 'r', encoding="latin1") as file:
        reader = csv.DictReader(file)

        for row in reader:
            dor = row['DATE_OF_REGISTRATION']
            if len(dor) == 8:
                val = int(dor[6:])
                val += 2000
                if val >= 2001 and val <= 2021:
                    if val in result:
                        result[val] += 1
                    else:
                        result[val] = 1


# separating the year and corresponding count
# of company registered
def year_num_of_reg(result, year, number_of_company_reg):
    for key in result.keys():
        year.append(key)
        number_of_company_reg.append(result[key])


# plotting a bar plot
def plot_bar():
    plt.bar(year, number_of_company_reg)
    plt.xlabel("Year")
    plt.ylabel("Number of Company registered")
    plt.show()


if __name__ == '__main__':
    read_csv()
    year_num_of_reg(result, year, number_of_company_reg)
    plot_bar()
