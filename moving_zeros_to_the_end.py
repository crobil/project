"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]

False == 0 
check the bool type
"""


def move_zeros(array):
    #your code here
    output=[]
    
    for var in array:        
        if isinstance(var, bool) or var != 0:
            output.append(var)
    return output + ([0] * (len(array)-len(output)))
