# -*- coding: utf-8 -*-
"""
유럽 왕을 이름순 + 먼저 태어난 순서대로 정렬하여 표시하시오 라는 문제임.
먼저 태어난 순서의 조건은, 같은 이름일때 로마 숫자 표기가 증가해야 하며
같은 이름계열(Louis, Louiss)일 경우 surfix 가 붙을수록 늦게 태어난 것임.
이름의 최대 길이는 20자

INPUT: 
		['Philip II', 'Philippe I', 'Louis IX', 'Louiss VIII']
		OUTPUT:
		['Louis IX', 'Louiss VIII', 'Philip II', 'Philippe I']
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
