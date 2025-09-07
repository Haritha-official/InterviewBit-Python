# main.py

# Define the main function
def main():
    # Create a set with some duplicate values
    # Note: Sets automatically remove duplicates
    my_set = set([1, 3, 2, 4, 1, 3, 3, 0])
    
    # Add multiple elements (10 to 23, excluding 11) to the set
    my_set.update([10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])
    
    # Remove elements 2 and 3 from the set (if they exist)
    my_set.discard(2)
    my_set.discard(3)
    
    # Convert the set into a list for sorting (since sets are unordered)
    li = list(my_set)
    li.sort()

    # Print the sorted list
    print(li)
    
    # Return 0 to indicate successful execution
    return 0

# Run the main function only if this file is executed directly
if __name__ == '__main__':
    main()
