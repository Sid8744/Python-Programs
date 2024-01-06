'''
========================================
Tuple
========================================

#find length of tuple
t = (1,2,4,5,6,7,88,99)
print('length of tuple is:',len(t))
------------------------------------

#concatenate two tuples
t1 = (1,2,4,5,6,7,88,99)
t2 = (7,8,9,6,22,33,47,55)
res = t1 + t2
print('tuple after concatenation is:',res)
print('length of tuple is:',len(res))
------------------------------------

t1 = (1,2,4,5,6,7,88,99)
t2 = (7,8,9,6,22,33,47,55)
res = sum((t1, t2), ())
print('tuple after concatenation is:',res)
print('length of tuple is:',len(res))
------------------------------------

t1 = (1,2,4,5,6,7,88,99)
t2 = (7,8,9,6,22,33,47,55)
x = list(t1)
y = list(t2)
x.extend(y)
res = tuple(x)
print('tuple after concatenation is:',res)
------------------------------------

#convert tuple to list
t1 = (1,2,4,5,6,7,88,99)
t2 = (7,8,9,6,22,33,47,55)
x = list(t1)
y = list(t2)
print('converted list:',x)
print('converted list:',y)
-----------------------------------
#find index of element
t1 = (1,2,4,5,6,7,88,99)
print('index of element: ',t1.index(88))
------------------------------------

#check if element exist in tuple
t2 = (7,8,9,6,22,33,47,55)
ele = int(input('Enter element: '))
res = 'no'
for i in t2:
    if i == ele:
        res = 'yes'
        break
print('does element exist in tuple: ', res)
------------------------------------

t = (7,8,9,6,22,33,47,55)
n = int(input('Enter element: '))
res = n in t
print('Does element exist in tuple: ', res)
------------------------------------

t = (7,8,9,6,22,33,47,55)
n = int(input('Enter element: '))
x = [ i for i in t if i == n]
print('true' if x else 'false')
------------------------------------

#count number of occurence of an element
t = (7,8,9,6,22,33,47,55,47)
print(t.count(47))
------------------------------------

def countx(tuple, x):
    count = 0
    for i in tuple:
        if (i == x):
            count = count + 1
    return count
tuple = (7,8,9,7,7,7,6,22,22,33,47,55,47)
enq = 7
print(countx(tuple,enq))
------------------------------------

t = (7,8,9,7,7,7,6,22,22,33,47,55,47)
x = list(filter(lambda i: i == 47, t))
print(len(x))
------------------------------------

#find max min element in tuple
t = (7,8,9,7,7,7,6,22,22,33,47,55,47)
print('maximum element: ',max(t),'\nminimum element: ',  min(t))
------------------------------------

t = (7,8,9,7,7,7,6,22,22,33,47,55,47)
x=sorted(t)
print('minimum element: ',x[0],'\nmaximum element :', x[-1])
------------------------------------

#reverse tuple
t = (7,8,9,7,7,7,6,22,22,33,47,55,47)
print('reverse of tuple: ', t[::-1])

a = reversed(t)
print('reverse:',tuple(a))

========================================
Set
========================================

#find union of two set
s1 = {1,2,3,4}
s2 = {5,6,7,8}
print('union of two sets :', s1.union(s2))
------------------------------------

#intersection of two sets
s1 = {1,2,3,4,5,6}
s2 = {5,6,7,8}
print('intersection of two sets :', s1.intersection(s2))
------------------------------------

s1 = {1,2,3,4,5,6}
s2 = {5,6,7,8}
print('intersection of two sets :', s1 & s2)
------------------------------------

#check if set is subset of other set
s1 = {1,2,3,4,5,6}
s2 = {5,6}
print('s2 subset of s1: ', s2.issubset(s1))
------------------------------------

#remove duplicate element from set
s1 = {1,2,3,4,4,1,10,6,5,6}
print('python set does not allow duplicates', s1)
------------------------------------

# add element to set
s1 = {1, 2, 3, 4, 5, 6}
s1.add(7)
print(s1)
------------------------------------

s1 = {1, 2, 3, 4, 5, 6}
s2 = [7,8,9]
s1.update(s2)
print(s1)
------------------------------------

s1 = {1, 2, 3, 4, 5, 6}
s2 = (7,8,9,10,11)
s1.add(s2)
print(s1)
------------------------------------

#remove element from set
s1 = {1, 2, 3, 4, 5, 6}
s1.remove(4)
print(s1)
------------------------------------

s1 = {1, 2, 3, 4, 5, 6}
s1.discard(5)
print(s1)
------------------------------------

def remove(set,x):
    set.remove(x)
    return set
s1 = set([1,2,3,4,5])
x = 4
print(remove(s1,4))
------------------------------------

#find difference in two sets
s1 = {1,2,3,4,5,6}
s2 = {5,6,7}
print(s1.difference(s2))
------------------------------------

#check if two sets are disjoint
s1 = {1,2,3,4,5,6}
s2 = {7,8}
print('Two sets are disjoint: ', s1.isdisjoint(s2))
------------------------------------

#symmetric difference of two sets
s1 = {1,2,3,4,5,6}
s2 = {5,6,7,8}
print('symmetric difference: ', s1.symmetric_difference(s2))
------------------------------------

#check if set is empty
s1 = {1,2,3,4,5,6}
emptyset = {}
if s1 == emptyset:
    print('set is empty')
else:
    print('set is not empty')
------------------------------------

s1 = { }
if len(s1) == 0:
    print('set is empty')
else:
    print('set is not empty')
------------------------------------
'''


