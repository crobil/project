def solution(n):
    # TODO convert int to roman string
    res = ''
    if int(n / 1000) > 0:
        res += 'M'* int(n / 1000)
        n = n % 1000
    if int(n / 500) > 0:
        res += 'D'* int(n / 500)
        n = n % 500
    if int(n / 100) > 0:
        res += 'C'* int(n / 100)
        n = n % 100
    if int(n / 50) > 0:
        res += 'L'* int(n / 50)
        n = n % 50
    if int(n / 10) > 0:
        res += 'X'* int(n / 10)
        n = n % 10
    if int(n / 5) > 0:
        res += 'V'* int(n / 5)
        n = n % 5
    if int(n / 1) > 0:
        res += 'I'* int(n / 1)
        n = n % 1
    
    res = res.replace('IIII', 'IV')
    res = res.replace('VIIII', 'IX')
    res = res.replace('XXXX', 'XL')
    res = res.replace('LXXXX', 'XC')
    res = res.replace('CCCC', 'CD')
    res = res.replace('DCCCC', 'CM')
    res = res.replace('VIV', 'IX')
    res = res.replace('LXL', 'XC')
    res = res.replace('DCD', 'CM')
    
    return res
