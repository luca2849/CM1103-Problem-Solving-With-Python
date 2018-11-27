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
