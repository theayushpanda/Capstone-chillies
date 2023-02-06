# code chunk for printing each word of a sentence in separate lines

sentence = input("Enter a sentence: ")
words = sentence.split()

# for loop for checking every word and printing it in a new line at every iteration

for word in words:
    print(word)