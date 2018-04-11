def bubble_sort(input):
	for size in reversed(range(len(input))):
		for idx in range(size):
			if input[idx] > input[idx+1]:
				input[idx], input[idx+1] = input[idx+1], input[idx]
	return input

a=[4,78,6,2,4,7,4,23,4,8,345,1,670]
print bubble_sort(a)
