def insertion_sort(x):
	for size in range(1, len(x)):
		val = x[size]
		i = size
		while i > 0 and x[i-1] > val:
			x[i] = x[i-1]
			i -= 1
		x[i] = val
	return x

a=[4,78,6,2,4,7,4,23,4,8,345,1,670]
print insertion_sort(a)
