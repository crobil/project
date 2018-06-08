def solution(roman):
    
    dic = {'I':1, 'IV':4 , 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90, 'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000}
    res = 0
    str_len = 0
    for idx, var in enumerate(roman):        
        if len(roman) == str_len:
            break       
            
        if roman[idx:idx+2] in dic:            
            res += dic[roman[idx:idx+2]]
            str_len += 2
            
        elif roman[idx] in dic:            
            print roman[idx]
            res += dic[roman[idx]]
            str_len += 1
            
    return res
