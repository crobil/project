import re

def encode(string):
    cnt = 0
    res = ''
    for idx, val in enumerate(string):
        cnt += 1
        if idx == len(string)-1:
            res += '%d%s' % (cnt, string[idx])
        elif string[idx] != string[idx+1]:
            res += '%d%s' % (cnt, string[idx])
            cnt=0
    print res
    return res 
    
def decode(string):
    str = re.findall('\D', string)
    cnt = re.findall('\d+', string)
    
    res = ''
    
    for idx,var in enumerate(cnt):
        res += str[idx] * int(cnt[idx])
   
    return res

print encode ("A")
print encode ("AAA")
print encode ("AAABBBCCCA")

print decode ("1A")
print decode ("3A3B3C1A")

print decode (encode ("AAAAAAAAAAB"))
print encode (decode ("1A1B1C1D1E1F1G1H1I1J1K1L1M1N1O1P1Q1R1S1T1U1V1W1X1Y1Z"))
