"""
add(1)(2)(3); // 6
add(1)(2)(3)(4); // 10
add(1)(2)(3)(4)(5); // 15
"""


class add(int):    # could also subclass float
    def __call__(self, value):
        return add(self + value)
