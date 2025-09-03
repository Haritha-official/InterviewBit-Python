def main():
    # Read an integer input from the user (the upper limit)
    N = int(input("Enter a number: "))

    # Loop from 0 to N-1
    for i in range(0, N):
        # Skip the iteration if the number is even
        if i % 2 == 0:
            continue
        # Print the number if it is odd
        print(i)

    return 0  # Exit point of the program


# Standard Python convention: run main() only if the script is executed directly
if __name__ == '__main__':
    main()
