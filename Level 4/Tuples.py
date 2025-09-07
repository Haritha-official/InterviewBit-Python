# main.py

# Define the main function
def main():
    # Create two tuples
    tuple1 = tuple(("one", "two", "three"))
    tuple2 = tuple(("1", "2", "3"))
    
    # Tuples are immutable, so to modify them,
    # first convert them into lists
    tuple1 = list(tuple1)
    tuple2 = list(tuple2)
    
    # Change the value at index 0 of both tuples to "number"
    tuple1[0] = "number"
    tuple2[0] = "number"
    
    # Convert the lists back into tuples
    tuple1 = tuple(tuple1)
    tuple2 = tuple(tuple2)
    
    # Print the modified tuples
    print(tuple1)
    print(tuple2)
    
    # Return 0 to indicate successful execution
    return 0

# Run the main function only if this file is executed directly
if __name__ == '__main__':
    main()
