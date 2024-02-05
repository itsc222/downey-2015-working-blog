numbers = [10, 20, 30, 40]

list2 = ['crunchy frog', 'ram bladder', 'lark vomit']

list3 = ['spam', 2.0, 5, [10, 20]]

cheeses = ['Cheddar', 'Edam', 'Gouda']

print(cheeses)

# print(numbers, cheeses)

print(cheeses[0])

cheeses[1] = 'Pepperjack'

cheeses.append('Havarti')

print(cheeses)

print('Cheddar' in cheeses)

for cheese in cheeses:
    print(cheese)

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)

number_cheese = numbers + cheeses

print(number_cheese)

hella_cheeses = cheeses * 3

print(hella_cheeses)

cheeses.append('Colby Jack')

t = ['a', 'B', 'c']
t2 = ['D', 'e']

t.extend(t2)

print(t)

numbers = [5, 3, 9, 0, 1, 495, 2.3]

numbers.sort()

print(numbers)

def add_all(t):
    total = 0
    for x in t:
        total += x
    return total

print(add_all(numbers))

print(sum(numbers))

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return(res)

print(capitalize_all(t))

def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res

print(only_upper(t))

# c = cheeses.pop(1)

# print(c)

# del cheeses[0]

# del cheeses[0:3]

# cheeses.remove('Havarti')

# print(cheeses)

s = 'spam'
t = list(s)

print(t)

a = [1, 2, 3]
b = a

print(b is a)

b[0] = 42

print(a)

def delete_head(t):
    del t[0]

# delete_head(t)

# print(t)
    
def tail(t):
    return t[1:]

# print(tail(t))

rest = tail(t)

print(rest)



