'''''
===============================================
String
==============================================
#count no. of character in a string
s = 'India is my country'
print('Number of characters:', len(s))
___________________________
#reverse a string
s = 'India is my country'
print('Reverse of string: ',s[::-1] )
_________________________
#Palindrome or not
s = 'racecar'
if s == s[::-1]:
    print('String is Palindrome')
else:
    print('String is not Palindrome')
_______________________

x = 'racecar'
w = ''
for i in x:
    w = i + w
if x==w:
    print('yes')
else:
    print('no')
_______________________

#remove all vowels from string
s = 'India is my country'
vowels = ['a','e','i','o','u','A','E','I','O','U']
result = ''
for i in range(len(s)):
    if s[i] not in vowels:
        result = result + s[i]
print('string after removing vowels: ', result)
_________________________

s = 'India is my country'
vowels = ['a','e','i','o','u','A','E','I','O','U']
result = ''
for char in s:
    if char not in vowels:
        result = result + char
print('string after removing vowels: ', result)
___________________

s = 'India is my country'
result = s
vowels = ['a','e','i','o','u','A','E','I','O','U']
for x in s:
    if x in vowels:
        result = result.replace(x,'')
print('string after removing vowels: ', result)
_____________________

#find first non repeating character in string
s = 'tit for tat'
for i in s:
    if s.count(i) == 1:
        print('first non-repeating character is: ', i)
        break
______________________________

#capitalize first letter of string
s = 'tit for tat'
print('Original string: ', s)
print('String after capitalizing first letter: ',s.title())
____________________________


#check if two strings are anagrams
s1 = 'silent'
s2 = 'listen'
print('Given strings to check if they are anagram :', s1 , s2)
if (sorted(s1) == sorted(s2)):
    print('Result: strings are anagrams')
else:
    print('Result: strings are not anagrams')
__________________________________

def check(s1,s2):
    if (sorted(s1) == sorted(s2)):
        print('Result: strings are anagrams')
    else:
        print('Result: strings are not anagrams')
s1 = 'silent'
s2 = 'listen'
check(s1,s2)

s1 = 'dad'
s2 = 'add'
check(s1,s2)
_____________________________________________

#maximum frequency of character in string
s = 'The world has gone in oblivion'
print('Original string is: ', s)
freq = {}
for i in s:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
res = max(freq, key= freq.get)
print('maximum frequency character of string is: ', str(res))
________________________________________________________

#check if string is valid email address
#find length of longest substring without repeating characters
___________________________________________________

=================================================
List=
=================================================

#find sum of all elements in list
l = [1,2,3,5,7,99,111]
print('sum of all elements: ', sum(l))
____________________________________

total = 0
l = [1,2,3,5,7,99,111]
for ele in range(0, len(l)):
    total = total + l[ele]

print('sum of all elements: ', total)
____________________________________

total = 0
ele = 0
l = [1,2,3,5,7,99,111,222]
while ele < len(l):
    total = total + l[ele]
    ele += 1
print('sum of all elements: ', total)
______________________________________

#find max and min element in list
l = [0,1,2,3,5,7,99,111,222]
print('given list:', l)
print('maximum element is: ', max(l))
print('minimum element is: ', min(l))
______________________________________

l = [1,2,3,5,7,0,99,111,222]
min = None
for ele in l:
    if min is None or ele< min:
        min = ele
print('minimum element is: ', min)
print('index of min element is: ', l.index(min))
______________________________________

l = [1,2,3,5,7,0,99,111,222]
max = None
for ele in l:
    if max is None or ele > max:
        max = ele
print('maximum element is: ', max)
print('index of max element is: ', l.index(max))
______________________________________

def min_max(l):
    if not l:
        raise ValueError('please provide a non empty list')
    minimum = maximum = l[0]
    for num in l[1:]:
        if num < minimum:
            minimum = num
        elif num > maximum:
            maximum = num

    return [minimum, maximum]

print(min_max([1,102,0,88,99]))
______________________________________

l = [1,2,3,5,7,0,99,111,222]
num1 = sorted(l)[-1]
print('largest number is: ', num1)
print('index of largest number is: ', l.index(num1))

num2 = sorted(l)[0]
print('largest number is: ', num2)
print('index of largest number is: ', l.index(num2))
______________________________________

def min_max(l):
    num = sorted(l)
    minimum = num[0]
    maximum = num[-1]
    return[minimum, maximum]
print(min_max([0,22,88,-1,999,66666]))
______________________________________

#remove duplicates from list
l = [1,2,33,66,1,8,66]
print('given list: ',l)
l1 = list(set(l))
print('new list after removing duplicates: ', l1)
______________________________________

l = [1,2,33,66,1,8,66]
print('given list: ',l)
print('list without duplicates:', [*set(l)])
______________________________________

l = [1,2,8,33,66,2,1,8,66]
print('given list: ',l)
res = []
for x in l:
    if x not in res:
        res.append(x)
print('list without duplicates: ', res)
______________________________________

#check if list is sorted in ascending order
l = [1,2,3,4,5,8,6,7]
print('given list: ',l)
l1 = sorted(l)
if l == l1:
    print('given list is sorted')
else:
    print('given list is not sorted')
______________________________________

l = [1,2,3,4,5,6,7]
l1 = l[:]
l1.sort()
if l == l1:
    print('given list is sorted')
else:
    print('given list is not sorted')
______________________________________

#find second largest element of list
l = [1,8,33,66,2,1,8,66]
l1 = list(set(l))
l1.sort()
print('Second largest numberis: ',l1[-2])
______________________________________

l = [1,8,33,44,66,2,1,8,66]
l1 = list(set(l))
l1.remove(max(l1))
print('Second largest number is: ', max(l1))
______________________________________

#list of string in alphabetical order
l = ['say', 'hello', 'to', 'my', 'little', 'friend']
l.sort()
print(l)
______________________________________


l = ['say', 'hello','a', 'to', 'my', 'little', 'friend']
for ele in sorted(l):
    print(ele, end=' ')
______________________________________

l = ['say', 'hello','a', 'to', 'my', 'little', 'friend']
l.sort(key = len)
print(l)
______________________________________

l = ['1','8','99','66','47']
l.sort(key=int)
print(l)
______________________________________

#find common element between 2 lists
a = [1,2,5,8,9,7,6]
b = [2,5,77,8,98,5]
s1 = set(a)
s2 = set(b)
print('common elements are', s1.intersection(s2))
______________________________________

def common(a,b):
    s1 = set(a)
    s2 = set(b)
    if len(s1.intersection(s2)) > 0:
        return 'common elements are: ', s1.intersection(s2)
    else:
        return 'no common elements present'

a = [1,2,5,8,9,7,6]
b = [2,5,77,8,98,5]
print(common(a,b))

a = [1,9,7,6]
b = [2,5,77,8,98,5]
print(common(a,b))
______________________________________

def common(a,b):
    s1 = set(a)
    s2 = set(b)
    if (s1 & s2):
        return 'common elements are: ', s1 & s2
    else:
        return 'no common elements present'

a = [1,2,5,8,9,7,6]
b = [2,5,77,8,98,5]
print(common(a,b))

a = [1,9,7,6]
b = [2,5,77,8,98,5]
print(common(a,b))
______________________________________


#remove nth occurence of element from list
def removenthword(list,word,n):
    list1 = []
    count = 0
    for i in list:
        if i == word:
            count += 1
            if count != n:
                list1.append(i)
        else:
            list1.append(i)
    lst = list1
    if count == 0:
        print('no word found')
    else:
        print('updated list: ', lst)


list = ['you','are','you','why','are','you']
word = 'are'
n = 2
removenthword(list,word,n)
______________________________________

#find difference between two list:
a = [1,2,5,8,9,7,6]
b = [2,5,77,8,98,5]

s1 = set(a)
s2 = set(b)

print('differnce between two lists is: ', list((s1.difference(s2))))
______________________________________

a = [1,2,5,8,9,7,100,6]
b = [2,5,77,8,98,5]
list = []
for ele in a:
    if ele not in b:
        list.append(ele)
print('differnce between two lists is: ', list)
______________________________________

#remove element in list divisible by 3:
c = [1,2,3,4,5,6,7,8,9,9,9,10,11,12,13,14,15,16,17,18,19,20,21]
for ele in c:
    if ele % 3 != 0:
        continue
    else:
        c.remove(ele)
print('list with element not divisible by 3: ', c)

______________________________________
'''''