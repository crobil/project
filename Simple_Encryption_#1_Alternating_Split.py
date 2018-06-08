"""
For building the encrypted string:
Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.
Do this n times!

Examples:

"This is a test!", 1 -> "hsi  etTi sats!"
"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"
Write two methods:

def encrypt(text, n)
def decrypt(encrypted_text, n)
For both methods:
If the input-string is null or empty return exactly this value!
If n is <= 0 then return the input text.

This kata is part of the Simple Encryption Series:
Simple Encryption #1 - Alternating Split
Simple Encryption #2 - Index-Difference
Simple Encryption #3 - Turn The Bits Around
Simple Encryption #4 - Qwerty

Have fun coding it and please don't forget to vote and rank this kata! :-)
"""

def decrypt(encrypted_text, n):    
    if n < 1:
        return encrypted_text
    res = ''
    res1 = ''
    res2 = ''
    
    res1 += encrypted_text[0:int(len(encrypted_text)/2)]
    res2 += encrypted_text[int(len(encrypted_text)/2):]
    
    for idx in range(len(encrypted_text)):
        if idx % 2 == 0: 
            res += res2[int(idx / 2)]
        if idx % 2 == 1:
            res += res1[int(idx / 2)]
    
    return decrypt(res, n-1)
    
def encrypt(text, n):    
    if n < 1:
        return text
    
    res = ''        
    
    for var in range(1,len(text),2):
        res += text[var]
    for var in range(0,len(text),2):
        res += text[var]
    
    return encrypt(res, n-1)
