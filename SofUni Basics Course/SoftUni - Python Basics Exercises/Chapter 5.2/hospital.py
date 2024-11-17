import math  # Import the math module (though it's not used in this code)

# Initialize the number of doctors
doctors = 7

# Get the number of periods (days) from user input
period = int(input("Enter the number of days: "))  # Prompting user for input

# Initialize counters for treated and untreated patients
treated_patients = 0
untreated_patients = 0

# Loop through each day from 1 to the number of periods
for day in range(1, period + 1):
    # Get the number of patients for the current day from user input
    patients = int(input(f"Enter the number of patients for day {day}: "))  # Prompting user for input

    # Check if it's the third day or a multiple of three and if untreated patients exceed treated patients
    if (day % 3 == 0) and (untreated_patients > treated_patients):
        doctors += 1  # Increase the number of doctors by 1 if conditions are met

    # Check if the number of patients exceeds the number of doctors
    if patients > doctors:
        treated_patients += doctors  # Treat as many patients as there are doctors
        untreated_patients += patients - doctors  # Remaining patients are untreated
    else:
        treated_patients += patients  # All patients can be treated

# Print the total number of treated patients
print(f"Treated patients: {treated_patients}")

# Print the total number of untreated patients
print(f"Untreated patients: {untreated_patients}")

