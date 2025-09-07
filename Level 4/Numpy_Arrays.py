# main.py

"""
This program demonstrates how to work with NumPy arrays in Python.
It converts a list into a NumPy ndarray and finds all the indexes of a given value.

Steps:
1. Convert a Python list into a NumPy ndarray.
2. Use np.where() to locate all positions of a specific value (in this case, 2).

Sample Output:
<class 'numpy.ndarray'>
(array([2, 3, 7], dtype=int64),)
"""

import numpy as np

# Define the main function
def main():
    # Create a simple Python list
    my_arr = [1, 3, 2, 2, 5, 3, 8, 2]
    
    # Convert the list into a NumPy ndarray
    arr = np.array(my_arr)
    
    # Print the type to confirm conversion
    print(type(arr))
    
    # Use np.where() to find all the indexes of value 2
    x = np.where(arr == 2)
    
    # Print the result (tuple of arrays containing indices)
    print(x)
    
    # Return 0 to indicate successful execution
    return 0

# Run the main function only if this file is executed directly
if __name__ == '__main__':
    main()
