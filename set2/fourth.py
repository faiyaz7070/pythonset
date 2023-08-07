# ### Problem **4: Arrange string characters such that lowercase letters should come first**

# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

# **Given**:

# ```
# str1 = PyNaTive
# ```

# **Expected Output**:

str1 = "PyNaTive"

lowercase_chars = ""
uppercase_chars = ""

for char in str1:
    if char.islower():
        lowercase_chars += char
    else:
        uppercase_chars += char

arranged_string = lowercase_chars + uppercase_chars
print(arranged_string)
