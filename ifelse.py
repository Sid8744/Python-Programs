'''
========================================================
If Else loop
========================================================
num = 5
if num>10:
    print('number is greater than 10')

color = input('color:  ')
if color == 'red':
    print('color is red')
else:
    print('color is not red')
-----------------------------------------------------
num = int(input('enter number: '))
if num > 100:
    print('number is greater than 100')
elif num ==100:
    print('number is equal to 100')
else:
    print('number is smaller than 100')
-----------------------------------------------------
speed = int(input('speed of bike: '))
if speed <= 10:
    print('bike is at first gear')
elif speed < 20:
    print('shift to second gear')
elif speed < 30:
    print('shift to third gear')
elif speed < 40:
    print('shift to fourth gear')
else:
    print('shift to fifth gear')
-----------------------------------------------------
button = int(input('press button for beverage: '))
if button == 1:
    print('pour hot water')
elif button == 2:
    print('pour tea')
elif button == 3:
    print('pour coffee')
-----------------------------------------------------
ratio = float(input('l/b ratio: '))
if ratio >= 2:
    print('slab is one way slab')
else:
    print('slab is two way slab')
-----------------------------------------------------
car = input('enter your car type: ')
if car == 'automatic':
    gear = input('enter gear you are on: ')
    if gear == 'P':
        print('car is parked')
    elif gear == 'D':
        print('car is in driving mode')
    elif gear == 'R':
        print('car is in reverse mode')
else:
    print('car is not having automatic transmission')
-----------------------------------------------------

citizen = input('enter your citizenship: ')
if citizen == 'indian':
    age = int(input('enter your age: '))
    if age >= 18:
        print('You can vote..')
    else:
        print('sorry you are not eligible: age<18')
else:
    print('You must be an Indian citizen')
-----------------------------------------------------
element = input('enter type of rcc structural element: ')
if element == 'footing':
    print('minimum cover required is 50mm')
elif element == 'column':
    print('minimum cover required is 40mm')
elif element == 'beam':
    print('minimum cover required is 25mm')
elif element == 'slab':
    print('minimum cover required is 20mm')
else:
    print('incorrect entry')
----------------------------------------------------

#check if no. is positive,negative or zero
num = float(input('Enter number: '))
if num < 0:
    print('number is negative')
elif num > 0:
    print('number is positive')
else:
    print('number is zero')
----------------------------------------------------

#check if no. is even or odd
num = int(input('Enter number: '))
if num%2 ==0:
    print('number is even')
else:
    print('number is odd')
----------------------------------------------------

#check if year is leap year or not
year = int(input('Enter year: '))
if year % 4 == 0 and year % 100 != 0:
    print('year is leap year')
else:
    print('year is not leap year')
----------------------------------------------------

#find max of three no.s
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))
if num1>num2 and num1>num3:
    largest = num1
elif num2>num1 and num2>num3:
    largest = num2
else:
    largest = num3
print('Largest of three number: ', largest)
----------------------------------------------------

#check if no. is prime
num = int(input('Enter number: '))
if num>1:
    for i in range(2,int((num/2)+1)):
        if num%i==0:
            print('number is not prime')
            break
        else:
            print('number is prime')
else:
    print('number is not prime')
----------------------------------------------------

num = int(input('Enter number: '))
for i in range(2,num-1):
    if num%i ==0:
        print('number is not prime')
        break
    else:
        print('number is prime')
        break
----------------------------------------------------

#check if no. id divisible by both 3 and 5
num = int(input('Enter number: '))
if num%3==0 and num%5==0:
    print('Number is divisible by 3 & 5')
else:
    print('not divisible by 3 & 5')
----------------------------------------------------

#check if character is vowel or consonant
x = input('Enter character: ')
if (x=='a' or x=='e' or x=='i' or x=='o' or x=='u'):
    print('Character is vowel')
else:
    print('Character is consonant')
----------------------------------------------------

def vowel(x):
    if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'):
        print('Character is vowel')
    else:
        print('Character is consonant')
vowel('i')
----------------------------------------------------

#check if given string is palindrome
str = 'noon'
if str == str[::-1]:
    print('given string is palindrome')
else:
    print('not a palindrome')
----------------------------------------------------

str = 'noone'
str1 = ''
for i in str:
    str1 = i + str1
if str == str1:
    print('given string is palindrome')
else:
    print('not a palindrome')
----------------------------------------------------

#largest among  3 no.s using nested if else
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))
if num1>num2:
    if num1>num3:
        largest = num1
    else:
        largest = num3
else:
    if num2>num3:
        largest = num2
    else:
        largest = num3
print('largest number is: ',largest)
----------------------------------------------------

#check if triangle is eqyilateral, isoceles or scalene
#based on its side length
x = int(input('length of first side: '))
y = int(input('length of second side: '))
z = int(input('length of third side: '))
if x==y==z:
    print('equilateral triangle')
elif x==y or x==z or y==z:
    print('isoceles triangle')
else:
    print('scalene triangle')
----------------------------------------------------

def triangle(x,y,z):
    if x == y == z:
        print('equilateral triangle')
    elif x == y or x == z or y == z:
        print('isoceles triangle')
    else:
        print('scalene triangle')
x=1
y=1
z=1
triangle(x,y,z)
----------------------------------------------------
'''











