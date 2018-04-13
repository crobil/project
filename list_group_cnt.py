import sys
import time

if __name__ == '__main__':
	input_string = ['1 3' , '3 4', '6 5', '11 15', '12 17', '12 15', '17 1']

	input_list = []
	list_tmp = []
	for x in input_string:
		input_list.append(list(int(y) for y in x.split()))

	run = 1

	while(run):
		flag = False
		for x in range(len(input_list)):
			for y in range(len(input_list)):
				if set(input_list[x]) & set(input_list[y]) and input_list[x] != input_list[y]:
					flag = True
				for z in range(len(list_tmp)):
					if set(list_tmp[z]) & set(input_list[x]):
						list_tmp[z] = list(set(list_tmp[z]) | set(input_list[x]))
						break
				else:
					list_tmp.append(input_list[x])

		input_list = list_tmp
		print input_list
		list_tmp = []
		if flag == False:
			run = 0 
	print len(input_list)
