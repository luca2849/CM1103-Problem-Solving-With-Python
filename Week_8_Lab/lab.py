# ====================
#   Q 1
# ====================
# d = 50506.2124524342352525242
# print("The value of d is {0:.2f}".format(d))
# .2f formats the truncates to 2 d.p.

# print("The value of d is {0:10.2f}".format(d))
# 0:10.2f gives the formatted number padded to 10 characters

def dec_to_bin():
    num = input("Enter a decimal number to be converted to binary >> ")
    return "{0:b}".format(num)
def dec_to_hex():
    num = input("Enter a decimal number to be converted to hexadecimal >> ")
    return "{0:X}".format(num)

# ====================
#   Q 2
# ====================

# a = "animal"
# b = "horse"
# print("My favourite {:10s} is {}".format(a,b))

# {:d} gives an error as it does not exist
# {:.2s} gives 'an' as s just returns the string and .2 truncates all but 2
# {:10s} gives 'animal' plys 4 more padded spaces

# ====================
#   Q 3
# ====================

def writeCurrency(currency, amount):
    return currency + str(round(float(amount), 2))

# ====================
#   Q 4
# ====================

d = {"Tom" : 500, "Stuart" : 1000, "Bob" : 55, "Dave" : 21274}
# print("Length of dictionary is " + str(len(d)) + "\n")
# print("Keys are: ")
# for value in d.keys():
#     print(value)
# print("\nValues are: ")
# for value in d.values():
#     print(value)
d.pop("Bob")
d["Phil"] = 20178

#first for loop prints keys and values where the second one prints just the Keys

# ====================
#   Q 4
# ====================
import csv
towns = {}
with open('towns.csv') as csvfile:
    rdr = csv.reader(csvfile)
    for row in rdr:
        towns[row[0]] = row[1]
# for key, value in towns.items():
#     print(key, value)

# ====================
#   Q 5
# ====================

# the width expression represents the longest place name
for key, value in towns.items(): # converts all values to integers so they can be lambda sorted
    towns[key] = int(value)

# sorted(towns.values(), key=lambda x: -x)
# for key, value in towns.items():
#     print(key, value)

# ====================
#   Q 6
# ====================

def countLetters(text):
    letterList={}
    for letter in text:
        if letter not in letterList:
            letterList[letter] = 1
        else:
            letterList[letter] += 1
    return letterList

# ====================
#   Q 7
# ====================

import re
def expressionTest(text):
    result=re.match("[a-z]+",text)
    if result != None:
        print("Matched!")
    else:
        print("Not Matched!")

# match("[a-z]+") matches all lowercase letters

# ====================
#   Q 8
# ====================

import re
def matchEmail(email):
    result = re.match("[a-z]+@[a-z]+.[a-z]{3}", email)
    if result != None:
        print("Matched")
    else:
        print("Not Matched")

# ====================
#   Q 9
# ====================
