import math

e = math.exp(1.0)

def area(radius):
    a = math.pi * radius ** 2
    return a

def area(radius):
    return math.pi * radius ** 2

print(area(3))

def compare(x, y):
    if x > y:
        return(1)
    if x == y:
        return(0)
    if x < y:
        return(-1)
    
print(compare(3, 1))

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    # print("dsquared is", dsquared)
    result = math.sqrt(dsquared)
    return(result)

print(distance(1, 2, 4, 6))

def hypotenuse(a, b):
    return("The hypotenuse is", math.sqrt(a **2 + b ** 2))

print(hypotenuse(3, 4))

def circle_area (xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return(result)

#make more concise:
def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))

print(circle_area(4, 5, 7 , 1))

def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False
    
print(is_divisible(6, 3))
print(is_divisible(3, 5))

def is_between(x, y, z):
    if x <= y and z >= y:
        return(print(True))
    else:
        return(print (False))

is_between(5, 6, 10)

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        return result
    
print(factorial(3))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n - 2)
    
print(fibonacci(10))

def factorial(n):
    if not isinstance(n, int):
        print('factorial is only defined for integers')
        return None
    elif n < 0:
        print('Factorial is only defined for positive integers.')
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(-4))

def factorial(n):
    space = ' ' * (4*n)
    print(space, 'factorial', n)
    if n == 0:
        print(space, 'returning 1')
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        print(space, 'returning', result)
        return result

factorial(4)


