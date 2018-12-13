import coursework as cw
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter # for getting the sorting key from a tuple

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

def score_figures(test_data):
    discard_one_dict = {}
    discard_two_dict = {}
    discard_three_dict = {}
    for value in test_data:
        discard_one_dict[value[0]] = cw.series_score(value)
        discard_two_dict[value[0]] = cw.series_score(value, 2)
        discard_three_dict[value[0]] = cw.series_score(value, 3)
    return [sorted(discard_one_dict.items(), key=lambda kv: kv[1]), sorted(discard_two_dict.items(), key=lambda kv: kv[1]), sorted(discard_three_dict.items(), key=lambda kv: kv[1])]

def generate_test_data(races_to_run, file_name = "values.csv"):
    # gets the names defined in the comma-seperated value file, so names are never hard-coded
    name_list = list(cw.read_sailor_data(file_name).keys())
    # creates a dictionary with the names as keys and empty lists as values
    output = {key:[] for key in name_list}
    for i in range(0, races_to_run):
        finishing_order = cw.run_races(1)
        for index, value in enumerate(finishing_order):
            output[value].append(index + 1)
    return [(name, output[name]) for name in name_list]

test_data = [("Alice", [1, 2, 1, 1, 1, 1]), ("Bob", [3, 1, 5, 3, 2, 5]), ("Clare", [2, 3, 2, 2, 4, 2]), ("Dennis", [5, 4, 4, 4, 3, 4]), ("Eva", [4, 5, 3, 5, 5, 3])]

races_to_run = int(input("How many races would you like to model? >>"))
for value in score_figures(generate_test_data(races_to_run)):
    print(value)
print()
