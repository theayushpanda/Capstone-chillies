# code chunk to print the frequency of characters in a string

def count_occurrences(string):
    
    # opening a dictionary
    
    letter_count = {}
    
    # for loop for counting frequency
    
    for letter in string:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

# example for 'google.com'

string = 'google.com'
letter_count = count_occurrences(string)
print(letter_count)
