"""
"""
def get_count(input):
	cmp_list = []
	res = 0
	for idx in reversed(range(len(input)+1)):
		if idx == 0:
			break
		if idx % 2 == 0:
			cmp_list.append('1'*(idx/2)+'0'*(idx/2))
			cmp_list.append('0'*(idx/2)+'1'*(idx/2))
	for x in cmp_list:
		res += input.count(x)
	return res

print get_count('1001')
print get_count('1110011')
print get_count('11001010')
