from operator import itemgetter # for getting the sorting key from a tuple
import coursework as cw
import numpy as np
import matplotlib.pyplot as plt
import random

print(cw.run_races(6))
def count_wins(num_of_races, file_name = 'values.csv'):
    name_list = list(cw.read_sailor_data(file_name).keys())
    # creates a dictionary with the names as keys and empty lists as values
    results = {key:0 for key in name_list}
    for i in range(0, num_of_races):
        race_result = cw.calculate_finishing_order(cw.generate_performances(cw.read_sailor_data(file_name)))
        for index, value in enumerate(race_result):
            results[value] += (index + 1)
    return sorted(results.items(), key=lambda keyvalue: keyvalue[1])

race_num = int(input("Input number of models to perform >> "))
print("Over", race_num, "Models")
results = count_wins(race_num)
totals = [value[1] for value in results]
names = [value[0] for value in results]
def plot_bar_x():
    # this is for plotting purpose
    index = np.arange(len(names))
    plt.bar(index, totals)
    plt.xlabel('Name', fontsize=10)
    plt.ylabel('Score', fontsize=10)
    plt.xticks(index, names, fontsize=10, rotation=30)
    plt.title('Scores for ' + str(race_num) + ' models.')
    for a in totals:
        plt.text(80, a, str(a))
    plt.show()

plot_bar_x()
