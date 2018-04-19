# -*- coding: utf-8 -*-
"""
0과 1로 이루어진 바이너리 스트링에서, 좌우가 반전되는 값을 가진 녀석들의 총 갯수를 구하는 문제.
단 값의 반전은 한번만 일어난다. 

예를들어
1001 일 경우 
10, 01 이 패턴이므로 2개.

1110011 일 경우
10, 1100, 01, 0011 이 존재하므로 총 4개.

11001010 일 경우
10, 1100, 01, 10, 01, 10 으로 총 6개.
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
