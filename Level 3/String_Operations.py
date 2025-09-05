def main():
    # Take input string from the user
    S = input()
    
    # Print the length of the string
    print(len(S))
    
    # Print the index (first occurrence) of the character 'a'
    # Note: It's guaranteed that 'a' exists in the string
    print(S.index("a")) 
    
    # Print every 2nd character starting from index 0
    # Slice format: S[start:end:step]
    # Here:
    # start = 0 (beginning of string)
    # end   = default (till end of string)
    # step  = 2 (take every second character)
    print(S[0::2])
    
    return 0


if __name__ == '__main__':
    # Entry point of the program
    main()
