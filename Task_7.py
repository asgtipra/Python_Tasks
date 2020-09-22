#TASK SEVEN: CLASSES AND ONJECTS
'''
1. Write a program that calculates and prints the value according
to the given formula:
Q = Square root of [(2*C*D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program
in a comma-separated sequence.
'''
import math
def sqrtof(C = 50, H = 30):
    val = []
    D = [x for x in input("Enter number seperated by commas: ").split(',')]
    for i in D:
        Q = math.sqrt(2*C*int(i)/H)
        val.append(round(Q, 2))
    print(val)

sqrtof()

'''
2. Define a class named Shape and its subclass Square.
The Square class has an init function which takes a length
as argument. Both classes have an area function which can
print the area of the shape where Shape’s area is 0 by default.
'''
class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length*self.length

S = Square(5)
print(S.area())


'''
3. Create a class to find the three elements that sum to zero from
a set of n real numbers.
Input array: [-25,-10,-7,-3,2,4,8,10]
Output: [[-10,2,8],[-7,-3,10]]
'''

class Solution(object):
    def threesum(self, nums):
        res = []
        nums.sort()
        length = len(nums)

        for i in range(length-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = length-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if not total:
                    res.append([nums[i], nums[l], nums[r]])
                    while nums[l] == nums[l + 1]:
                        l += 1
                    while nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1
                elif total < 0:
                    l = l + 1
                else:
                    r = r - 1
        return res

nums = [-25,-10,-7,-3,2,4,8,10]
s = Solution().threesum(nums)
print(s)


'''
4. What is the output of the following code? Explain your answer
as well.
'''
class Test:
    def __init__(self):
        self.x = 0
class Derived_Test(Test):
    def __init__(self):
        self.y = 1
def main():
    b = Derived_Test()
    print(b.x,b.y)
main()

'''
Answer: It will give us an Error because class Derived_Test inherits 
class Test variable x is not inherited we have to mention the Test.__init__(self) 
in the Derived_Test class.
'''
# Output:
# 0 1
# Reason: when main() function is called, object b of Derived_Test
# class is created which also inherits the properties of Test class.

class A:
    def __init__(self, x= 1):
        self.x = x
class der(A):
    def __init__(self,y = 2):
        super().__init__()
        self.y = y
def main():
    obj = der()
    print(obj.x, obj.y)
main()

''' 
Answer : 1 2
In this code invoking method is properly implemented i.e. super().__init__()
'''

class A:
    def __init__(self,x):
        self.x = x
    def count(self,x):
        self.x = self.x+1
class B(A):
    def __init__(self, y=0):
        A.__init__(self, 3)
        self.y = y
    def count(self):
        self.y += 1
def main():
    obj = B()
    obj.count()

    print(obj.x, obj.y)
main()

'''
Answer: 3 1
invoking method is properly implemented as we are 
class B inherits properties of class A
'''

class A:
    def __init__(self):
        self.multiply(15)
        print(self.i)

    def multiply(self, i):
        self.i = 4 * i;
class B(A):
    def __init__(self):
        super().__init__()

    def multiply(self, i):
        self.i = 2 * i;
obj = B()

''' 
Answer: 30 
The Class B overrides parent class A
'''

'''
5. Create a Time class and initialize it with hours and minutes.
Make a method addTime which should take two time object and add them.
E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
Make a method displayTime which should print the time.
Make a method DisplayMinute which should display the total minutes
in the Time. E.g.- (1 hr 2 min) should display 62 minute.
'''
class Time(object):

    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(t1, t2):
        x = Time(0, 0)
        x.hours = t1.hours + t2.hours
        x.minutes = t1.minutes + t2.minutes
        while x.minutes >= 60:
            x.hours += 1
            x.minutes -= 60
        return x

    def displayTime(self):
        print(f"Time is, {self.hours} hours and {self.minutes} minutes.")

    def displayMinutes(self):
        print((self.hours*60) + self.minutes, "minutes")

a = Time(2, 50)
b = Time(1, 20)
c = Time.addTime(a, b)
d = Time(1, 2)

c.displayTime()
d.displayMinutes()

'''
6. Write a Person class with an instance variable, , and a
constructor that takes an integer, , as a parameter.
The constructor must assign  to  after confirming the argument
passed as  is not negative; if a negative argument is passed as ,
the constructor should set  to  and print Age is not valid,
setting age to 0.. In addition, you must write the following
instance methods:
1. yearPasses() should increase the  instance variable by .
2. amIOld() should perform the following conditional actions:
○ If , print You are young..
○ If  and , print You are a teenager..
○ Otherwise, print You are old..
Sample Input:
4
-1
10
16
18
Sample Output:
Age is not valid, setting age to 0.
You are young.
You are young.
You are young.
You are a teenager.
You are a teenager.
You are old.
You are old.
You are old.
'''

class Person:
    def __init__(self, Age):
        if Age < 0:
            self.age = 0
            print("Age is not valid, setting age to 0")
        else:
            self.age = Age

    def yearPasses(self):
        self.age += 1

    def amIOLD(self):
        if self.age<13:
            print("You are Young. ")

        elif 13 <= self.age < 18:
            print("You are a Teenager. ")

        else:
            print("You are old. ")

x = int(input("Enter a count"))
for i in range(0, x):
    a = int(input("Please Enter your age: "))
    p = Person(a)
    p.amIOLD()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOLD()