# 4. **Sum and Average**: Write a Python program that calculates and prints the sum and average of a list of numbers.
#     - *Input*: [10, 20, 30, 40]
#     - *Output*: "Sum: 100, Average: 25.0"

arr = [10, 20, 30, 40]

# Sum
sum=0
for i in range(len(arr)):
    sum+=arr[i]
    
print(sum)

# Average
sum1=0
for i in range(len(arr)):
    sum1+=arr[i]
    
print(sum1/len(arr));    