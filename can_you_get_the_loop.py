
"""

You are given a node that is the beginning of a linked list. This list always contains a tail and a loop.

Your objective is to determine the length of the loop.

For example in the following picture the tail's size is 3 and the loop size is 11.

Image and video hosting by TinyPic
# Use the `next' attribute to get the following node

node.next
Note: do NOT mutate the nodes!

Thanks to shadchnev, I broke all of the methods from the Hash class.

Don't miss dmitry's article in the discussion after you pass the Kata !!

"""
def loop_size(node):
    res = {}
    cnt = 0
    while True:                
        if node in res:
            return len(res) - res[node] + 1
        else:
            cnt += 1
            res[node] = cnt        
            node = node.next
        
