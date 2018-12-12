import coursework as cw
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter

def count_wins(num_of_models, num_of_races = 6, file_name = 'values.csv'):
    name_list = list(cw.read_sailor_data(file_name).keys())
    # creates a dictionary with the names as keys and empty lists as values
    results = {key:0 for key in name_list}
    for i in range(0, num_of_models):
        race_result = cw.run_races(num_of_races)
        for index, value in enumerate(race_result):
            results[value] += (index + 1)
    return sorted(results.items(), key=lambda keyvalue: keyvalue[1])

def average_modelling(num_of_models = 1, file_name = 'values.csv'):
    result = count_wins(num_of_models)
    output = {}
    for tuple in result:
        output[tuple[0]] = tuple[1] / num_of_models
    return sorted(output.items(), key=lambda keyvalue: keyvalue[1])


race_num = int(input("Input number of models and averages to perform >> "))
results = count_wins(race_num)
print("Over", race_num, "Models")
for value in results:
    print(value[0], "scored", value[1])
totals = [value[1] for value in results]
names = [value[0] for value in results]
averages = average_modelling(race_num)
avg_names = [key for key, value in averages]
avg_values = [value for key, value in averages]
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 10
fig_size[1] = 8
print(fig_size)
def plot_bar(x_data, y_data, title, x_label, y_label, color = "grey"):
    index = np.arange(len(x_data))
    bar_list = plt.bar(index, y_data)
    for bar in bar_list:
        bar.set_color(color)
    plt.xlabel(x_label, fontsize=10)
    plt.ylabel(y_label, fontsize=10)
    plt.xticks(index, x_data, fontsize=10, rotation=30)
    plt.title(title, fontsize=20)
    x = -0.05 # default x value for bar labels
    for value in y_data:
        plt.text(x, value * 0.5, value, fontsize=10)
        x += 1

plt.subplot(2, 1, 1)
plot_bar(names, totals, "Total Scores", "Names", "Total Score")
plt.subplot(2, 1, 2)
plot_bar(avg_names, avg_values, "Average Position", "Names", "Average Positions")
plt.tight_layout()
plt.show()
