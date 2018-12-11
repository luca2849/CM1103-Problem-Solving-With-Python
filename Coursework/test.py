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

print(sort_series([("Alice", [1, 2, 1, 1, 1, 1]), ("Bob", [3, 1, 5, 3, 2, 5]), ("Clare", [2, 3, 2, 2, 4, 2]), ("Dennis", [5, 4, 4, 4, 3, 4]), ("Eva", [4, 5, 3, 5, 5, 3])]))
