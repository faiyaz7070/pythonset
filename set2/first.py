# Problem **1: Print the following pattern**

# Write a program to print the following number pattern using a loop.

# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


for i in range(1,6):
    bag=""
    for j in range(1,i+1):
        bag+=str(j)+" "
    print(bag)