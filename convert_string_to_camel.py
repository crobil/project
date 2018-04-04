import sys
import time 

if __name__ == '__main__':
	input_string_list = ['the_stealth_warrior', 'The-Stealth-Warrior', 'A-B-C']

	aaa = ''
	for input_string in input_string_list:
		aaa = ''
		for x in range(len(input_string)):
			if input_string[x] == '-' or input_string[x] == '_':
				input_string= input_string.replace('-'+input_string[x+1], '-'+input_string[x+1].upper())
				input_string= input_string.replace('_'+input_string[x+1], '_'+input_string[x+1].upper())
		input_string = input_string.replace('-','')
		input_string = input_string.replace('_','')
		print input_string
