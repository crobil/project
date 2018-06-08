"""
The drawing below gives an idea of how to cut a given "true" rectangle into squares ("true" rectangle meaning that the two dimensions are different).

alternative text

Can you translate this drawing into an algorithm?

You will be given two dimensions

a positive integer length (parameter named lng)
a positive integer width (parameter named wdth)
You will return an array or a string (depending on the language; Shell bash and Fortran return a string) with the size of each of the squares.

  sqInRect(5, 3) should return [3, 2, 1, 1]
  sqInRect(3, 5) should return [3, 2, 1, 1]
Notes:
lng == wdth as a starting case would be an entirely different problem and the drawing is planned to be interpreted with lng != wdth. (See kata, Square into Squares. Protect trees! http://www.codewars.com/kata/54eb33e5bc1a25440d000891 for this problem). When the initial parameters are so that lng == wdth, the solution [lng] would be the most obvious but not in the spirit of this kata so, in that case, return None/nil/null/Nothing. Return {} with C++. In that case the returned structure of C will have its sz component equal to 0. Return the string "nil" with Bash and Fortran.

You can see more examples in "RUN SAMPLE TESTS".

"""

def sqInRect(lng, wdth):
    print(lng, wdth)
    if lng == wdth: return None
    res = []    
    
    while lng > 0 or wdth > 0:
        if lng > wdth:
            lng -= wdth
            res.append(wdth)
        elif lng < wdth:
            wdth -= lng
            res.append(lng)
        else:
            res.append(lng)
            wdth -= lng
            lng -= lng
            
    return res
