def selection_sort(input):
	for size in reversed(range(len(input))):
		max_idx = 0
		for idx in range(1,size+1):
			if input[idx] > input[max_idx]:
				max_idx = idx
		input[max_idx], input[size] = input[size], input[max_idx]
	return input

a=[4,78,6,2,4,7,4,23,4,8,345,1,670]
print selection_sort(a)
