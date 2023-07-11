
# Write a Python program to reverse a string

s = "1234abcd"

def reverse(string):
    string = string[::-1]
    return string
 

print("The original string is : ", end="")
print(s)
 
print("The reversed string is : ", end="")
print(reverse(s))