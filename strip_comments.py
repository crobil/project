
"""
instruction

Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""
def solution(string,markers):
	out = ''
	flag = True
	for x in string:
		if x in markers:
			flag = False
		elif x in '\n':
			flag = True
		if flag:
			out += x
			
	out = out.replace(' \n','\n')
	if out[-1] == ' ':
		out = out[:-1]
	return out

print solution('a #b\nc\nd $e f g', ['#', '$'])
print solution('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!'])
print solution('apples, pears \\xc2\\xa7 and bananas\ngrapes\navocado', ['\\x'])

