from collections import Counter

def main():
    # ====================================================
    # Problem:
    #   A shopkeeper has N shops, each selling a specific type of chocolate.
    #   Customers arrive with queries to buy chocolates.
    #
    # Input Format:
    #   Line 1: N (number of shops)
    #   Line 2: N integers → type of chocolate sold at each shop
    #   Line 3: M (number of customers/queries)
    #   Next M lines: x choc_type
    #       - x = money customer pays
    #       - choc_type = type of chocolate they want
    #
    # Rules:
    #   - If a shop has the requested choc_type available:
    #         add x to total revenue
    #         reduce availability of that choc_type by 1
    #   - If choc_type is not available: ignore the request
    #
    # Output:
    #   Total revenue after processing all M customers
    #
    # Example:
    #   Input:
    #     5
    #     1 2 3 2 1
    #     3
    #     10 2
    #     5 1
    #     7 4
    #
    #   Output:
    #     15
    #   (10 for choc_type 2, 5 for choc_type 1, ignore choc_type 4)
    #
    # Approach:
    #   - Use collections.Counter to track chocolate availability
    #   - Iterate through customer queries and update revenue
    #
    # Complexity:
    #   Time: O(N + M)   (building Counter + processing queries)
    #   Space: O(N)      (to store chocolate counts)
    # ====================================================

    N = int(input().strip())
    shops = list(map(int, input().split()))

    # Count availability of each chocolate type
    shop_count = Counter(shops)

    M = int(input().strip())
    total
