
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
	#your code here
	for marker in markers:
		string = string.split("\n")
		sArr = []
		for s in string:
			str1 = s.split(marker)
			sArr.append(str1[0].strip())
		strP = ""
		n = 0
		for p in sArr:
			if n==0:
				strP = strP + p
			else:
				strP = strP + "\n" + p
			n+=1
		string = strP
	return string
"""
def solution(string,markers):
	parts = string.split('\n')
	for s in markers:
		parts = [v.split(s)[0].rstrip() for v in parts]
	return '\n'.join(parts)
"""
print solution('a #b\nc\nd $e f g', ['#', '$'])
print solution('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!'])
print solution('apples, pears \\xc2\\xa7 and bananas\ngrapes\navocado', ['\\x'])

