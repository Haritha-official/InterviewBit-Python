from itertools import permutations

def main():
    # -------------------------------------
    # Input: A string S and an integer K
    # Example: 
    #   Input: HACK 2
    #   Output: All possible permutations of length 2 from "HACK"
    # -------------------------------------
    S, K = input().split()
    K = int(K)
    
    # Generate all permutations of length K from the sorted string
    perms = permutations(sorted(S), K)
    
    # Print each permutation as a string
    for i in perms:
        print("".join(i))
    
    return 0


if __name__ == '__main__':
    main()
