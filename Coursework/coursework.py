from operator import itemgetter # for getting the sorting key from a tuple in sort_series()
import random # for the normal distribution (gaussian) functions
from collections import OrderedDict # for ordered dict function
random.seed(57)

def series_score(sailor_results, discard = 1):
    #check if discard value is valid
    if discard >= len(sailor_results[1]) or discard < 0:
        return -1
    #sort list
    sorted_list = sorted(sailor_results[1], key=lambda x: x)[:(len(sailor_results[1])-discard)]
    total = 0
    #work out total for the sailor
    for value in sorted_list:
        total += value
    #return total
    return total

def sort_series(sailor_results):
    sailor_results_copy = sailor_results.copy()
    sailor_list = []
    formatted_output_list = []
    #create list of tuples with series names, result arrays and series scores
    for i in range(0, len(sailor_results_copy)):
        sailor_list.append((sailor_results_copy[i][0], sailor_results_copy[i][1], series_score(sailor_results_copy[i])))
    # sort by the series score
    sailor_list.sort(key=itemgetter(2))
    #produce output in required format
    for value in sailor_list:
        formatted_output_list.append((value[0], value[1]))
    #return sorted list
    return formatted_output_list

def read_sailor_data(file):
    #output dictionary initialisation
    output_dict = OrderedDict()
    #counter to skip title row of csv file
    counter = 0
    import csv
    with open(file) as csvfile:
        rdr = csv.reader(csvfile)
        for row in rdr:
            if counter != 0:
                #add to dictionary with key as name and a tuple of the performance and standard deviation
                output_dict[row[0]] = (row[1], row[2])
            counter += 1
    #return built object
    return output_dict

def generate_performances(sailor_data):
    output = OrderedDict()
    for key, value in sailor_data.items():
        output[key] = random.gauss(int(value[0]), int(value[1]))
    return output

def calculate_finishing_order(generated_sailor_data):
    output_list = []
    sorted_list = sorted(generated_sailor_data.items(), key=lambda keyvalue: keyvalue[1], reverse=True)
    for key, value in sorted_list:
        output_list.append(key)
    return output_list

def run_races(num_of_races):
    results = {"Alice": [], "Bob": [], "Clare": [], "Dennis": [], "Eva": []}
    for i in range(0, num_of_races):
        order = calculate_finishing_order(generate_performances(read_sailor_data('values.csv')))
        for index, value in enumerate(order):
            results[value].append(index + 1)
        output = []
        for key, value in results.items():
            output.append((key, value))
    return calculate_finishing_order(dict(sort_series(output)))

print(run_races(6))
