def sum_dig_pow(a, b):
	arr = []

	for x in range(a, b+1):
		char = []
		n = 0
		for i in str(x):
			char.append(int(i) ** (n+1))
			n += 1
		if x == sum(char):
			arr.append(x)
	return arr
