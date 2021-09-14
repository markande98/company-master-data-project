import csv
import matplotlib.pyplot as plt

arr = []


def read_csv():
    with open('Maharashtra.csv', 'r', encoding="latin1") as file:
        reader = csv.DictReader(file)

        for row in reader:
            val = int(float((row['AUTHORIZED_CAP'])))
            arr.append(val)


def select_interval():

    while True:
        print("To select the intervals type the following key")
        print("Press 1 : To select 0 - 1L")
        print("Press 2 : To select 1L - 10L")
        print("Press 3 : To select 10L - 1Cr")
        print("Press 4 : To select 1Cr - 10Cr")
        print("Press 5 : To select > 10Cr")
        choice = int(input("Enter your choice : "))
        switcher = {
            1: "0 - 1L",
            2: "1L - 10L",
            3: "10L - 1Cr",
            4: "1Cr - 10Cr",
            5: ">10Cr"
        }

        result = switcher.get(choice, "Invalid Choice")

        if result != "Invalid Choice":
            return [result, choice]
        else:
            print("Invalid Choice, select again")


def set_intervals(result):
    intervals = []
    if result == "0 - 1L":
        intervals.append(0)
        intervals.append(100000)
    elif result == "1L - 10L":
        intervals.append(100000)
        intervals.append(1000000)
    elif result == "10L - 1Cr":
        intervals.append(1000000)
        intervals.append(10000000)
    elif result == "1Cr - 10Cr":
        intervals.append(10000000)
        intervals.append(100000000)
    else:
        intervals.append(100000000)
        intervals.append(1000000000)
    return intervals


def plot_histogram():
    result = select_interval()
    intervals = set_intervals(result)
    result = result[0]
    # Plot a histogram
    # To create a 10000 gap in the intervals
    bins = []

    step_size = intervals[1] // 10
    for i in range(intervals[0], intervals[1], step_size):
        bins.append(i)

    # To create a list which has values between the intervals
    values = []
    for i in arr:
        if i >= 100000000:
            values.append(i)
            continue
        elif i >= intervals[0] and i <= intervals[1]:
            values.append(i)

    plt.hist(values, bins, color='g')
    plt.xlabel(result)
    plt.ylabel("Authorized Cap")
    plt.xticks(fontsize=8)
    plt.show()


if __name__ == '__main__':
    read_csv()
    plot_histogram()
