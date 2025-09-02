# Define the main function
def main():
    # Take the first integer input from the user and store it in variable A
    A = int(input())
    
    # Take the second integer input from the user and store it in variable B
    B = int(input())
    
    # Print the sum of A and B
    print(A + B)
    
    # Print the difference of A and B (A - B)
    print(A - B)
    
    # Print the product of A and B
    print(A * B)
    
    # Print the quotient when A is divided by B (integer division, result is an integer)
    print(A // B)
    
    # Print the quotient when A is divided by B (floating-point division, result can be decimal)
    print(A / B)
    
    # Print the remainder when A is divided by B (modulo operation)
    print(A % B)
    
    # Print A raised to the power of B (exponentiation)
    print(A**B)
    
    # Return 0 to indicate successful completion (not necessary in Python, but okay)
    return 0


# This checks if the file is being run directly (not imported as a module)
if __name__ == '__main__':
    main()
