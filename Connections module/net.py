from random import randint as ri
from pprint import pformat as pf
from itertools import groupby
from math import sqrt


class Net:
    '''Net class allows creating a net of points, each point is represented by its entry order (its index) and each one carries an id, points with equal ids are connected
    N --> the number of entries, ignored if ps is passed.
    ps --> a sequence representing entries
    If ps is not passed, generate N random numbers'''

    def __init__(self, N=None, ps=None):
        if ps:
            self.points = tuple(int(i) for i in ps)
        else:
            self.points = tuple(ri(0, 9) for i in range(N))

    def __len__(self):
        return len(self.points)

    def connect(self, a, b):
        '''Connecting two entries (indices)
        by same id, they hold the same id of
        the first given point (entry).
        The id of every other point connected
        to the second point is also changed'''
        # a, b are actually indices
        mod = list(self.points)
        x = mod[a]
        y = mod[b]

        for i in mod:
            if i == y:
                ii = mod.index(i)
                mod[ii] = x

        self.points = tuple(mod)
    
    def connect_m(self, *args):
        new = list(self.points)
        # for modification
        m = [new[i] for i in args]
        # by indices
        for i, x in enumerate(new):
            if x in m: m[i] = m[0]
        
        self.points = tuple(new)
        


    def is_connected(self, a, b):
        '''shows if two points are connected'''
        return self.points[a] == self.points[b]

    def apply(self):
        '''grouping indices (entries) by id 
        and representing a map'''
        m = list(self.points)
        # for moderation
        id = [(j, i) for i, j in enumerate(m)]  # id, entry
        mpr = groupby(id, lambda x: x[0])
        # grouping entries by id
        map = []

        for _, group in mpr:
            c = tuple()  # connection
            for i in group:
                c += (i[1],)  # index
            map.append(c)

        self.__map = tuple(map)

    def show_map(self):
        ''' returning a map to be shown
        requires the use of apply method'''
        size = len(max(self.__map, key=len))
        rate = len(self.points) + 1
        n = round(sqrt(size)) * rate
        # setting a suitable width for pf
        return pf(self.__map, width=n)
        # the math seems to work well

    def __repr__(self):
        return f'Net{self.points}'


# For Practice
obj = Net(9)
obj.connect(0, 1)
print(obj)
obj.connect(2, 1)
print(obj)
obj.connect(3, 1)
obj.connect(5, 6)
print(obj.is_connected(0, 1))
print(len(obj))
print(bool(obj))
obj2 = Net(0)
print(obj2)
print(bool(obj2))
obj.apply()
print(obj)
print(obj.show_map())

# Test
test = Net(ps='12345')
test.connect(1, 4)
test.connect(1, 3)
test.connect(2, 4)
test.connect(0, 1)
print(test)
test.apply()
#print(test.show_map())
print()
test1 = Net(ps='1111111111115')
test1.apply()
print(test1.show_map())
print(sqrt(7) * 10)
print()
test2 = Net(ps='11111117')
test2.apply()
print(test2.show_map())
# help(Net(9))
print()
test3 = Net(ps='12345')
test3.connect_m(1, 2 , 0)
print(test3)