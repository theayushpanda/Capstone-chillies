str_manip=input("Enter a sentence: ")
print(len(str_manip),"characters")                       #printing the length of the string

print(str_manip.replace(str_manip[-1],"@"))              #replacing every char same as the last char in the string by "@"
print(str_manip[-1:-4:-1])                               

first_word=str_manip[0:3]                                #creating a new word by creating a substring
last_word=str_manip[-2:]
new_word=first_word+last_word
                                                         #printing the new word
print(new_word)

def print_words(str_manip):                              #printing each word in a separate line
    words = str_manip.split()
    for word in words:
        print(word)

print_words(str_manip)