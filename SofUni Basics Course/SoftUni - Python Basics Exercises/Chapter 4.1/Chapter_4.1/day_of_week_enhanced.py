# day_of_week.py (enhanced)

# Define a dictionary to store the day names and their corresponding numbers
days = {
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
    "Sunday": 7
}

# Function to get the day number from a given day name
def get_day_number(day_name):
    # Use the dictionary's get() method to retrieve the day number
    # If the day name is not found, return "Invalid day name"
    return days.get(day_name, "Invalid day name")

# Function to get the day name from a given day number
def get_day_name(day_number):
    # Iterate through the dictionary's items to find the day name
    # If the day number is not found, return "Invalid day number"
    for name, number in days.items():
        if number == day_number:
            return name
    return "Invalid day number"

# Main function to handle user input and interactions
def main():
    # Loop indefinitely until the user chooses to exit
    while True:
        # Display the menu options to the user
        print("Day of Week Menu:")
        print("1. Get day number")
        print("2. Get day name")
        print("3. Exit")
        
        # Get the user's choice from the menu
        choice = input("Enter your choice: ")

        # Handle the user's choice
        if choice == "1":
            # Ask the user to input a day name
            day_name = input("Enter a day name: ")
            # Call the get_day_number function and print the result
            print(get_day_number(day_name))
        elif choice == "2":
            # Ask the user to input a day number
            day_number = int(input("Enter a day number: "))
            # Call the get_day_name function and print the result
            print(get_day_name(day_number))
        elif choice == "3":
            # Exit the loop and end the program
            break
        else:
            # If the user's choice is not valid, print an error message
            print("Invalid choice. Please try again.")

# Check if the script is being run directly (not being imported)
if __name__ == "__main__":
    # Call the main function to start the program
    main()