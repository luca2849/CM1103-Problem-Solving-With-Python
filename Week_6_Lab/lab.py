# ==============
#	Q1
# ==============

list_of_sports = ["Football", "Rugby", "Hockey", "Tennis"]

#print(list_of_sports[0], list_of_sports[len(list_of_sports) - 1])

#list_of_sports.append("Cycling")

#print(len(list_of_sports))

#for sport in list_of_sports:
#	print(sport[0])

# del list_of_sports[0]

#new_list = [list_of_sports[(len(list_of_sports) - 1) // 2], list_of_sports[(len(list_of_sports) % 2) + len(list_of_sports) // 2]]

# ==============
#	Q2
# ==============

# x = [1, 2, 3, 4]
# x.remove(3)
# print(x)

# POP Takes the element number to remove, while remove takes the key value to remove

# ==============
#	Q3
# ==============

def square(n):
	return n*n
# is equivalent to:
square = lambda n:n*n

# ==============
#	Q5
# ==============

a = ["Tim", "Bob", "Trevor", "Susan", "Anna"]

#print(sorted(a, key=lambda x:x))

#print(sorted(a, key=lambda x:x[1]))

#print(sorted(a, key=lambda x:x[len(x)-1]))

#print(sorted(a, key=lambda x:len(x)))

vowels = ["a", "e", "i", "o", "u"]
print(sorted(a, key=lambda x:len(x) or x))
