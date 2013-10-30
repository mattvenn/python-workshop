"""
Design, code test and evaluate a system to accept and test a password for certain characteristics. 
* It should be at least 6, and no more than 12 characters long 
* The system must indicate that the password has failed and why, asking the user to re enter 
their choice until a successful password is entered. 
* A message to indicate that the password is acceptable must be displayed. 
* Password strength can be assessed against simple criteria to assess its suitability; for 
example a password system using only upper and lower case alphabetical characters and 
numeric characters could assess the password strength as: 
* WEAK if only one type used, eg all lower case or all numeric 
* MEDIUM if two types are used 
* STRONG if all three types are used

For example 
hilltop, 123471324, HAHGFD are all WEAK, 
catman3 and 123456t are MEDIUM and 
RTH34gd is STRONG 
* A message to indicate the password strength should be displayed after an acceptable 
password is chosen.
"""

#fetch the password, keep going until between 6 and 12 chars long
while True:
    password = raw_input("enter password: ")

    if len(password) > 6 and len(password) < 12:
        print "password acceptable"
        break
    else:
        print "password is too long or short, please try again."

#setup some counters for our chars
lowercase = 0
uppercase = 0
numeric = 0

#go through the letters in the password, increasing our count of different types of chars
for letter in password:
    if letter.isdigit():
        numeric += 1
    if letter.isupper():
        uppercase += 1
    if letter.islower():
        lowercase += 1

#if a different type of char is used, increase the strength
strength = 0
if numeric > 0:
    strength += 1
if uppercase > 0:
    strength += 1
if lowercase > 0:
    strength += 1
 
#print out our verdict
if strength <= 1:
    print "weak"
elif strength == 2:
    print "medium"
else:
    print "strong"
