# 9. **Fibonacci Sequence**: Write a Python function that generates the first n numbers in the Fibonacci sequence.
#     - *Input*: 5
#     - *Output*: "[0, 1, 1, 2, 3]"

# First Method
def fibonacci_sequence(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_number = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_number)
    return sequence[:n]

# Test the function
input_num = 5
fibonacci = fibonacci_sequence(input_num)
print(f"{fibonacci}")


# Second Method
def fibonacci_sequence(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        sequence = [0, 1]
        for i in range(2, n):
            next_number = sequence[i - 1] + sequence[i - 2]
            sequence.append(next_number)
        return sequence

# Test the function
input_num = 5
fibonacci = fibonacci_sequence(input_num)
print(f"{fibonacci}")
