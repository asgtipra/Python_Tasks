#TASK SIX: HIGHER ORDER FUNCTIONS, GENERATORS,
#           LIST COMPREHENSION AND DECORATOR

'''
1. Write a program to Python find the values which is not divisible
3 but is should be a multiple of 7. Make sure to use only higher
order function.
'''
def my_func(x):
    if x % 3 != 0 and x % 7 == 0:
        return x

y = list(filter(my_func, range(100)))
print(y)

'''
2. Write a program in Python to multiple the element of list by 
itself using traditional function and pass the function to map to 
complete the operation.
'''
def my_func(x):
    return x ** x

x = list(range(1,6))
# print(x)
y = list(map(my_func, x))
print(y)


'''
3. Write a program to Python find out the character in a string 
which is uppercase using list comprehension.
'''
word = "Hello Innovation_Python Training"
x = [i for i in word if i.isupper()]
print(list(x))

'''
4. Write a program to construct a dictionary from the two lists 
containing the names of students and their corresponding subjects. 
The dictionary should maps the students with their respective subjects. 
Let’s see how to do this using for loops and dictionary comprehension.
HINT-Use Zip function also
●	Student = ['Smit', 'Jaya', 'Rayyan']	
●	capital = ['CSE', 'Networking', 'Operating System']
'''
# 1st method Using zip function
Student = ['Smit', 'Jaya', 'Rayyan']
capital = ['CSE', 'Networking', 'Operating System']

dictionary = dict(zip(Student, capital))
print(dictionary)

# 2nd method Using Dictionary Comprehension:
dict1 = {Student[i]: capital[i] for i in range(len(Student))}
print(dict1)

# 3rd method Using Dictionary Comprehension and zip function
dict2 = {k: v for k, v in zip(Student, capital)}
print(dict2)

# 4th method Using for loop
dict4 = {}

for k in Student:
    for v in capital:
        dict4[k] = v
        capital.remove(v)
        break
print(dict4)


'''
5. Learn More about Yield, next and Generators
'''
#In progress

'''
6. Write a program in Python using generators to reverse the string. 
Input String = “Consultadd Training”
'''
x = input("Enter a string: ")
def reverse(x):
    y = x[::-1]
    for i in range(len(y)):
        yield y[i]

for i in reverse(x):
    print(i)

'''
7. Write any example on decorators.
'''
def my_decorator(func):
    def reverse(x):
        y = x[::-1]
        print(y)
        print(func(x))
    return reverse

@my_decorator
def rev_in_list(x):
    return ("Length of string is: ", len(x))

print(rev_in_list('Python Training Consultadd'))


'''
8. Learn about What is FRONT END and its Technologies and Tools
● Make sure to mention at least 5 top notch technologies of Frontend.
● Also mentioned the name of companies using those 5 technologies individually
'''
#Answer#
'''
HTML/CSS :- Coursera, Cognizant, ADP, DataDog
JavaScript :- Microsoft, PayPal, Netflix, Uber, ebay 
Angular :- Google, Microsoft, AWS, Apple, Adobe
React :- Uber, Facebook, Netflix, Udemy, Airbnb
Bootstrap :- Spotify, Udemy, Lyft, Linkedln, Intel  
'''