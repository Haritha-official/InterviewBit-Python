# main.py

"""
This program filters words with odd lengths from a given list of strings
using Python list comprehension.

Sample Output:
['given', 'intern', 'network', 'multiple', 'define', 'algorithm', 'phase']
"""

# Define the main function
def main():
    # Create a list of strings
    str_list = [
        'given', 'intern', 'InterviewBit', 'network', 'local',
        'multiple', 'define', 'nodes', 'algorithm', 'allows',
        'community', 'phase', 'single'
    ]
    
    # Use list comprehension to filter words with odd length
    # Condition: len(x) % 2 == 1 → word length is odd
    my_list = [x for x in str_list if len(x) % 2 == 1]
    
    # Print the filtered list
    print(my_list)
    
    # Return 0 to indicate successful execution
    return 0

# Run the main function only if this file is executed directly
if __name__ == '__main__':
    main()
