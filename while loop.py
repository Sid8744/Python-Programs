'''
=====================================
While loop
=====================================
num = 10
while num == 10:
    print('gm')
    num = 11
-------------------------------------

num = 1
while num < 6 :
    print('sid')
    num += 1
-------------------------------------

#print numbers from 1 to ten
num = 1
while num <= 10:
    print(num, end=' ')
    num = num + 1
-------------------------------------

#sum of all number from 1 to 100
num = 100
sum = 0
while num > 0:
    sum = sum + num
    num = num - 1
print('sum of all number from 1 to 100 :',sum)
-------------------------------------

#find factorial of number
num = 5
factorial = 1
while num > 0:
    factorial = num * factorial
    num = num - 1
print('factorial of number: ',factorial)
-------------------------------------

num = int(input('Enter number: '))
fact = 1
i = 1
while i<=num:
    fact = fact * i
    i = i + 1
print('Factorial: ',fact)
-------------------------------------

#print even number between 1 and 50
max = 50
num = 1
while num <= max:
    if (num % 2 == 0):
        print(num, end=' ')
    num = num + 1
-------------------------------------

num = 2
while num<=50:
    print(num, end=' ')
    num = num + 2
-------------------------------------

#iterate over string and print each character
num = 1
s = 'python'
while num == 1:
    print(s)
    num = 2
-------------------------------------

s = 'python'
i = 0
while i < len(s):
    print(s[i])
    i = i + 1
-------------------------------------

#iterate over list of tuple and print each element
t = (1,2,'a','b','c',3)
i = 0
while i < len(t):
    print(t[i])
    i = i + 1
-------------------------------------

#find largest element in list using while loop
l = [11,2,3,4,5,10,6,777,88,9]
i = 0
while i < len(l):
    if l[i] == max(l):
        print(l[i])
    i = i+1
-------------------------------------

#check if all element in list are even
l = [112,2,3,4,5,10,6,2694,88,9]
print('Given list: ',str(l))
i = 0
print('Even number in list: ')
while i < len(l):
    if l[i]%2 ==0:
        print(l[i],end=' ')
    i = i+1
-------------------------------------

#find common number between two list
l1 = [1,2,3,4,5,6]
l2 = [5,6,7,8,9,10]



------------------------------------

#sum of digit of number
n = 78912
sum = 0
while n > 0:
    dig = n%10
    sum = sum + dig
    n = n//10
print('sum of digit of number: ', sum)
'''





