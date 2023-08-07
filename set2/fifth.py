# ### Problem **5: Concatenate two lists index-wise**

# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

# **Given**:

# ```
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# ```

# **Expected output:   ['My', 'name', 'is', 'Kelly']**


list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

result_list = [x + y for x, y in zip(list1, list2)]

print(result_list)
