def main():
    # ----------------------------------------
    # Input:
    #   Line 1: List A (space-separated elements)
    #   Line 2: List B (space-separated elements)
    #
    # Task:
    #   For each element in B:
    #     - If element is not in A, print -1
    #     - If element is in A, print all indices where it occurs in A
    #
    # Example:
    #   Input:
    #     1 2 3 2 4
    #     2 5
    #   Output:
    #     1 3
    #     -1
    # ----------------------------------------
    
    A = input().split()
    N = len(A)   # size of list A
    B = input().split()
    M = len(B)   # size of list B
    
    # For each element in B, check its presence in A
    for i in B:
        if i not in A:
            # Element not found in A
            print(-1)
            continue
        
        # Print all indices where element occurs in A
        for k, v in enumerate(A):
            if v == i:
                print(k, end=' ')
        print()  # move to next line after indices
    
    return 0


if __name__ == '__main__':
    main()
