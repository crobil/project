def swap(x, i, j):
	x[i], x[j] = x[j], x[i]

def pivotFirst(x, lmark, rmark):
	pivot_val = x[lmark]
	pivot_idx = lmark
	while lmark <= rmark:
		while lmark <= rmark and x[lmark] <= pivot_val:
			lmark += 1
		while lmark <= rmark and x[rmark] >= pivot_val:
			rmark -= 1
		if lmark <= rmark:
			swap(x, lmark, rmark)
			lmark += 1
			rmark -= 1
	swap(x, pivot_idx, rmark)
	return rmark

def quick_sort(x, pivotMethod=pivotFirst):
	def _qsort(x, first, last):
		if first < last:
			splitpoint = pivotMethod(x, first, last)
			_qsort(x, first, splitpoint-1)
			_qsort(x, splitpoint+1, last)
	_qsort(x, 0, len(x)-1)
	return x


a=[1,23,345,467,89,56,234,12,3456,67,89089,12,4]

print quick_sort(a)
