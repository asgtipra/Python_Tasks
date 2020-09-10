# ////// 1
elementList = [10, "welcome", 30.0, 10 + 20j, 40, 50.0,"to", "Python", 40 -10j, 100]


# ////// 2
elements = ["10",40, 30.0, "hello", "world"]
print(elements[0])
print(elements[2:4])
print(elements[4:5])

# ////// 3
numberList = [10, 20, 30, 50]
sum = 0 
mult = 1
for i in numberList:
    sum = sum  + i
    mult = mult * i 

print(sum)
print(mult)


# ///////4
listInfo = [-1, -10, 150, 20, 100, 40]
print(min(listInfo))
print(max(listInfo))

# ///////5
listInfo = [1,2,4,8, 11, 15, 21]
listOdd = []
for i in listInfo:
    if i%2 != 0:
        listOdd.append(i)
print(listOdd)

# ///////// 6
listSquare = []
for i in range(1, 31):
    if i * i <  31:
        listSquare.append(i)
print(listSquare)


# //////// 7
list1 = [1,3, 5, 7, 9, 10]
list2  =[2, 4, 6, 8]
list1[-1: ] = list2 
print(list1)


# //////// 8
a = { 1: 10 , 2: 20}
b = {3: 30, 4:40}
a.update(b)
print(a)


# //////// 9 
dict1  = { }
for i in range(1, 6):
    dict1[i] = i * i
print(dict1)

# //////// 10 
x = "34, 67, 55, 33, 12, 98"
list1 = x.split()
tupp = tuple(list1)
print(list1)
print(tupp)

# //////// 11
elementList = [10, "welcome", 30.0, 10 + 20j, 40, 50.0,"to", "Python", 40 -10j, 100]

# /////// 12
elements = ["10",40, 30.0, "hello", "world"]
print(elements[0])
print(elements[2:4])
print(elements[4:5])


# /////// 13
x = [100, 200, 300, 400, 500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600, 700, 800]
# part 1
print(x[5][0:4])

# part 2
print(x[6:8])

#  part 3
print(x[0:len(x):2])

# part 4 
print(x [::-1])


# part 5 
print(x[5][5][0:1])

#part 6
print(x[:-0])


# //////14
list1 =  []
for i in range(1000):
    print(i)

# ////// 15
Tuple advantages:
immutable
consumes less memory
Can use in a dictionary as key but its not possible with lists

# ////// 16
for i in range(1, 101):
    if i%3 == 0 and i%2 ==0:
        print(i)


# ////// 17
str1 = "helloworld"
str1 =str1.lower()
print(str1[::-1])
for i in range(len(str1)):
    if str1[i] =="a" or str1[i] == "e" or str1[i] == "i" or str1[i]=="o" or str1[i] =="u":
        print(i, str1[i])

# ////// 18
str1 = "hello my name is abcde"
str1 = str1.split()
for i in str1:
    if len(i) % 2 == 0:
        print(i)


# /////// 19 
x = [1,2,3,4,5,6,7,8,9,-1]
for i in range(len(x)):
    for j in range(i+1,len(x)):
        if x[i] + x[j] == 8:
            print(x[i], x[j])


# /////// 20
 
evenList = [2,4,6,8,10,16]
oddList = [1,3,5,9,11]
for i in range(10):
    num = int(input("Enter the number in the range of 1-50"))
    if num % 2 ==0 : 
        evenList.append(num)
    elif num %3 == 0:
        oddList.append(num)
print(sum(evenList))
print(max(evenList))
print(sum(oddList))
print(max(oddList))


# //////21

str1 = "12abcbacbaba344ab"
dict1 ={}

for i in str1:
    if i.isalpha():
        if i in dict1:
            dict1[i] = dict1[i] + 1
        else:
            dict1[i] = 1
for i in dict1:
    print(str(i) +"="+ str(dict1[i]))





# ////// 22
x = (1,2,3,4,5,6,7,8,9,10)
x1 = []
for i in x:
    if i % 2 ==0:
        x1.append(i)
x1 = tuple(x1)
print(x1)

