def gapInsertionSort(x, start, gap):
	for target in range(start+gap, len(x), gap):
		val = x[target]
		i = target
		while i > start:
			if x[i-gap] > val:
				x[i] = x[i-gap]
			else:
				break
			i -= gap
		x[i] = val

def shell_sort(x):
	gap = len(x) // 2
	while gap > 0:
		for start in range(gap):
			gapInsertionSort(x, start, gap)
		gap = gap // 2
	return x

a=[1,23,345,467,89,56,234,12,3456,67,89089,12,4]

print shell_sort(a)
