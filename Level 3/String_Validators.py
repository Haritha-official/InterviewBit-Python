def main():
    # Take input string from the user
    S = input()
    
    # Check if the string contains at least one alphanumeric character (letters or digits)
    print(any(c.isalnum() for c in S)) 
    
    # Check if the string contains at least one alphabet character (a-z or A-Z)
    print(any(c.isalpha() for c in S))
    
    # Check if the string contains at least one digit (0-9)
    print(any(c.isdigit() for c in S))
    
    # Check if the string contains at least one lowercase letter (a-z)
    print(any(c.islower() for c in S))
    
    # Check if the string contains at least one uppercase letter (A-Z)
    print(any(c.isupper() for c in S))
    
    return 0


if __name__ == '__main__':
    # Entry point of the program
    main()
