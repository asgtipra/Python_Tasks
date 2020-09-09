#TASK ONE: NUMBERS AND VARIABLES
'''
1.Create three variables in a single line and assign different values to them and
make sure their data types are invited differently.
Like one is int, another one is float and last one is string")
a = 1; b = 2.01; c = 'string'
'''

a, b, c = 1, 2.01, 'string'

print(a,"=", type(a))
print(b,"=", type(b))
print(c,"=", type(c))
'''
2.Create a variable of value type complex and 
swap it with another variable whose value is an integer.
'''
print("---Before Swapping---")
d, e = 10+3j, 10
print(d,"= Type of d is", type(d))
print(e,"= Type of e is", type(e))
d, e = e, d
print("---After Swapping---")
print(d,"= Type of d is", type(d))
print(e,"= Type of e is", type(e))

'''
3. Swap two numbers using third variable as result name and do the same task without using any third variable.
'''

print("i) ")
f, g = 15, 20
print("        ---Before Swapping---")
print(f, g)
result = f
f = g
g = result
print("        ---After Swapping---          ")
print(f, g)
print("--------------------------------------")
print("ii) ")
f, g = 15, 20
print("        ---Before Swapping---         ")
print(f, g)
f, g = g, f
print("        ---After Swapping---          ")
print(f, g)

'''
4. Write a program to print the value given by the user by using both Python 2.x and Python 3.x Version.")
'''
#Python 2
'''txt = raw_input("Type something to test: ")
print "Is this what you just said", txt
'''
#Python 3
newvar = input("Enter any number")
print("Is it ur number", newvar)

'''
5. 	Write a program to complete the task given below:
●	Ask user to enter any 2 numbers in between 1-10 and add both of them to another variable call z.
●	Use z for adding 30 into it and print the final result by using variable result.
'''
x = int(input('Enter 1st Number between 1 to 10: '))
y = int(input('Enter 2nd Number between 1 to 10: '))
z = x + y
print("Addition of two number is : ", z)
result = z + 30
print("Result of after adding addition into 30 is: ", result)


'''
6. 	Write a program to check the data type of the entered values. 
HINT: Printed output should say - 
The input value data type is : int/float/string/etc
'''
a = (input('Enter any number: '))
b = int(input('Enter any number: '))
c = float(input('Enter any number: '))

print("The input value of data type is: ", type(a))
print("The input value of data type is: ", type(b))
print("The input value of data type is: ", type(c))

'''
7. 	Create Variable using CamelCase, LadderCase and UPPERCASE. (Refer:   https://capitalizemytitle.com/camel-case/)
'''

'''
8. 	If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again. Will it change the value. If Yes then Why?
'''
a = 10
print(type(a))
a = 'string'
print(type(a))

'''
Yes its data type will change
When we inialize one value to a variable whos data type is suppose integer and 
then when we initialize same variable with different value who's data type is string
Python compiler will implicitly determine type of the new value
'''
