import math
import time

x = 5

x = 7

print(x)

a = 5
b = a
print(b)
a = 3
print(b)

def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
        # time.sleep(0.1)
    print('Blastoff!')

countdown(10)

def sequence(n):
    while n != 1:
        print(n)
        if n % 2 == 0: #n is even
            n = n/2
        else:
            n = n * 3 + 1 #n is odd

sequence(3)

#Collatz Conjecture

def print_n(s, n):
    while n > 0:
        print(s)
        n = n - 1
    return

print_n("yes!", 4)

# while True:
#     line = input('>')
#     if line == 'done':
#         break
#     print(line)

# print('Done!')

a = 4
x = 3
y = (x + a/x) / 2

print(y)

x = y
y = (x + a/x) / 2

print(y)

x = y
y = (x + a/x) / 2

print(y)

x = y
y = (x + a/x) / 2

print(y)

x = y
y = (x + a/x) / 2

print(y)

x = y
y = (x + a/x) / 2

print(y)

a = 16
x = 3

while True:
    print(x)
    y = (x + a / x) / 2
    epsilon = 0.001
    if abs(y - x) < epsilon:
        break
    x = y






