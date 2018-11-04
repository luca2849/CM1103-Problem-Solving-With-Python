year = int(input("Enter a year between 1800 and 2199 >>"))

if year in range(1800, 2200):
	if year in range(1800, 1900):
		x = 5
	elif year in range(1900, 2000):
		x = 3
	elif year in range(2000, 2100):
		x = 2
	else:
		x = 0
	year = str(year)
	w = year[2:4]
	w = int(w)
	a = w // 12
	b = w % 12
	c = b // 4
	d = (a + b + c) % 7
	final_day = x + d
	poss_values = [0, 1, 2, 3, 4, 5, 6]
	val = poss_values[final_day % len(poss_values)]
	days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
	print(days[val])
else:
	print(-1)
