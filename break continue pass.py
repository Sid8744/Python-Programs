'''
===========================================
Break Statement
===========================================
for i in range(11):
    if i==6:
       break
    else:
        print(i,end=' ')
------------------------------------------------

for i in range(11):
    if i == 6:
        break
    print(i, end=' ')
------------------------------------------------

k = [12,55,48,0,6,9,77]
for num in k:
    if num == 6:
        break
    print(num, end=' ')
------------------------------------------------

k = [ 0,12,55,48,0,6,9,77]
for num in k:
    if num == 0:
        continue
    print(num, end=' ')
------------------------------------------------

#find first occurence of number in list
l = [1,2,4,5,4,4,6,3,7,8]
print('Given list: ',str(l))
num = int(input('Enter number: '))
for i in range(len(l)):
    if l[i] == num:
        print('First occurence of number at index: ',l.index(num))
        break
------------------------------------------------

#search for specific element in list
l = [1,2,4,5,4,4,6,3,7,8]
print('Given list: ',str(l))
num = int(input('Enter number: '))
i = 0
while i < len(l):
    if l[i] == num:
        print('Element exists in list')
        break
    i = i + 1
else:
    print('Element does not exist in list')
------------------------------------------------

#find prime number between 1 and 100
print(('Prime numbers between 1 to 100: '))
for num in range(1,101):
    for i in range(2,num):
        if num%i ==0:
            break
    else:
        print(num, end=' ')
------------------------------------------------

#check if number present in list
l = [1,2,3,4,5,6,7,8,9]
print('Given list: ',str(l))
num = int(input('Enter number: '))
i = 0
while i < len(l):
    if l[i] == num:
        print('Number present in list')
        break
    i = i + 1
else:
    print('Number absent in list')
------------------------------------------------

#print first negative number in list
l = [1,-2,-3,-4,5,6,7,8,9]
i = 0
while i < len(l):
    if l[i] < 0:
        print('First negative number: ',l[i])
        break
    i = i + 1
------------------------------------------------

#print element until condition is met


------------------------------------------------

#search for specific character in string using while loop
s = 'python'
print('given string: ',s)
chr = input('enter character: ')
i = 0
while i < len(s):
    if chr in s:
        print('character is in string')
        break
    else:
        print('character absent')
        break
    i = i + 1
------------------------------------------------

#find first occurence of vowel in string using for loop
s = 'Pytuh'
vowel = ['a','e','i','o','u','A','E','I','O','U']
for i in s:
    if i in vowel:
        print('first occurence of vowel: ',s.index(i))
        break
else:
    print('Vowel absent in string')
------------------------------------------------

#find index of first occurence of substring in string using while loop
s = input('Enter string: ')
p = input('Enter substring: ')
i = 0
while i < len(s):
    if s[i] == p[0]:
        print('first occurence of substring: ',s.index(p[0]))
        break
    i = i + 1
===========================================
Continue Statement
===========================================

#print all even no. between 1 and 20 except 10 using for loop
for i in range(1,21):
    if i%2 == 0:
        if i==10:
            continue
        print(i, end=' ')
------------------------------------------------

#print element of a list skipping negative no. using while loop
l = [-1,2,-3,4,-7,8,-66,44]
print('Original list: ')
i = 0
while i < len(l):
    if l[i] < 0:
        l.remove(l[i])
        continue
    i = i + 1
print('New list without negative no.s: ',l)
------------------------------------------------

#print first 10 multiples of 3 except for 9 using for loop
for num in range(0,31,3):
    if num == 9:
        continue
    print(num, end = ' ')
------------------------------------------------

#iterate over string and print only consonant using for loop
s = input('Enter string: ')
vowels = 'aeiouAEIOU'
for i in s:
    if i not in vowels:
        print(i, end = '')
------------------------------------------------

s = 'apple'
vowels = 'aeiouAEIOU'
for i in s:
    if i in vowels:
        continue
    print(i, end = '')
---------------------------------------------

#print element of list skipping even no. using while loop
l = [1,2,31,15,19,4,5,6,77,88,98,21]
print('Original list: ',l)
i = 0
while i < len(l):
    if l[i] % 2 == 0:
        l.remove(l[i])
        continue
    i = i + 1
print('List without even numbers: ',l, end=' ')
---------------------------------------------

#find sum of all no.s between 1 and 100 excluding multiples of 5 using for loop
sum = 0
for i in range(1,101):
    if i%5 == 0:
        continue
    sum = sum + i
print('sum of all no.s between 1 and 100 excluding multiples of 5: ',sum)
---------------------------------------------

#print uppercase letter in string using while loop
s = 'Python Is GooD'
print('Given string: ',s)
upper = ''
for chr in s:
    if chr.isupper():
        upper = upper + chr
print('String with only uppercase letter: ',upper)
---------------------------------------------
Not solved
s = 'Python Is GooD'
i = 0
while i < len(s):
    if s[i].islower():
        continue
    else:
        print(s)
    i = i + 1
---------------------------------------------

#print element of list skipping element divisible by 3 using for loop
l = [1,2,4,5,6,3,8,9,66,33,42,78,100]
print('Original list: ',l)
for i in l:
    if i%3 == 0:
        continue
    else:
        print(i, end=' ')
---------------------------------------------

#iterate over list of tuple and print only tuple with specific condition using while loop
---------------------------------------------


#print no. between 1 and 50 excluding multiples of 7 using for loop
for i in range(1,51):
    if i%7 == 0:
        continue
    else:
        print(i,end=' ')
'''








