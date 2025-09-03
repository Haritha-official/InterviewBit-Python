# Function to calculate the factorial of a number N
def factorial(N):
    # Base case: factorial of 0 is always 1
    if N == 0:
        return 1

    # Recursive case: N! = N × (N-1)!
    return N * factorial(N - 1)


# Example usage:
# print(factorial(5))  # Output: 120
