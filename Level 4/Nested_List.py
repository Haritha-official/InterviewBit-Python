# main.py

# Define the main function
def main():
    # Create a nested list with strings and a sublist
    my_list = [['a', 'b'], ['cc', 'dd', ['eee', 'fff']], ['g', 'h']]
    
    # Insert a new list [1, 2, 3] at the end of my_list
    my_list.append([1, 2, 3])
    
    # Print the list after appending
    print(my_list)
    
    # Delete 'eee' from the nested sublist inside my_list
    # Access path: my_list[1] → ['cc', 'dd', ['eee', 'fff']]
    # my_list[1][2] → ['eee', 'fff']
    # remove('eee') deletes the element 'eee'
    my_list[1][2].remove('eee')
    
    # Print the list after deleting 'eee'
    print(my_list)
    
    # Return 0 to indicate successful execution
    return 0

# Run the main function only if this file is executed directly
if __name__ == '__main__':
    main()
