'''
====================================
For loop
====================================
l = [1,2,3,4,5]
for ele in l:
    print(ele)
-------------------------------------
for val in range(1,101):
    if val % 10 == 0:
        print(val, 'is divisible by 10')
-------------------------------------
s = {10,20,'a','b',50}
for ele in s:
    print(ele)
-------------------------------------
s = {10,20,'a','b',50}
for ele in s:
    if str(ele).isalpha():
        print(ele, 'is alphabet')
-------------------------------------
s = {1,10,5,11,80,90,66}
for ele in s:
    if ele % 2 == 0:
        print(ele, 'is even number')
-------------------------------------
s = {1,10,5,11,80,90,66}
for ele in s:
        print(ele*5, 'is five times of', ele, 'and', ele/2, 'is half of', ele)
-------------------------------------
z = [35, 50, 70, 60, 80]
print(sum(z), 'are total marks obtained')
-------------------------------------
d = {1:'a', 2:'b', 3:'c'}
for x in d:
    print(x)
-------------------------------------
d = {1:'a', 2:'b', 3:'c'}
for x in d:
    print(x)
for v in d.values():
    print(v)
-------------------------------------
d = {1:'a', 2:'b', 3:'c'}
for x in d.items():
    print(x)
-------------------------------------
s = 'amol is in pune you contact him: 9877665544'
for num in s:
    if str(num).isdigit():
        print(num, end = '')
-------------------------------------
z = [11,12,13,21,22,44,66]
for val in z:
    if val%11 == 0 and val%2 == 0:
        print(val, 'is divisible by 2 and 11')
-------------------------------------
z = [11, 12, 13, 21, 22, 44, 66]
for val in z:
    if val % 11 == 0 or val % 2 == 0:
        print(val, 'is divisible by 2 or 11')
-------------------------------------

d = 'seema got 89 77 75 90 65 marks in five subjects'
x = (d.split()[2:7])
print('marks obtained: ', x)
y = [eval(i) for i in x]
print('total marks:', sum(y))
z = sum(y)/5
print('percentage: ', z)
-------------------------------------

#print no. 1 to 10
for i in range(1,11):
    print(i, end=' ')
-------------------------------------

#calculate sum of all no. in list
l = [1,2,4,5]
print('original list: ',l)
sum = 0
for num in l:
    sum = num + sum
print('sum of all numbers in list: ',sum)
-------------------------------------

l = [1,2,4,5]
total = 0
for i in range(len(l)):
    total += l[i]
print('sum of all numbers in list: ',total)
-------------------------------------

#find fraction of number
l = [1,2,4,5]
for i in l:
    res = 1/i
    print('factorial of numbers: ',res)
-------------------------------------

#find factorial of number
num = int(input('Enter number: '))
factorial = 1
if num < 0:
    print('no factorial for negative numbers')
elif num == 0:
    print('factorial of zero is 1')
else:
    for i in range(1,num+1):
        factorial = i * factorial
    print('facorial for', num, ':', factorial)
-------------------------------------

def factorial(x):
    res = 1
    for i in range(1,x+1):
        res = i*res
    print(res)
factorial(10)
-------------------------------------

from functools import reduce
def factorial(x):
    res = reduce(lambda x,y: x*y, range(1,x+1))
    print(res)
factorial(10)
-------------------------------------

#print even no. between 1 to 50
for i in range(1,51):
    if i%2 == 0:
        print(i, end=' ')
-------------------------------------

even = list(filter(lambda x: x%2==0, range(1,51)))
print(even)
-------------------------------------

#iterate over string and print each character
s = 'python'
for i in s:
    print(i, end=' ')
-------------------------------------

s = 'python'
for i in range(len(s)):
    print(s[i], end=' ')
-------------------------------------

#find largest element in list
l = [2,3,4,11,5,6,8]
print('Given list: ',str(l))
max = l[0]
for i in l:
    if i > max:
        max = i
print('Largest number: ',max)
-------------------------------------

#iterate over list of tuple
name = [('a',1,88),('b',2,56),('c',3,77)]
for x in name:
    for y in x:
        print(y)
-------------------------------------

#check if all element in list are even
l = [2,6,8]
print('Given list: ',str(l))
res = True
for i in l:
    if i%2!=0:
        res = False
print('All element in list are even: ',res)
-------------------------------------

l = [2,6,11,8]
print('Given list: ',str(l))
res = True
for i in l:
    if i%2:
        res = False
print('All element in list are even: ',res)
-------------------------------------

#find common element between two list
l1 = [1,2,3,4]
l2 = [3,4,5,6]
for i in l1:
    if i in l2:
        print(i)
-------------------------------------

#sum of digit of numbers
l = 7892
sum = 0
for i in str(l):
    sum = sum + int(i)
print('sum of number in digit', l,':',sum)
-------------------------------------
'''
