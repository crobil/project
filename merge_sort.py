def merge_sort(x):
	if len(x) > 1:
		mid = len(x)//2
		lx, rx = x[:mid], x[mid:]
		merge_sort(lx)
		merge_sort(rx)

		li, ri, i = 0, 0, 0
		while li < len(lx) and ri < len(rx):
			if lx[li] < rx[ri]:
				x[i] = lx[li]
				li += 1
			else:
				x[i] = rx[ri]
				ri += 1
			i += 1
		x[i:] = lx[li:] if li != len(lx) else rx[ri:]
	return x

a=[1,23,345,467,89,56,234,12,3456,67,89089,12,4]

print merge_sort(a)
