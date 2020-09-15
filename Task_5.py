# TASK FIVE: FILE HANDLING AND EXCEPTION HANDLING
'''
1. Write a program in Python to allow the error of syntax to go in
exception. HINT: use SyntaxError
'''
try:
    x = int(input("Enter a num1"))
    y = int(input("Enter a num2"))
    z = ('print (x+/y)')
    exec(z)

except SyntaxError:
    print("Please provide the correct syntax")


'''
2. Write a program in Python to allow user to open a
file by using argv module. If the entered name is incorrect
throw an exception and ask them to enter the name again.
Make sure to use read only mode.
'''
from sys import argv

pname, fname = argv
print("The name of program is: ", pname)
print("The name of file is: ", fname)

while True:
    try:

        fh = open(fname, 'r')
        content = fh.read()
        print(content)
        fh.close()
        break

    except:
        print("The name entered is wrong. Please provide correct name")

        try_again = input("Do you want to try again! Please press Yes|No: ")
        if try_again == "Yes" or try_again == "yes" or try_again == "Y" or try_again == "y":
            fname = input("Enter the correct file name:")
        elif try_again == "NO" or try_again == "no" or try_again == "N" or try_again == "n":
            break
'''
3. Write a program to handle an error if the user entered the number more than four digits it should return “Please
length is too short/long !!! Please provide only four digits”
'''
while True:
    try:
        x = int(input("Enter a number: "))
        if len(str(x)) == 4:
            print(x)
            break
        else:
            raise Exception
    except:
        if len(str(x)) < 4:
            print("Length is short! Please provide four digits\n")
        elif len(str(x)) > 4:
            print("Length is long! Please provide four digits\n")

'''
4. Create a login page backend to ask user to enter the UserEmail
and password. Make sure to ask Re-Type Password and if the password
is incorrect give chance to enter it again but it should not be more
than 3 times.
'''
u_email = input("Enter the user email: ")
password = input("Enter the password:")
count = 1
while True:

    try:
        p_word = input("Re-type the password:")
        if p_word == password:
            print("Created login page")
            break
        else:
            raise Exception
    except:
        if count == 1:
            print("You have 3 attempts left"
                  "\nPlease Enter the password again")
            count = count + 1
        elif count == 2:
            print("Incorrect password, Please try again")
            count = count + 1
            print("You have 2 attempt left")
        elif count == 3:
            print("Incorrect password, Please try again")
            count = count + 1
            print("You have 1 attempt left")
        else:
            print("3 attempts are over!")
            break

'''
5.  https://www.programiz.com/python-programming/exception-handling
Go through this link to understand Finally and
Raise concept.
''' #DONE


'''
6. Read any file using Python File handling concept and
return only the even length string from the doc.txt
file.Consider the content as:
'''

'''
Consider the content as: 
Hello I am a file 
Where you need to return the data string 
Which is of even length 
Make sure you return the content in 
The same link as it is present.
'''

file = open('data.txt', 'r')
for i in file:
    i = i.rstrip()  # removed whitespace
    if len(i) % 2 == 0:
        print(i)
    else:
        continue