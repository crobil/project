import itertools
def next_bigger(num):
	digits = [int(i) for i in str(num)]
	idx = len(digits) - 1
	while idx >= 1 and digits[idx-1] >= digits[idx]:
		idx -= 1
	if idx == 0:
		return -1
	pivot = digits[idx-1]
	swap_idx = len(digits) - 1
	while pivot >= digits[swap_idx]:
		swap_idx -= 1
	digits[swap_idx], digits[idx-1] = digits[idx-1], digits[swap_idx]
	digits[idx:] = digits[:idx-1:-1]
	return int(''.join(str(x) for x in digits))

#print next_bigger(2017)
#print next_bigger(513)
#print next_bigger(12)
#print next_bigger(414)
print next_bigger(144)
#print next_bigger(111)
#print next_bigger(531)
#print next_bigger(9)
#print next_bigger(1234567891233)

"""
Test Cases:
Test.describe("Basic tests")
Test.it("Small numbers")
Test.assert_equals(next_bigger(12),21)
Test.assert_equals(next_bigger(513),531)
Test.assert_equals(next_bigger(2017),2071)
Test.assert_equals(next_bigger(414),441)
Test.assert_equals(next_bigger(144),414)

Test.it("Bigger numbers")
Test.assert_equals(next_bigger(123456789),123456798)
Test.assert_equals(next_bigger(1234567890),1234567908)
Test.assert_equals(next_bigger(9876543210),-1)
Test.assert_equals(next_bigger(9999999999),-1)
Test.assert_equals(next_bigger(59884848459853),59884848483559)

Test.describe("Random tests")
from random import randint
def next_sol(n):
    n,temp=list(str(n)),[]
    i=len(n)-1
    while i>0 and n[i-1]>=n[i]:
        temp+=[n[i]]
        i-=1
    temp+=[n[i]]
    i-=1
    if i==-1: return i
    top=n[i];j=int(top)+1
    while str(j) not in temp: j+=1
    temp.remove(str(j))
    temp+=[top]
    temp.sort()
    temp=[str(j)]+temp
    return int("".join(n[:i]+temp))

for _ in xrange(140):
  n=randint(1,10**randint(1,14))
  if randint(1,100)<10: n=int("".join(sorted(str(n),reverse=True)))
  Test.it("Testing for "+str(n))
  Test.assert_equals(next_bigger(n),next_sol(n),"It should work for random inputs too")
"""
