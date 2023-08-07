# 6. **Count Vowels**: Write a Python program that counts the number of vowels in a given string.
#     - *Input*: "Hello"
#     - *Output*: "Number of vowels: 2"

input_str = "Hello"
vowels = "aeiouAEIOU"
count = 0
for char in input_str:
    if char in vowels:
        count += 1
        
print("Number of vowels:", count)
