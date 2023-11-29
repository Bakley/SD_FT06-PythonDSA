def print_fibonacci(length):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(length):
        fib_sequence.append(a)
        a, b = b, a + b
    print("Fibonacci sequence:")
    print(fib_sequence)

# Example usage:
length_to_generate = 10  # Change this value to generate a different length of the sequence
print_fibonacci(length_to_generate)