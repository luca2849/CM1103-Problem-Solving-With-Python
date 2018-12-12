import coursework as cw
import numpy as np
import matplotlib.pyplot as plt

def count_wins(num_of_models, num_of_races = 6, file_name = 'values.csv'):
    name_list = list(cw.read_sailor_data(file_name).keys())
    # creates a dictionary with the names as keys and empty lists as values
    results = {key:0 for key in name_list}
    for i in range(0, num_of_models):
        race_result = cw.run_races(num_of_races)
        for index, value in enumerate(race_result):
            results[value] += (index + 1)
    return sorted(results.items(), key=lambda keyvalue: keyvalue[1])

def average_modelling(num_of_models, race_result):
    output = {}
    for tuple in race_result:
        output[tuple[0]] = tuple[1] / num_of_models
    return sorted(output.items(), key=lambda keyvalue: keyvalue[1])


race_num = int(input("Input number of models and averages to perform >> "))
results = count_wins(race_num, 1)
totals = [value[1] for value in results]
names = [value[0] for value in results]
averages = average_modelling(race_num, results)
avg_names = [key for key, value in averages]
avg_values = [value for key, value in averages]
fig_size = plt.rcParams["figure.figsize"]
figure = plt.gcf()
figure.canvas.set_window_title("Total Scores and Average Results")
fig_size[0] = 10
fig_size[1] = 8
def plot_bar(x_data, y_data, title, x_label, y_label, color = "grey"):
    index = np.arange(len(x_data))
    bar_list = plt.bar(index, y_data)
    for bar in bar_list:
        bar.set_color(color)
    plt.xlabel(x_label, fontsize=15)
    plt.ylabel(y_label, fontsize=15)
    plt.xticks(index, x_data, fontsize=15, rotation=30)
    plt.title(title, fontsize=20)
    x = -0.05 # default x value for bar labels
    for value in y_data:
        plt.text(x, value * 0.5, value, fontsize=20)
        x += 1

plt.subplot(2, 1, 1)
plot_bar(names, totals, "Total Scores Over " + str(race_num) + " Races", "Names", "Total Score")
plt.subplot(2, 1, 2)
plot_bar(avg_names, avg_values, "Average Position Over " + str(race_num) + " Races", "Names", "Average Positions")
plt.tight_layout()
plt.show()
