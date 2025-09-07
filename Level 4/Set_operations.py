# main.py

# Helper function to print set elements in a sorted list format
def printset(s):
    print(sorted(list(s)))

# Define the main function
def main():
    # Define three sets representing students who play each sport
    # X → Students who love Football
    # Y → Students who love Cricket
    # Z → Students who love Basketball
    X = set([1, 3, 7, 5, 6, 10, 20, 21, 22, 23, 55, 51, 2, 19, 9, 17, 27, 26, 25, 35])
    Y = set([2, 10, 13, 18, 17, 22, 28, 27, 5, 49, 46, 43, 3])
    Z = set([21, 1, 32, 25, 12, 11, 8, 10, 26, 16, 31, 20, 30, 14])
    
    # set1 → Students who love ALL THREE sports (intersection of X, Y, Z)
    set1 = X.intersection(Y, Z)
    printset(set1)
    
    # set2 → Students who love Football AND Cricket, but NOT Basketball
    set2 = X.intersection(Y).difference(Z)
    printset(set2)
    
    # set3 → Students who love ONLY Cricket (not Football, not Basketball)
    set3 = Y.difference(X, Z)
    printset(set3)
    
    # Return 0 to indicate successful execution
    return 0

# Run the main function only if this file is executed directly
if __name__ == '__main__':
    main()
