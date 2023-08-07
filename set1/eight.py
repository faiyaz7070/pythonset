# 8. **Factorial Calculation**: Write a Python function that calculates the factorial of a number.
#     - *Input*: 5
#     - *Output*: "Factorial of 5 is 120."

# First Method
def factorial(n):
    if n == 0: return 1
    else: return n * factorial(n - 1)

# Test the function
input_num = 5
result = factorial(input_num)
print(f"Factorial of {input_num} is {result}.")


# Second Method
def factorial2(n):
    result2 = 1
    for i in range(1, n + 1):
        result2 *= i
    return result2

# Test the function
input_num1 = 8
result2 = factorial2(input_num1)
print(f"Factorial of {input_num1} is {result2}.")
