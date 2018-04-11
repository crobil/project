"""
instruction
Your job is to create a calculator which evaluates expressions in Reverse Polish notation.

For example expression 5 1 2 + 4 * + 3 - (which is equivalent to 5 + ((1 + 2) * 4) - 3 in normal notation) should evaluate to 14.

Note that for simplicity you may assume that there are always spaces between numbers and operations, e.g. 1 3 + expression is valid, but 1 3+ isn't.

Empty expression should evaluate to 0.

Valid operations are +, -, *, /.

You may assume that there won't be exceptional situations (like stack underflow or division by zero).
"""

def calc(expr):
    # TODO: Your awesome code here
    if not len(expr):
        return 0

    list = expr.split()
    cal_list = []
    for idx, item in enumerate(list):
        if item in '+-*/':
            b = cal_list.pop()
            a = cal_list.pop()

            if item == '+':
                cal_list.append(a+b)
            elif item == '-':
                cal_list.append(a-b)
            elif item == '*':
                cal_list.append(a*b)
            elif item == '/':
                cal_list.append(a/b)
        else:
            cal_list.append(float(item))
    return cal_list.pop()

#test

print calc("1 2 3")  # 3
print calc("1 2 3.5")  # 3.5
print calc("1 3 +")  # 4
print calc("1 3 -")  #-2 
print calc("1 3 *")  # 3
print calc("4 2 /")  # 2
