import re

def main():
    """
    Roman Numeral Validator (1–3999) using Regular Expressions.

    Rules covered by the regex pattern:
    - Thousands: M{0,3} → 0 to 3 'M' (1000, 2000, 3000)
    - Hundreds: (CM|CD|D?C{0,3})
        - CM → 900
        - CD → 400
        - D?C{0,3} → 0–300 (C to CCC) or with D (500–800)
    - Tens: (XC|XL|L?X{0,3})
        - XC → 90
        - XL → 40
        - L?X{0,3} → 0–30 (X to XXX) or with L (50–80)
    - Ones: (IX|IV|V?I{0,3})
        - IX → 9
        - IV → 4
        - V?I{0,3} → 0–3 (I to III) or with V (5–8)

    The program:
    - Reads N (number of test cases)
    - Reads N Roman numeral strings
    - Validates each against the regex
    - Prints "YES" if valid, otherwise "NO"
    """
    
    n = int(input().strip())
    
    # Regex pattern to match valid Roman numerals (1–3999)
    pattern = re.compile(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$")
    
    for _ in range(n):
        s = input().strip()
        
        # fullmatch() ensures the entire string is validated
        if pattern.fullmatch(s):
            print("YES")
        else:
            print("NO")


# Entry point of the program
if __name__ == '__main__':
    main()
