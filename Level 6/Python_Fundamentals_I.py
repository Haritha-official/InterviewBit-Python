from functools import reduce 
import math

def main():
    # ----------------------------------------
    # Example demonstrating Python's
    # functional programming tools:
    # - map()
    # - filter()
    # - reduce()
    # ----------------------------------------
    
    # Use map() to calculate the square of each number
    my_ints = [4, 6, 3, 9, 2, 8, 12]
    
    # Use filter() to extract only the names 
    # that are less than or equal to 7 letters
    my_names = ["scaler", "interviewbit", "rishabh", "student", "course"]
    
    def seven_letters(names):
        """Return True if the given name has <= 7 characters"""
        return len(names) <= 7
    
    # Use reduce() to calculate the product of all numbers
    my_numbers = [4, 6, 9, 23, 5]
    
    # Applying map: squares of integers
    map_result = list(map(lambda x: x**2, my_ints))
    
    # Applying filter: names with <= 7 letters
    filter_result = list(filter(seven_letters, my_names))
    
    # Applying reduce: product of numbers
    reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)
    
    # Printing the results
    print("Squares using map():", map_result)
    print("Filtered names using filter():", filter_result)
    print("Product using reduce():", reduce_result)
    
    return 0

# Entry point of the program
if __name__ == '__main__':
    main()
