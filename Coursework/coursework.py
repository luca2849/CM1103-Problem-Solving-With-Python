"""
Python program to model sailors race results using their mean and standard deviation
"""
# Note - for all imports I am only importing the needed functions to improve efficiency
from operator import itemgetter # for getting the sorting key from a tuple
from collections import OrderedDict # for ordered dict function
from random import normalvariate # for the normal distribution function

def series_score(sailor_results, discard=1):
    """
    Takes a tuple of a sailor's name and their results and returns the total
    of their places minus the lowest
    e.g. ("bob", [2, 4, 1, 1, 2, 5]) would return 10 (2 + 4 + 1 + 1 + 2)
    The function also takes an argument to cut off a given number of worst results,
    defaulted to 1
    """
    #check if discard value is valid
    if discard >= len(sailor_results[1]) or discard < 0:
        return -1
    #sort list and slice off required values
    sorted_list = sorted(sailor_results[1])[:(len(sailor_results[1])-discard)]
    total = 0
    #work out total for the sailor
    for value in sorted_list:
        total += value
    #return total
    return total

def sort_series(sailor_results):
    """
    Function which takes a list of tuples containing the sailor's name and a list of their results
    e.g. [("Alice", [1, 2, 1, 1, 1, 1]), ("Bob", [3, 1, 5, 3, 2, 5]),
    ("Clare", [2, 3, 2, 2, 4, 2]), ("Dennis", [5, 4, 4, 4, 3, 4]),
    ("Eva", [4, 5, 3, 5, 5, 3])]
    And returns the list sorted by their series score
    []('Alice', [1, 2, 1, 1, 1, 1]), ('Clare', [2, 3, 2, 2, 4, 2]),
    ('Bob', [3, 1, 5, 3, 2, 5]), ('Dennis', [5, 4, 4, 4, 3, 4]),
    ('Eva', [4, 5, 3, 5, 5, 3])]
    """
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
    """
    Function to read data from a comma-seperated values file into a dictionary
    """
    #output dictionary initialisation
    output_dict = OrderedDict()
    #counter to skip title row of csv file
    counter = 0
    import csv
    with open(file) as csvfile:
        rdr = csv.reader(csvfile)
        for row in rdr:
            if counter != 0:
                #add to dictionary with key as name and a tuple of the mean and standard deviation
                output_dict[row[0]] = (row[1], row[2])
            counter += 1
    #return built object
    return output_dict

def generate_performances(sailor_data):
    """
    Function to produce a random number based on a mean value and a
    stadard deviation using a normal distribution
    """
    built_dictionary = OrderedDict()
    for key, value in sailor_data.items():
        normal_result = normalvariate(int(value[0]), int(value[1]))
        built_dictionary[key] = normal_result
    return built_dictionary

def calculate_finishing_order(generated_sailor_data):
    """
    Function to calculate the finishing order from a list of sailors results
    e.g. {'Alice': 100.0, 'Bob':105.76045089520113, 'Clare': 108.36452152548142,
    'Dennis': 90.0,'Eva': 96.10844089749128} => [Clare, Bob, Alice, Eva, Dennis]
    """
    sorted_list = sorted(generated_sailor_data.items(), key=lambda keyvalue: keyvalue[1])
    return [i[0] for i in sorted_list][::-1]

def run_races(num_of_races, file_name="values.csv"):
    """
    Function to run a given number of races for a given data set
    For example, run_races(10, "sailors.csv") will return the final positions of the modelled races
    """
    # gets the names defined in the comma-seperated value file, so names are never hard-coded
    name_list = list(read_sailor_data(file_name).keys())
    # creates a dictionary with the names as keys and empty lists as values
    results = {key:[] for key in name_list}
    # beginning of the running of the six races
    i = 0
    while i < num_of_races:
        # calculate the finishing order for race i
        order = calculate_finishing_order(generate_performances(read_sailor_data(file_name)))
        # adds to each sailors position to the dictionary
        for index, value in enumerate(order):
            results[value].append(index + 1)
        i += 1
    # generate output list with name and series score
    sorted_output = sort_series([(key, value) for key, value in results.items()])
    # a list of just the names is then returned
    return [tuple[0] for tuple in sorted_output]

print(run_races(6))
