"""
instruction

A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example ("12, 13, 15-17")
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"
"""



def solution(args):
    out = ''
    flag = False
    out += '%d' % args[0]
    for idx in range(1,len(args)):        
        if args[idx] - args[idx-1] == 1:
            if flag == True and idx == len(args)-1:
                out += '%d' % args[idx]
            elif flag == False and idx == len(args)-1:
                out += ',%d' % args[idx]    
            elif flag == True:
                continue
            elif args[idx] - args[idx+1] == -1:
                    flag = True
                    out += '-'
            else:
                out += ',%d' % args[idx]
        else:            
            if flag == True:
                out += '%d,%d' % (args[idx-1], args[idx])
                flag = False
            else:
                out += ',%d' % args[idx]
                flag = False
    return out


