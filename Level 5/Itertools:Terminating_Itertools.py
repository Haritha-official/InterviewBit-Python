import itertools
import operator

def main():
    # Define three lists
    arr1 = [2, 1, 3, 4, 1]
    arr2 = [1, 2, 4]
    arr3 = [10, 3, 4, 3, 5, 6, 32, 11]
    
    # ----------------------------------------
    # 1. Merge all three lists into a single list (arr4)
    #    Elements will appear in order: arr1 → arr2 → arr3
    #    Using itertools.chain for efficient concatenation
    # ----------------------------------------
    arr4 = list(itertools.chain(arr1, arr2, arr3))
    print(arr4)
    
    # ----------------------------------------
    # 2. Compute successive multiplication (prefix product)
    #    using itertools.accumulate() with operator.mul
    #
    #    Example: [a, b, c] → [a, a*b, a*b*c]
    #    Store result in arr5
    # ----------------------------------------
    arr5 = list(itertools.accumulate(arr4, operator.mul))
    print(arr5)
    
    return 0


if __name__ == '__main__':
    main()
