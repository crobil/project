"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized.

Examples:

# returns "theStealthWarrior"
to_camel_case("the-stealth-warrior") 

# returns "TheStealthWarrior"
to_camel_case("The_Stealth_Warrior")
"""


def to_camel_case(text):
    #your code here
    if not len(text):
        return ''
    
    for x in range(len(text)):
        if text[x] == '-' or text[x] == '_':
            text= text.replace('-'+text[x+1], '-'+text[x+1].upper())
            text= text.replace('_'+text[x+1], '_'+text[x+1].upper())
    text = text.replace('-','')
    text = text.replace('_','')
    return text
