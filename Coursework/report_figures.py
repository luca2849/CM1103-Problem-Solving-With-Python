import coursework as cw
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter

def count_wins(num_of_races, file_name = 'values.csv'):
    name_list = list(cw.read_sailor_data(file_name).keys())
    # creates a dictionary with the names as keys and empty lists as values
    results = {key:0 for key in name_list}
    for i in range(0, num_of_races):
        race_result = cw.run_races(10)
        for index, value in enumerate(race_result):
            results[value] += (index + 1)
    return sorted(results.items(), key=lambda keyvalue: keyvalue[1])

def average_modelling(models_to_average, num_of_races = 1, file_name = 'values.csv'):
    name_list = list(cw.read_sailor_data(file_name).keys())
    # creates a dictionary with the names as keys and empty lists as values
    totals = {key:0 for key in name_list}
    for i in range(0, models_to_average):
        current_model = count_wins(num_of_races)
        for value in current_model:
            totals[value[0]] += value[1]
    for key, value in totals.items():
        totals[key] = value / models_to_average
    print(sorted(totals.items(), key=itemgetter(1)))
    return sorted(totals.items(), key=itemgetter(1))

def plot_bar(x_data, y_data, title, x_label, y_label, subplot):
    index = np.arange(len(x_data))
    bar_list = plt.bar(index, y_data)
    for bar in bar_list:
        bar.set_color('r')
    plt.xlabel(x_label, fontsize=10)
    plt.ylabel(y_label, fontsize=10)
    plt.xticks(index, x_data, fontsize=10, rotation=30)
    plt.title(title)
    x = -0.05 # default x value for bar labels
    for value in y_data:
        plt.text(x, value + (value * 0.01), value)
        x += 1
    plt.show()

race_num = int(input("Input number of models to perform >> "))
results = count_wins(race_num)
print("Over", race_num, "Models")
for value in results:
    print(value[0], "scored", value[1])
totals = [value[1] for value in results]
names = [value[0] for value in results]
# plot_bar(names, totals, "Total Scores", "Names", "Total Score")
extra = input("Would you like to see average results? (Y/N) >>")
if extra.lower() == "y":
    races_to_average = int(input("How many models should be averaged? >>"))
    averages = average_modelling(races_to_average)
    names = [key for key, value in averages]
    averages = [value for key, value in averages]
    print(names, averages)
    avg_averages = []
    avg_names = []
    for index in enumerate(names):
        print(str(names[index[0]]) + "'s average is " + str(averages[index[0]]))
        avg_names.append(names[index[0]])
        avg_averages.append(averages[index[0]])
    # plot_bar(avg_names, avg_averages, "Average Positions", "Names", "Average Position")
def plot_bar(x_data, y_data, title, x_label, y_label, color = "grey"):
    index = np.arange(len(x_data))
    bar_list = plt.bar(index, y_data)
    for bar in bar_list:
        bar.set_color(color)
    plt.xlabel(x_label, fontsize=10)
    plt.ylabel(y_label, fontsize=10)
    plt.xticks(index, x_data, fontsize=10, rotation=30)
    plt.title(title)
    x = -0.05 # default x value for bar labels
    for value in y_data:
        plt.text(x, value * 0.5, value, fontsize=10)
        x += 1

plt.subplot(2, 1, 1)
plot_bar(names, totals, "Total Scores", "Names", "Total Score")
plt.subplot(2, 1, 2)
plot_bar(avg_names, avg_averages, "Average Positions", "Names", "Average Positions")
plt.show()
