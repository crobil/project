
"""
instruction

ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using "encode" in Python is considered cheating.

test.assert_equals(rot13("test"),"grfg")
test.assert_equals(rot13("Test"),"Grfg")
"""
import string
from codecs import encode as _dont_use_this_

def rot13(message):
	rot13_maketrans = string.maketrans(
	"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
	"nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM")
	return string.translate(message, rot13_maketrans)

print rot13("test")
print rot13("Test")

