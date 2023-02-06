# program to convert every alternate character to uppercase and every other to lowercase

def alternate_case(s):
  s = list(s)
  
  # for loop to test character position in the string and convert into upper and lower case

  for i in range(len(s)):
    if i % 2 == 0:
      s[i] = s[i].upper()
    else:
      s[i] = s[i].lower()
  return "".join(s)

# storing the string and printing
string = input("Enter a string: ")

print(alternate_case(string))

# code chunk to convert every alternate word into upper and lowercase

words = string.split()

# for loop to determine word position and cast upper and lowercase

for i in range(len(words)):
    if i % 2 == 0:
        words[i] = words[i].upper()
    else:
        words[i] = words[i].lower()

# printing final result

result = " ".join(words)
print(result)
