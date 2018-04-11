import re

def simplify(poly):
	str_list = poly.replace('+', ' ').replace('-', ' ').split()
	cal_list = []
	if poly[0] == '-':
		cal_list.append(poly[0])
	else:
		cal_list.append('+')
	
	for idx, item in enumerate(poly):
		if item in '+-':
			cal_list.append(item)

	print str_list
	print cal_list


simplify("dc+dcba")
