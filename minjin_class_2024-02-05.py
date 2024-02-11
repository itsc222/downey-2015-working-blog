import random
import time
import math
#Conditionals

#Boolean Expressions

5 == 5

5 != 5

#comparison operators

# ==, equals
# !=, not equal to
# >, greater than
# <, less than
# >=, greater than or equal to
#etc.


def registration():
    return {input("Please enter your name: "):input("Please enter your age: ") + " years old."}

# reg = registration()

# print(reg)
price = random.randint(1, 200)

def guess_again(x):
    return(compPrice(x, price))

def compPrice(x, y):
    if x < 0:
        print("Prices cannot be negative.")
        return(guess_again(float(input("Guess again: "))))
    if x < y:
        print("Go higher")
        return(guess_again(float(input("Guess again: "))))
    elif x > y:
        print("Not that much!")
        return(guess_again(float(input("Guess again: "))))
    elif x == y:
        print('Bingo!')
        return


# compPrice(float(input("Type a number: ")), price)
    
def larger(x, y):
    if x == y:
        return("x and y are equal")
    elif x < y:
        return y
    else:
        return x

# print(larger(float(input("Enter a number: ")), float(input("Enter another number: "))))
    
#while statement
    
def raw():
    raw = input("Type something: ")
    while raw == "":
        raw = input("Please type something")

def countdown(n):
    while n > 0:
        print(n)
        time.sleep(0.05)
        n = n - 1
    print("Go!")

# countdown(100)

def getMean(x, y, z):
    # print(s)
    mean = ((x + y + z) / 3.0)
    return mean

# g = [random.randint(1, 100) for _ in range(50)]
# print(g)

# print(getMean(g))

def getSD(x, y, z):
    m = getMean(x, y, z)
    t = math.pow((x - m), 2) + math.pow((y-m), 2) + math.pow((z - m), 2)
    sd = math.sqrt(t / 3.0)
    return sd

# print(getSD(10, 20, 30))

# print(getMean(10, 20, 30))

# def allPos(x, y, z):
#     if x > 0 and y > 0 and z > 0:
#         return 1
#     return 0

# print(allPos(2, 3, 2))

def allPos(x, y, z):
    return x > 0 and y > 0 and z > 0

# if allPos(3, -60, 20):
#     print("All positive!")
# else:
#     print("Not all positive!")

fn = "Xiaofei"

length = len(fn)

# print(length)

first = fn[0]
second = fn[1]
last = fn[-1]
# last1 = fn[len(fn)]
last2 = fn[len(fn) - 1]

#slice

# print(fn[:6])

# print(fn[:-1])

# print(fn[:])

# print("Xiaofei" > "Lu")

# print("Luiz" < "Lu")

# print("luiz" > "Lu")

#Immutability

fn2 = fn[0] + "e" + fn[2:]

# print(fn2)

fn = " Xiaofei Lu "
# print(fn.strip()) # only removes the whitespace on the boundaries of the string.

a = "A"

a = (a.lower())

# print(a.upper())

#String traversal

def countChar(char, string):
    m = 0
    n = 0
    while m < len(string):
        if string[m].upper() == char.upper():
            n += 1
        m += 1
    return n


def countChar(char, string):
    n = 0
    for letter in string:
        if char.lower() == letter.lower():
            n = n + 1
    return char + " appears " +  str(n) + " times in " + string

string = "Minjin and Xiaofei"
letter = "i"

a = countChar(letter, string)

print(a)







