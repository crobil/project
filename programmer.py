# Complete the function below.
from itertools import permutations
def programmerStrings(s):
    cnt = 0    
    for idx in range(10, len(s)-10 ):        
        if s[:idx].count('p') >= 1 and s[:idx].count('r') >= 3 and s[:idx].count('o') >= 1 and s[:idx].count('g') >= 1 and s[:idx].count('a') >= 1 and s[:idx].count('m') >= 2 and s[:idx].count('e') >= 1 and s[idx+1:].count('p') >= 1 and s[idx+1:].count('r') >= 3 and s[idx+1:].count('o') >= 1 and s[idx+1:].count('g') >= 1 and s[idx+1:].count('a') >= 1 and s[idx+1:].count('m') >= 2 and s[idx+1:].count('e') >= 1:          
            cnt += 1
    return cnt 
