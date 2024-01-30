import time
import math
#Programming skills

#think creatively about solutions
#express solution explicitly and accurately.

#think about solutions step-by-step

# A Program
# input
# output
# calculations
# conditional execution
# repetition


#This code will write a sexual script. lol.
def sex(n):
    start_time = time.time()
    while n > 0:
        if n % 5 == 4:
            print('Oh God!')
            time.sleep(.8)

        if n % 4 == 3:
            print("Oh!")
            time.sleep(1)
        if n % 3 == 2:
            print("*bed creaking sounds*")
            time.sleep(0.5)
        if n % 3 == 1:
            print("Fuck!")
            time.sleep(.9)
        else:
            print('Uh!')
            time.sleep(1.2)
        n = n-1
    time.sleep(2)
    end_time = time.time()
    sex_time = round(end_time - start_time, 1)
    print("Ahhhhhh! I came.")
    print(f"You had sex for {round((sex_time / 2), 0)} minutes.")

# sex(10)
    
print("Minjin", "Kim")

instructor = "Xiaofei Lu"

students = 7

pi = math.pi

print(instructor, students, pi)

print(21 % 5)

# print = print("print")

print((1 + 2) ** (8 / 4) - (3 * 7))
fn = "Zimeng"
ln = "Shao"


#This code will print an interaction between several people who all go by the same name.
def print_name(fn, ln, n):
    print(f"There are {n} " + fn + " " + ln + "s")
    print("Let's introduce ourselves.")
    time.sleep(1)
    while n > 0:
        print("My name is " + fn + " " + ln)
        time.sleep(1)
        print("Nice to meet you!")
        time.sleep(1)
        n = n - 1
    return

# print_name(fn, ln, 3)

name = fn + " " + ln

# print(name)

type_of_32 = type(32)

print(type_of_32)

a = 32

b  = float(a)

s = str(a)

print(type(a), type(s))

print(str(a) + " words. Hell yeah, brother!")

print(a + b)

import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

sentence = "There are seven students in this classroom and four of them are on drugs"
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)

# print(tokens)

def print_dashes():
    dashes = ("-" * 2)
    print(dashes)
    return(dashes)

# print_dashes()
    
print(tokens)

def printTitle(title):
    print_dashes()
    print(title)
    print_dashes()
    return


booktitle = "Pride and Prejudice"
printTitle(booktitle)

# sex(12)

def print_my_title(title, marker, n):
    print(marker * n)
    print(title)
    print(marker * n)

booktitle = "Pride and Prejudice"
marker = "*" * len(print_dashes())

print_my_title(booktitle, marker, 20)

sex(9)