import math

print(type(42))

print(int(2.34343))
print(float('2.49392'))
print(str(32))

# ratio = signal_power / noise_power
# decibels = 10 * math.log10(ratio)

radians = 0.7
height = math.sin(radians)

degrees = 45
radians = degrees / 180.0 * math.pi
print(math.sin(radians))
print(math.sqrt(2)/2.0)

x = math.sin(degrees / 360.0 * 2 * math.pi)

x = math.exp(math.log(x + 1))

def print_lyrics():
    print("I'm a lumberjack and I'm okay.")
    print("I sleep all night and I work all day.")
    return

print(print_lyrics)
print(type(print_lyrics))

print_lyrics()

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()

def print_twice(bruce):
    print(bruce)
    print(bruce)

print_twice('Spam')

print_twice(42)

print_twice(math.pi)

print_twice('Spam' * 4)

print_twice(math.cos(math.pi))

michael = 'Eric, the half a bee'

print_twice(michael)

def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)

line1 = 'Bing tiddle '
line2 = 'tiddle bang'

cat_twice(line1, line2)

# print(cat)

x = math.sqrt(5)
golden = (math.sqrt(5) + 1 / 2)

result = print_twice("bing")
print(result)
print(type(result))

# print(' ' * 65 + 'monty')

#Excercise 3.1
def right_justify(monty):
    print(' ' * (70 - len(monty)) + monty)
    return

monty = "drugs"
right_justify(monty)

def do_twice(f, value):
    f(value)
    f(value)

def print_spam(red):
    print(red)

do_twice(print_spam, 'capitalism')

