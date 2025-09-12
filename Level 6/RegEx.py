import re

def main():
    """
    Demonstration of Python's re (regular expressions) module:
    - findall() → returns all matches of a pattern
    - search()  → finds first match and returns its position
    - sub()     → replaces matches with a given string
    """
    
    txt = "The quick brown fox jumps over the lazy dog"
    
    # Find all occurrences of the character 'o' in the string
    x = re.findall("o", txt)
    print("All 'o' characters:", x)
    
    # Find the first occurrence of 'h' and print its index position
    y = re.search("h", txt)
    print("Index of first 'h':", y.start())
    
    # Replace the first 3 whitespace characters with '#'
    z = re.sub("\s", "#", txt, 3)
    print("Text after replacing first 3 spaces:", z)
    
    return 0


# Entry point of the program
if __name__ == '__main__':
    main()
