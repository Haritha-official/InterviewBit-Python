def main():
    """
    Division with Exception Handling.

    The program:
    - Reads T (number of test cases)
    - For each test case:
        - Reads two inputs (a, b)
        - Tries to convert them into integers
        - Prints the result of integer division a // b
    - Handles exceptions:
        - ZeroDivisionError → if divisor is zero
        - ValueError → if inputs are not integers
    """
    
    T = int(input().strip())  # Number of test cases
    
    for _ in range(T):
        a, b = input().split()  # Read two values
        
        try:
            # Convert inputs to integers
            a = int(a)
            b = int(b)
            
            # Perform integer division
            print(a // b)
        
        # Handle division by zero
        except ZeroDivisionError as e:
            print("Error Code:", e)
        
        # Handle invalid input (non-integer values)
        except ValueError as e:
            print("Error Code:", e)

    return 0


# Entry point of the program
if __name__ == '__main__':
    main()
