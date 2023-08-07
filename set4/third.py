# **Longest Common Prefix**: Given a list of strings, find the longest common prefix.
#     - *Input*: ["flower","flow","flight"]
#     - *Output*: "fl"


def longest_common_prefix(strs):
    if not strs:
        return ""

 
    shortest = min(strs, key=len)

   
    for i, char in enumerate(shortest):
        for string in strs:
            if string[i] != char:
                return shortest[:i]  
    return shortest 

# Test the function with the given input
input_list = ["flower", "flow", "flight"]
output = longest_common_prefix(input_list)
print(output)  # Output: "fl"
