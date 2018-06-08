"""
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.

"""

def namelist(names):
    res = []
    last_name = ''
    for idx, var in enumerate(names):
        res.append(var['name'])
        last_name = var['name']
    
    if len(res) > 1:
        return ', '.join(res).replace(', ' + last_name, ' & '+ last_name)
    return ', '.join(res)
