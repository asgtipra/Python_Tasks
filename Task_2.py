#TASK TWO: OPERATORS AND DECISION MAKING STATEMENT
'''
1.	Write a program in Python to perform the following operation:
●	If a number is divisible by 3 it should print “Consultadd” as a string
●	If a number is divisible by 5 it should print “c” as a string
●	If a number is divisible by both 3 and 5 it should print “Consultadd Python Training” as a string.
'''
x = int(input("Enter a number: "))
if x % 3 == 0 and x % 5 != 0:
    print("Counsultadd")

elif x % 3 != 0 and x % 5 == 0:
    print("c")

elif x % 3 == 0 and x % 5 == 0:
    print("Counsultadd Python training")

else:
    print("Entered number is not divisible by 3 and 5")


'''
2. 	Write a program in Python to perform the following operator based task:
●	Ask user to choose the following option first:
○	If User Enter 1 - Addition 
○	If User Enter 2 - Subtraction
○	If User Enter 3 - Division
○	If USer Enter 4 - Multiplication
○	If User Enter 5 - Average
●	Ask user to enter the 2 numbers in a variable for first and second for the first 4 options mentioned above.
●	Ask user to enter two more numbers as first and second2 for calculating the average as soon as user choose an option 5.
●	At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
●	NOTE: At a time user can perform one action at a time.
'''


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


def average(numbers):
    avg = sum(numbers) / len(numbers)
    return avg


def negative(a):
    if a < 0:
        print("NEGATIVE")

print("Please select operation -\n"
      "1. Addition\n"
      "2. Subtraction\n"
      "3. Multiplication\n"
      "4. Division\n"
      "5. Average")

select = int(input("Enter option for calculation: "))

if 0 < select < 5:
    number1 = int(input("Enter 1st number: "))
    number2 = int(input("Enter 2nd number: "))
    if select == 1:
        a = addition(number1, number2)
        print(number1, "+", number2, "=", a)
        negative(a)

    elif select == 2:
        a = subtraction(number1, number2)
        print(number1, "-", number2, "=", a)
        negative(a)

    elif select == 3:
        a = multiplication(number1, number2)
        print(number1, "*", number2, "=", a)
        negative(a)

    elif select == 4:
        a = division(number1, number2)
        print(number1, "/", number2, "=", a)
        negative(a)

    elif select == 5:
        number3 = int(input("Enter 3rd number: "))
        number4 = int(input("Enter 4th number: "))
        a = [number1, number2, number3, number4]
        print("Average of given numbers: ", average(a))
        negative(a)
else:
    print("Invalid Selection")
    print("Please try again")

'''
3. Write a program in Python to implement the given flowchart:
'''

a = 10
b = 20
c = 30

avg = (a + b + c) / 3
print("avg = ", avg)

if avg > a and avg > b and avg > c:
    print("avg is higher than a, b, c")

elif avg > a and avg > b:
    print("avg is higher than a, b")

elif avg > a and avg > c:
    print("avg is higher than a, c")

elif avg > b and avg > c:
    print("avg is higher than b, c")

elif avg > a:
    print("avg is higher than a")

elif avg > b:
    print("avg is higher than b")

elif avg > c:
    print("avg is higher than c")

'''
4. 	Write a program in Python to break and continue if the following cases occurs:
●	If user enters a negative number just break the loop and print “It’s Over”
●	If user enters a positive number just continue in the loop and print “Good Going”
'''
while True:
    n = int(input("Enter number: "))
    if n > 0:
        print("Good Going")
        continue
    elif n < 0:
        break
print("Its over")

'''
5.   Write a program in Python which will find all such numbers 
which are divisible by 7 but are not a multiple of 5, between 2000 and 3200.
'''
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i)

''' 
6. What is the output of the following code examples?
●	   x=123 
   	   for i in x:
   		print(i)
OUTPUT ERROR:   		
TypeError: 'int' object is not iterable
●	i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print(“error”)
OUTPUT:
0
1
2
●	count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        Break
OUTPUT:
0
1
2
3
4
'''
'''
7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.
       Expected output: 0 1 2 4 5
Note: Use ‘continue’ statement
'''
for i in range(0, 7):
    if i != 3 and i != 6:
        print(i, end = ' ')
        continue

''' 
8.  Write a program that accepts a string as an input from user and calculate the number of digits and letters.
     Expected output: consul12
     Letters 6
     Digits 2
'''
x = input("Enter a String: ")
a = b = c = 0
for i in range(len(x)):
    if x[i].isdigit():
        a += 1
    elif x[i].isalpha():
        b += 1
    elif x[i].isspace():
        c += 1
print("digits count in string: ", a)
print("Letters count in string: ", b)
print("Spaces count in string: ", c)

'''
9. Read the two parts of the question below: 
●	 Write a program such that it asks users to 
“guess the lucky number”. 
If the correct number is guessed the program stops,
otherwise it continues forever. 
●	Modify the program so that it asks users whether 
they want to guess again each time. Use two variables, 
‘number’ for the number and ‘answer’ for the answer to
the question whether they want to continue guessing. 
The program stops if the user guesses the correct number
or answers “no”. ( The program continues as long as a user
has not answered “no” and has not guessed the correct number)
'''

print("------------GUESS THE LUCKY NUMBER-------------")

while True:
    n = int(input("Please enter number: "))
    if n != 36:
        print("Wrong number")
        a = input("Do you want to guess again select Y/N: ")
        if a == 'Y':
            continue
        elif a == 'N':
            break
        else:
            print("wrong selection"
                  "select again", input())
    else:
        print("Right Answer")
        break

''' 
10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter, such as
           		counter=1
		While counter <= 5:
			print(“Type in the”, counter, “number”
			counter=counter+1
The program asks for five guesses (no matter whether the correct number was guessed or not). If the correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”. After the fifth guess it stops and prints “Game over!”.
'''
print("------------GUESS THE LUCKY NUMBER-------------")
counter = 1
while counter <= 5:
    print("attempt", counter)
    counter += 1
    n = int(input("Please enter number: "))

    if counter == 6:
        print("Game Over")
    elif n != 36 and counter < 6:
        print("Try again!")
    elif n == 36:
        print("Good Guess!")

''' 
11. In the previous question, insert “break” after the 
“Good guess!” print statement. “break” will terminate 
the while loop so that users do not have to continue 
guessing after they found the number. 
If the user does not guess the number at all, 
print “Sorry but that was not very successful”.
'''

print("------------GUESS THE LUCKY NUMBER-------------")
counter = 1
while counter <= 5:
    print("attempt", counter)
    counter += 1
    n = int(input("Please enter number: "))

    if counter == 6:
        print("Sorry but that was not very successful")
    elif n != 36 and counter < 6:
        print("Try again!")
    elif n == 36:
        print("Good Guess!")
        break