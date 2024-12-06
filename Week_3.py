# Name : Kem
# November 29 , 2024

text = "Hi, my name is Kem! What is yours?"
index = text.find("Kem")
print(index) # Prints out index of name

# PRINTS OUT NAME
substring = text[index:index+3]
print(substring)

string1 = input ("Enter your 1st word:")
string2 = input ("Enter your 2nd word:")

if len(string1)> len(string2):
    print("Word 1 is longer!")
elif len(string1) < len(string2):
    print("Word 2 is longer")
else:
    print("Both your words are equal in legnth!")
