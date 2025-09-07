# main.py

# Define the main function
def main():
    # Create a dictionary with days of the week as keys
    # and assign numeric values to each day
    my_dict = {
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6,
        "Sunday": 0
    }

    # Update the value of Sunday from 0 to 7
    my_dict["Sunday"] = 7
    
    # Add a new key "Default" with value 0
    my_dict["Default"] = 0
    
    # Print dictionary items sorted by key
    # Format: ('Key', Value)
    for i in sorted(my_dict):
        print("('" + i + "',", str(my_dict[i]) + ")")

    # Return 0 to indicate successful execution
    return 0

# Run the main function only if this file is executed directly
if __name__ == '__main__':
    main()
