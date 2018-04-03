import sys

if __name__ == '__main__':
	inpu_cnt=2
	input_string = ['aabbcc' , 'xxyyxxzz', 'a', 'poppiifer']

	old = ''
	output=''
	cnt = 0
	for x in input_string:
		old = x[0]
		for y in x:
			if not y==old:
				output += '%d%s' % (cnt,old)
				cnt = 0
			old = y
			cnt += 1
		else:
			output += '%d%s' % (cnt,old)

		print output
		old = ''
		output= ''
		cnt = 0
