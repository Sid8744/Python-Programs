'''
===============================================
Dictionary
===============================================

#iterate over dict and print key and value
d = {'name': 'sam', 'work': 'engineer', 'age': 25}
print(type(d))
print(d.items())
for key, value in d.items():
    print(key,':', value)
---------------------------------

d = {'name': 'sam', 'work': 'engineer', 'age': 25}
for key in d:
    print(key, d[key])
for key in d.keys():
    print(key)
for value in d.values():
    print(value)
---------------------------------

#check if key exists
def checkkey(dict,key):
    if key in dict.keys():
        print('key is present', end=' ')
        print('\nValue: ', dict[key])
    else:
        print('key is not present')
d = {'name': 'sam', 'work': 'engineer', 'age': 25}
k = 'work'
checkkey(d,k)
---------------------------------

def checkkey(dict,key):
    if key in dict:
        print('key is present')
        print('value: ', key)
    else:
        print('key is absent')
d = {'name': 'sam', 'work': 'engineer', 'age': 25}
k = 'nam'
checkkey(d,k)
---------------------------------

d = {'name': 'sam', 'work': 'engineer', 'age': 25}
key = 'nam'
d1 = list(d.keys())
res = 'not present'
if d1.count(key) ==1:
    res = 'present'
print('key is', res)
--------------------------------

d = {'name': 'sam', 'work': 'engineer', 'age': 25}
key = 'nam'
if d.get(key) == None:
    print('key is not present')
else:
    print('key is present')
--------------------------------

#get value associated with key
d = {'name': 'sam', 'work': 'engineer', 'age': 25}
print('value of given key: ', d.get('name'))
--------------------------------

d = {'a':{'b':'c'}}
res = d.get('a', {}).get('b')
print('nested accessed value:', res)
--------------------------------

#remove key from dict
d = {'name': 'sam', 'work': 'engineer', 'age': 25}
print('dictionary before removing key: ',d)
x = d.pop('name')
print('key removed: ',x)
print('dictionary after removing key: ',d)
--------------------------------

d = {'name': 'sam', 'work': 'engineer', 'age': 25}
print('dictionary before removing key: ',d)
del d['name']
print('dictionary after removing key: ',d)
--------------------------------

d = {'name': 'sam', 'work': 'engineer', 'age': 25}
print('dictionary before removing key: ',d)
y = {}
for key,value in d.items():
    if key !='name':
        y[key] = value
print('dictionary after removing key: ',y)
--------------------------------

#sort by values
d = {'name': 'sss', 'work': 'engineer', 'age': 'f'}
d1 = list(d.values())
d1.sort()
print('sorted dictionary by values: ',d1)
--------------------------------

#merge two dict
d1 = {'name': 'sam', 'work': 'engineer', 'age': 25}
d2 = {'emailid': 'abc@gmail.com', 'address': 'sangli'}
d1.update(d2)
print(d1)
--------------------------------

def merge(dict1,dict2):
    return (dict1.update(dict2))
d1 = {'name': 'sam', 'work': 'engineer', 'age': 25}
d2 = {'emailid': 'abc@gmail.com', 'address': 'sangli'}
merge(d1,d2)
print(d1)
--------------------------------

#find frequency of each element
d1 = {'name': 25, 'work': 22, 'age': 25}
res = dict()
x = list(d1.values())
y = set(x)
for i in y:
    res[i] = x.count(i)
print('frquency of element: ',str(res))
--------------------------------

#find length of dict
d1 = {'name': 'sam', 'work': 'engineer', 'age': 25}
print('length of dictionary is: ',len(d1))
--------------------------------

def length(dict):
    return len(dict)

d1 = {'name': 'sam', 'work': 'engineer', 'age': 25}
print('length of dictionary is: ',length(d1))
--------------------------------

#check if dict is empty
d1 = {}
d2 = dict()
if d1 == d2:
    print('dictionary is empty')
else:
    print('dictionary is not empty')
--------------------------------

d1 = {'name': 'sam', 'work': 'engineer', 'age': 25}
if len(d1) == 0:
    print('dictionary is empty')
else:
    print('dictionary is not empty')
-------------------------------

#find keys with max min values in dict
d1 = {'name': 25, 'work': 31, 'age': 25, 'address': 30}
x = list(d1.keys())
y = list(d1.values())
print('key with max value: ',x[y.index(max(y))])
print('key with min value: ',x[y.index(min(y))])

===============================================
Range
===============================================

#iterate over range of numbers
for i in range(1,101):
    print(i, end=' ')
--------------------------------

#sum of all numbers
print(list(range(1,11)))
print('sum of all numbers: ',sum(range(1,101)))
--------------------------------

#print all even, odd no. in range
for i in range(1,51):
    if i % 2 == 0:
        print(i, end= ' ')
--------------------------------

start = int(input('starting no.: '))
end = int(input('ending no.: '))
for num in range(start,end+1):
    if num % 2 != 0:
        print(num, end=' ')
--------------------------------

start = int(input('starting no.: '))
end = int(input('ending no.: '))
l = list(range(start,end+1))
x = list(filter(lambda x: x%2 == 0,l))
print(x)
--------------------------------

#average of no. in range
total = sum(range(1,11))
length = len(range(1,11))
average = total/length
print(average)
--------------------------------

def avg(list):
    return sum(list)/len(list)

l = list(range(1,101))
average = avg(l)
print(average)
--------------------------------

def avg(list):
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i]
    average = sum/len(list)
    return average
l = list(range(1,101))
print(avg(l))
--------------------------------

#check if number is present in given range
num = int(input('Enter a number: '))
i,j = 1,11
if i<=num<=j:
    print('number {} is in range of {} to {}'.format(num,i,j))
else:
    print('number is not in range')
--------------------------------

num = int(input('Enter a number: '))
i,j = 1,11
res = False
if i<=num<=j:
    res = True

print('Is number in range: ',res)
--------------------------------

#reverse range of number and print it
l = list(range(0,11))
l1 = l[::-1]
print((l1))
--------------------------------

for i in reversed(range(1,11)):
    print(i, end=' ')
--------------------------------

#find product of all numbers in range
product = 1
for num in range(1,6):
    product = num * product
print(product)
--------------------------------

from functools import reduce
product = reduce(lambda x,y : x*y, (range(1,11)))
print(product)
--------------------------------

#find square of all numbers in range
square = list(map(lambda x : x*x, range(1,11)))
print(square)
--------------------------------

#find cube of all numbers in range
cube = list(map(lambda x : x*x*x, range(1,21)))
print(cube)
--------------------------------
'''





