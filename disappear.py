# code to remove characters from a string after asking the user to input characters to be removed

sentence = input("Enter a sentence: ")
characters_to_remove = input("Enter the characters to remove: ")

# for loop to check every character and replace it if it is matched with the user input

for char in characters_to_remove:
    sentence = sentence.replace(char, "")

print("Resultant string: " + sentence)
