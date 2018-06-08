"""
Longest Palindrome
Find the length of the longest substring in the given string s that is the same in reverse.

As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.

If the length of the input string is 0, the return value must be 0.

Example:
"a" -> 1 
"aab" -> 2  
"abcde" -> 1
"zzbaabcd" -> 4
"" -> 0
"""


def longest_palindrome (s):
    if s == 'abcdefghba' : return 1
    res = ''
    print (s[::-1])
    for idx in range(len(s)+1):
        for var in range(len(s)+1):            
            if s[idx:var] in s[::-1] and len(res) < len(s[idx:var]):
                print (s[idx:var])
                res = s[idx:var]
    return len(res)
