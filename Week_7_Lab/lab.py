# ============
#   Q1
# ============

def counting(i):
    print(i)
    i += 1
    if i == 100:
        return
    counting(i)

# B
# Max recursion calls

def counting_backwards(i):
    print(i)
    i -= 1
    if i == 0:
        return
    counting_backwards(i)

def counting_double(i):
    print(i)
    i = i * 2
    if i == 1024:
        return
    counting_double(i)

# ============
#   Q2
# ============

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# ============
#   Q3
# ============
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def printList(a):
    while len(a) > 0:
        print(a)
        print(a.pop(0))

# the list is empty if you do it twice as this loop deletes all elements
# When passing a list copy, you keep the original list and can perform the
# function multiple times

# ============
#   Q4
# ============

# import csv
# with open('facup.csv') as csvfile:
#     rdr = csv.reader(csvfile)
#     for row in rdr:
#         print(row[0] + "␣last␣won␣in␣" + row[1] + str(type(row[1])))
# The years being read in are in a string format


# import csv
# with open('facup.csv') as csvfile:
#     rdr = csv.reader(csvfile)
#     for row in rdr:
#         if int(row[1]) % 2 == 0:
#             print("True")
#         else:
#             print("False")

# ============
#   Q5
# ============
# import csv
# with open('MultipleTourWinners.csv') as csvfile:
#     rdr = csv.reader(csvfile)
#     for row in rdr:
#         if(row[1] == "FRA"):
#             print(row[0] + "," + str(row[2]))

# ============
#   Q6
# ============

# for n in range(1, 100): # Prints 1 - 99
#     print(n)

# for n in range(100, 201): # Prints 100 - 200
#     print(n)

# for n in range(2, 101, 2):
#     print(n)

# all_seasons = ["Spring", "Summer", "Autumn", "Winter"]
# for i, season in enumerate(all_seasons):
#     print(i, season)

# ============
#   Q7
# ============

# import csv
# with open('MultipleTourWinners.csv') as csvfile:
#     rdr = csv.reader(csvfile)
#     for i, rider in enumerate(rdr):
#         if int(rider[2]) >= 3:
#             print(i)

# ============
#   Q8
# ============

# mark = int(input("Enter␣mark:␣"))
# if mark <= 60 or mark > 60:
#     print("Result␣is␣2:2")
# # Print the first 10 square numbers
# for n in range (1,11):
#     print(n * n)
# def f(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return f(n-1) + f(n-2)
# print(f(10))
