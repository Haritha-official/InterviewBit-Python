def main():
    # Create a tuple 'data' containing three values:
    # - A string "Robin"
    # - An integer 10
    # - Another string "chocolates"
    data = ("Robin", 10, "chocolates")
    
    # format_string is not used here, so it's set to None for now
    format_string = None  
    
    # Print a formatted string using the old-style '%' formatting
    # %s → string placeholder
    # %d → integer placeholder
    # %s → string placeholder
    # The tuple 'data' values are substituted in order
    print("Hello %s. You are currently left with %d %s." % data)
    
    return 0


if __name__ == '__main__':
    # Entry point of the program
    main()
