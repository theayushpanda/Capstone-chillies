# This example program is meant to demonstrate errors.

# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

print("Welcome to the error program")                   #no brackets (syntax error)
print("\n")                                             #unnecessary indent (syntax error)

ageStr = "24" #I'm 24 years old.                        #ageStr should be assigned not equated (syntax error) + unnecessary long string (logical error)
age = ageStr
print("I'm " + age + " years old.")
three = "3"

answerYears = int(age) + int(three)                          #variable 'three' should be converted into int data type (syntax error)

print("The total number of years:" + str(answerYears))        #missing brackets (Syntax error) + variable name in quotes (Syntax error) + answerYears should be concatenated to str (Runtime error)
answerMonths = answerYears * 12 + 6                        #wrong variable name 'answer', should be 'answerYears' (Syntax error) + incorrect logic (logical error)
print("In 3 years and 6 months, I'll be " + str(answerMonths) + " months old")           #missing bracket (Syntax error) and needed to concatenate (Runtime error)

#HINT, 330 months is the correct answer

