fin = open('words.txt')
word_list = []
for line in fin:
    word = line.strip()
    word_list.append(word)

def twenty(list):
    for word in list:
        word = word.replace(' ', '')
        if len(word) > 20:
            print(word)
        else:
            pass
    return

# twenty(word_list)

def has_no_e(word):
    if "e" in word:
        print(word, True)
    else:
        pass
    return

# for word in word_list:
#     has_no_e(word)

def avoids(word_list):
    forbidden_letters = []
    forbidden_letters.append(input("What is forbidden letter #1?"))
    forbidden_letters.append(input("What is forbidden letter #2?"))
    forbidden_letters.append(input("What is forbidden letter #3?"))
    forbidden_letters.append(input("What is forbidden letter #4?"))
    forbidden_letters.append(input("What is forbidden letter #5?"))

    print(forbidden_letters)

    for word in word_list:
        for letter in word:
            if letter in forbidden_letters:
                return False
    return True
print((avoids(word_list)))