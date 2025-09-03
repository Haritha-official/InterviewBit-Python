def main():
    # Take input from the user (marks as an integer)
    num = int(input("Enter your marks: "))

    # Check the grade based on the marks and print the corresponding grade
    if num >= 90:
        print("A")  # Grade A for marks 90 and above
    elif num >= 80:
        print("B")  # Grade B for marks 80–89
    elif num >= 70:
        print("C")  # Grade C for marks 70–79
    elif num >= 60:
        print("D")  # Grade D for marks 60–69
    elif num >= 50:
        print("E")  # Grade E for marks 50–59
    else:
        print("F")  # Grade F for marks below 50

    return 0  # Exit point of the program


# Standard Python practice: only run main() if this file is executed directly
if __name__ == '__main__':
    main()
