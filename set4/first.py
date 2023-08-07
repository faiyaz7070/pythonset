# **Anagram Check**: Write a Python function that checks whether two given words are anagrams.
#     - *Input*: "cinema", "iceman"
#     - *Output*: "True"



def is_anagram(word1, word2):
    # Convert the input words to lowercase to make the comparison case-insensitive
    word1 = word1.lower()
    word2 = word2.lower()

    # Sort the characters of the words and compare if they are equal
    return sorted(word1) == sorted(word2)

# Test the function with the given input
word1 = "cinema"
word2 = "iceman"
result = is_anagram(word1, word2)
print(result)  # Output: True
