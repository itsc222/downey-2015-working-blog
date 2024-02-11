import pprint

eng2sp = dict()

# print(eng2sp)

eng2sp['one'] = 'uno'
eng2sp['dog'] = 'perro'

# print(eng2sp)

eng2sp['two'] = 'dos'
eng2sp['three'] = 'tres'

# print(eng2sp['two'])

# print('two' in eng2sp)

# print(len(eng2sp))

# print(eng2sp['dos'])

alphabet_dict = {}
for i in range(26):
    letter = chr(ord('A') + i)
    alphabet_dict[letter] = i + 1

# Display the resulting dictionary
# print(alphabet_dict)
    
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

hist = histogram('deamericanization')

# print(hist)

h = histogram('a')
# print(h)

print(h.get('a', 0))

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

# print(histogram('americanism'))

#Looping and dictionaries

def print_hist(h):
    for c in h:
        print(c, h[c])

h = histogram('parrot')
print_hist(h)

print('\n\n')

for key in sorted(h):
    print(key, h[key])

#11.4 reverse lookup
    
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
        raise LookupError()

key = reverse_lookup(h, 1)

# print(key)

#11.5 Dictionaries and Lists

def inverse_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

sp2eng = inverse_dict(eng2sp)
print(sp2eng)
print(eng2sp)

#Memos

#memoized version of Fibonacci:

known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return(known[n])
    res = fibonacci(n-1) + fibonacci(n - 2)
    known[n] = res
    return(res)

fibonacci(2)
fibonacci(3)
fibonacci(10)

print(known)

#Global variables

verbose = True

def example1():
    if verbose:
        print("Running example1")


been_called = False

def example2():
    been_called = True #wrong

def example2():
    global been_called
    been_called = True

count = 0

def example3():
    global count
    count += 1

pprint.pprint(known)
print(known)