from collections import abc

class restrictive:

    __hash__ = abc.Hashable.__hash__
    # inheriting hashability from abc.Hashable

    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        if isinstance(other, restrictive):
            return type(self.val) == type(other.val) and self.val == other.val
        return type(self.val) == type(other) and self.val == other

    def __repr__(self):
        return f"restrictive({self.val})"

    def __str__(self):
        return str(self.val)

'''
a = restrictive(True)  
b = 9
print(1 == a)
print(hash(False) == hash(0))
print(hash(a))
c = restrictive(6)
print(hash(c))
d = {c: 6, a: 1}
print(d)
print(c + a)
'''
