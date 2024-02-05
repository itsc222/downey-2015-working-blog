import math

fruit = 'banana'
letter = fruit[1]

print(letter)

print(len(fruit))

length = len(fruit)

last = fruit[length - 1]

print(last)

print(fruit[-1])

index = 0

while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

for letter in fruit:
    print(letter)

prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    print(letter + suffix)

length = len(prefixes)
index = list(range(length))

for i in index:
        if prefixes[i] == 'O' or prefixes[i] == 'Q':
            print(prefixes[i] + 'u' + suffix)
        else:
             print(prefixes[i] + suffix)

s = 'Monty Python'

print(s[0:5])
print(fruit[:3])
print(fruit[3:])

print(fruit[:])

greeting = 'Hello, world!'

new_greeting = 'J' + greeting[1:]

print(new_greeting)

def find(word, letter, start_index):
    index = start_index
    while index < len(word):
          if word[index] == letter:
               return index
          index = index + 1
    return(-1)

print(find('Chinese', 'e', 5))

# def count(word, letter):
#      index = 0
#      while index < len(word):
#           n = 0
#           if word[index] == letter:
#                return n + 1
#           index = index + 1
#      return 0

# print(count('american', 'a'))

def count(word, letter):
     count = 0
     for item in word:
          if item == letter:
               count = count + 1
     return(count)

print(count('anti-american', 'a'))

word = 'banana'

new_word = word.upper()

print(new_word)

index = word.find('a')

print(index)

word.find('na')

print('a' in word)

print('seed' in word)

def in_both(word1, word2):
     for letter in word1:
          if letter in word2:
               print(letter)

in_both('american', 'korean')

if word == 'banana':
     print('All right, bananas')

def before_or_after_banana(word):
    word = word.lower()
    if word < 'banana':
        print('Your word, ' + word + ', comes before banana')
    elif word > 'banana':
        print('Your word, ' + word + ' comes after banana.')
    else:
     print('All right, bananas.')

before_or_after_banana('Bomato')



