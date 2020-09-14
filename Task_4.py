#Task Four: FUNCTIONS

'''
1. Write a program to reverse a string.
Sample data: “1234abcd”
Expected Output: “dcba4321”
'''

def reverse():
    x = input("Enter a string: ")
    y = list(x)
    print("Reverse string is: ", x[::-1])

reverse()

''' 
2. 	Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters.
Expected Output:
No. of Upper case characters : 3
No. of Lower case Characters : 12
'''
def counts():
    x = input("Enter a String: ")
    Upper = 0
    Lower = 0
    for i in x:
        if i.isupper():
            Upper += 1
        elif i.islower():
            Lower += 1
        else:
            pass
    print("Sting: ", x)
    print("No. of Upper case characters : ", Upper)
    print("No. of Upper case characters : ", Lower)

counts()

'''
3. Create a function that takes a list and returns a new list
with unique elements of the first list.
'''
def unique(x):
    y = []

    for i in x:
        if i not in y:
            y.append(i)
    print("Unique elements in list: ", y)

x = [1,2,3,3,4,5,6,7,7,8,9,9]
unique(x)

'''
4. Write a program that accepts a hyphen-separated sequence of words
as input and prints the words in a hyphen-separated sequence after
sorting them alphabetically.
'''

def sperate_sort():
    x = input("Enter a hyphen-separated sequence of words: ")
    y = x.split('-')
    y.sort()
    print("The hyphen-separated sequence after sorting: ", '-'.join(y))

sperate_sort()

'''
5. Write a program that accepts a sequence of lines as input and
prints the lines after making all characters in the sentence
capitalized.
Sample input:
Hello world
Practice makes perfect
Expected Output:
HELLO WORLD
PRACTICE MAKES PERFECT
'''

def capi():
    x = []
    a = int(input("Enter line numbers: "))
    for i in range(a):
        y = input("Enter Something: ")
        if y:
            x.append(y.upper())
        else:
            break

    print(*x, sep = "\n")

capi()

'''
6. Define a function that can receive two integral numbers in
string form and compute their sum and print it in console.
'''

def sum_cal(a, b):
    x = int(a) + int(b)
    return x

n1 = "10"
n2 = "20"
print(sum_cal(n1, n2))

'''
7. Define a function that can accept two strings as input and print
the string with maximum length in console. If two strings have the
same length, then the function should print all strings line by line.
'''


def max_len():
    a = input("Enter 1st String: ")
    b = input("Enter 2nd String: ")

    if len(a) < len(b):
        print("Max length string is: ", b)

    elif len(a) > len(b):
        print("Max length string is: ", a)

    else:
        print("Both stings are of same length: ", a, b, sep="\n")

max_len()

'''
8. Define a function which can generate and print a tuple
where the value are square of numbers between 1 and 20.
'''

def square_val():
    a = []
    for i in range(1, 21):
        a.append(i**2)
    print(tuple(a))

square_val()

'''
9. Write a function called showNumbers that takes a parameter called
limit. It should print all the numbers between 0 and limit with a
label to identify the even and odd numbers.
Example: If the limit is 3 , it should print:
0 EVEN
1 ODD
2 EVEN
3 ODD
'''

def showNumbers():
    limit = int(input("Enter a number: "))
    for i in range(limit+1):
        if i % 2 == 0:
            print(i, "EVEN")
        else:
            print(i, "ODD")

showNumbers()

'''
10. Write a program which can filter() to make a list whose elements
are even number between 1 and 20 ( both included)
'''
x = [1,2,3,4,5,6,7,8,9,10]

y = list(filter(lambda a: a % 2 == 0, x))

print("Given list : ", x)

print("Even numbers from given list: ", y)

'''
11. Write a program which can map() and filter() to make a list whose
elements are square of even number in [1,2,3,4,5,6,7,8,9,10]
Hints: Use map() to generate a list.
       Use filter() to filter elements of a list
       Use lambda to define anonymous functions
'''

x = [1,2,3,4,5,6,7,8,9,10]

y = list(filter(lambda a: a % 2 == 0, x))

z = list(map(lambda a: a**2, y))

print("Given list : ", x)

print("Even numbers from given list: ", y)

print("Square of Even numbers in list: ", z)

'''
12. Write a function to compute 5/0 and use try/except to catch
the exceptions
'''

try:
    num = int(input("Enter a number you want to dividend: "))
    y = int(input("Enter number you want to divisor: "))
    x = num/y
    print(x)

except ZeroDivisionError:
    print("Exception handler for ZeroDivisionError")
    print("We cant divide a number by 0")

'''
13. Flatten the list [[1,2,3],[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8]
using reduce Goal : Turn [1,2,3,4,5,6,7] to 1234567
'''
from functools import reduce

a = [[1,2,3],[4,5],[6,7,8]]
print("Initial list: ", a)

flatten_list = reduce(lambda x, y: x + y, a)
print("List after flattening: ", flatten_list)

z = reduce(lambda x, y: 10*x+y, flatten_list, 0)
print("Final Goal: ", z)

''' 
14. What is the output of the following codes:
'''
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)
'''OUTPUT : 2'''
def a():
    try:
        f(x, 4)
    finally:
        print('after f')
    print('after f?')
a()
'''OUTPUT: after f'''