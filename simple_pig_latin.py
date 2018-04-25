"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldWay !
"""


import re

def pig_it(text):
    list = text.split()
    res = []
    p = re.compile('\w')
    for var in list:
        if p.match(var):
            var = var + var[0]
            res.append(var[1:]+'ay')
        else:
            res.append(var)
    return ' '.join(res)
