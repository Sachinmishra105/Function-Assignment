# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.


s = "The quick Brow Fox"

def upper_lower(str):
    count_upper = 0
    count_lower = 0
    for i in str:
        if i.isupper():
            count_upper += 1
        elif i.islower():
            count_lower +=1

    print(f'upper case letters:{count_upper}')  
    print(f'lower case letters:{count_lower}')
    return (count_upper,count_lower)
upper_lower("The quick Brow Fox")      