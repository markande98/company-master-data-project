import csv
import numpy as np
import matplotlib.pyplot as plt

# Here i am only considering the year >= 2000
# count of registration by principal buisness activity
principal_buisness_activity = {}
# count of registration by year (year >= 2000)
year = {}

x = np.arange(10)

years = []
pba = []
year_reg_count = []
pba_reg_count = []


# Read the csv file
def read_csv():
    with open("Maharashtra.csv", 'r', encoding="latin1") as file:
        reader = csv.DictReader(file)

        for row in reader:
            dor = row['DATE_OF_REGISTRATION']
            buisness = row['PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN']
            if buisness in principal_buisness_activity:
                principal_buisness_activity[buisness] += 1
            else:
                principal_buisness_activity[buisness] = 1
            if len(dor) == 8:
                val = int(dor[6:])
                val += 2000
                if val >= 2000:
                    if val in year:
                        year[val] += 1
                    else:
                        year[val] = 1


# separating years and its corresponding counts
def year_count(year, years, year_reg_count):
    for key in year.keys():
        years.append(key)
        year_reg_count.append(year[key])


# separating buisness and its corresponding count
def pba_count(principal_buisness_activity, pba, pba_reg_count):
    for key in principal_buisness_activity.keys():
        pba.append(key)
        pba_reg_count.append(principal_buisness_activity[key])


# Plot group bar
def plot_groupbar():

    year_reg_count.sort()
    pba_reg_count.sort()
    width = 0.34

    fig, ax = plt.subplots()

    ax.bar(x - width / 2, year_reg_count[:10],
           width, color="red", label='year count')
    ax.bar(x + width / 2, pba_reg_count[:10],
           width, color="blue", label='principal buisness count')
    fig.tight_layout()
    plt.legend()
    plt.ylabel("Registration Count")
    plt.show()


if __name__ == '__main__':
    read_csv()
    year_count(year, years, year_reg_count)
    pba_count(principal_buisness_activity, pba, pba_reg_count)
    plot_groupbar()
