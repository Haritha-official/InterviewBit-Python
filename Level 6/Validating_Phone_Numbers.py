import re

def main():
    """
    Indian Mobile Number Validator using Regular Expressions.

    Rules:
    - Must be exactly 10 digits long
    - First digit must be in the range 6–9
    - Remaining 9 digits can be 0–9

    Regex used:
    ^[6-9][0-9]{9}$
    - ^ → start of string
    - [6-9] → first digit must be 6, 7, 8, or 9
    - [0-9]{9} → exactly 9 digits (0–9)
    - $ → end of string
    """
    
    N = int(input())  # Number of test cases
    
    for _ in range(N):
        s = input().strip()  # Read each test string
        
        # Check against the regex pattern
        if re.match(r"^[6-9][0-9]{9}$", s):
            print("YES")
        else:
            print("NO")
    
    return 0


# Entry point of the program
if __name__ == '__main__':
    main()
