# Read the total number of students from input and convert to integer.
number_of_students = int(input())

#Initialize counters for each grade category.
#These variables track how many students fall into each range.

number_of_failed_students = 0 # For grades below 3.00 (fail)
number_of_avg_students = 0 # For grades between 3.00 and 3.99 (average)
number_of_good_students = 0 # For grades between 4.00 and 4.99 (good)
number_of_excellent_students = 0 # For grades 5.00 or above (top students)

# Variable to accumulate the sum of all grades for computing the average later.
total_result = 0

# Variable avg_grade will eventually hold the computed average grade.
avg_grade = 0

# Loop through each student's grade
for n in range(number_of_students):
# Input a grade as a float (supports decimal values) and add it to total_result.
    exam_grade = float(input())
    total_result += exam_grade

# Classify exam_grade into the appropriate category using if-elif-else.
    if exam_grade < 3:
    # If the grade is less than 3.00, increment the failed counter.
        number_of_failed_students += 1
    # Immediately calculate the percentage for failed students.
    # (number_of_failed_students * 100) / number_of_students gives the current percentage.
        failed = (number_of_failed_students * 100) / number_of_students
    # Print the result formatted to 2 decimal places.
        print(f"Fail: {failed:.2f} %")
    elif 3 <= exam_grade <= 3.99:
    # If the grade is between 3.00 and 3.99, increment the average counter.
        number_of_avg_students += 1
        avg = (number_of_avg_students * 100) / number_of_students
        print(f"Between 3.00 and 3.99: {avg:.2f} %")
    elif 4 <= exam_grade <= 4.99:
    # If the grade is between 4.00 and 4.99, increment the good counter.
        number_of_good_students += 1
        good = (number_of_good_students * 100) / number_of_students
        print(f"Between 4.00 and 4.99: {good:.2f} %")
    else:
    # For grades 5.00 and above, increment the top students counter.
        number_of_excellent_students += 1
        excellent = (number_of_excellent_students * 100) / number_of_students
        print(f"Top Students: {excellent:.2f} %")

# After processing all students, compute the overall average grade
avg_grade = total_result / number_of_students

# Print the average grade formatted to 2 decimal places.
print(f"Average: {avg_grade:.2f}")

"""
Key Concepts Learned:

Input & Conversion: Using input() and converting to int or float.

Accumulation: Adding each exam grade to a running total for average calculation.

Conditional Statements: Using if-elif-else and chained comparisons to classify each grade.

Percentage Calculation: Calculating percentages based on counts and the total.

Formatting Output: Using f-strings with :.2f to show two decimal places."""

# Original solution commented out

'''number_of_students = int(input())

number_of_failed_students = 0
number_of_avg_students = 0
number_of_good_students = 0
number_of_excellent_students = 0
total_result = 0
avg_grade = 0

for n in range(number_of_students):
    exam_grade = float(input())
    total_result += exam_grade

    if exam_grade <3:
        number_of_failed_students +=1
        failed = (number_of_failed_students*100)/number_of_students
        print(f"Fail: {failed:.2f} %")
    elif 3<= exam_grade <=3.99:
        number_of_avg_students += 1
        avg = (number_of_avg_students*100)/number_of_students
        print(f"Between 3.00 and 3.99: {avg:.2f} %")
    elif 4<= exam_grade <=4.99:
        number_of_good_students += 1
        good = (number_of_good_students*100)/number_of_students
        print(f"Between 4.00 and 4.99: {good:.2f} %")
    else:
        number_of_excellent_students += 1
        excellent = (number_of_excellent_students*100)/number_of_students
        print(f"Top Students: {excellent:.2f} %")


avg_grade = total_result/number_of_students
print(f"Average: {avg_grade:.2f}")'''

# Improvement dictionary while loop suggestions by the o3 mini:

"""
students_count = int(input())

# Keys are category names and values are initialized to 0.

grade_categories = {
"Fail": 0, # For grades below 3.00
"Between 3.00 and 3.99": 0, # For grades between 3.00 and 3.99 (inclusive)
"Between 4.00 and 4.99": 0, # For grades between 4.00 and 4.99 (inclusive)
"Top students": 0 # For grades 5.00 or higher
}

# Variable to accumulate the sum of all exam grades for computing the average
total_result = 0

# Initialize a counter for the while loop
counter = 0

# Process all student grades using a while loop

while counter < students_count:

# Read a grade from input (converted to float as grades can be decimal values)
exam_grade = float(input())

Process
# Classify the exam_grade and update the corresponding dictionary entry.

# Add this grade to the running total for later calculation of the average grade
total_result += exam_grade

# Classify the exam grade into the appropriate category using chained comparisons.
if exam_grade < 3:
    grade_categories["Fail"] += 1
elif 3 <= exam_grade <= 3.99:
    grade_categories["Between 3.00 and 3.99"] += 1
elif 4 <= exam_grade <= 4.99:
    grade_categories["Between 4.00 and 4.99"] += 1
else:
    # This case covers exam_grade >= 5.00 (top students)
    grade_categories["Top students"] += 1

# Increment the counter to proceed to the next student
counter += 1

# After processing all grades, calculate the average grade.
average_grade = total_result / students_count

# Calculate the percentage for each category.
fail_percentage = (grade_categories["Fail"] / students_count) * 100
avg_percentage = (grade_categories["Between 3.00 and 3.99"] / students_count) * 100
good_percentage = (grade_categories["Between 4.00 and 4.99"] / students_count) * 100
top_percentage = (grade_categories["Top students"] / students_count) * 100

E Print the results in the order specified by the problem statement.
Each result is formatted to display two digits after the decimal point.
print(f"Top students: {top_percentage:.2f}%")
print(f"Between 4.00 and 4.99: {good_percentage:.2f}%")
print(f"Between 3.00 and 3.99: {avg_percentage:.2f}%")
print(f"Fail: {fail_percentage:.2f}%")
print(f"Average: {average_grade:.2f}")"
"""

'''
Key Points and Concepts Explained:

Input and Type Conversion:

The first input (students_count) is converted to an integer because it represents the total number of students.

Each subsequent input (the exam grade) is converted to a float to accommodate decimal values.

Dictionary Usage:

A dictionary named grade_categories stores the counts for different grade ranges. This makes the code cleaner and more scalable than using separate variables.

While Loop:

Instead of using a for loop, the while loop is employed here. It runs until the counter is equal to the number of students.

The counter variable is incremented after processing each student.

Grade Classification with Chained Comparisons:

The if-elif-else block uses chained comparisons (e.g., 3 <= exam_grade <= 3.99) to determine the category for each grade.

Each grade is evaluated and the corresponding dictionary entry is updated.

Accumulation and Percentage Calculation:

The variable total_result accumulates the sum of all grades for computing the average.

Percentages are calculated by dividing the count of each category by the total number of students and then multiplying by 100.

Output Formatting:

f-strings along with the format specifier :.2f ensure that the numeric output is formatted to two decimal places as required.

This solution is a clear and concise way to handle the problem using a dictionary and a while loop, illustrating several handy Python concepts.
'''

'''
Key Concepts and Explanations in the Alternative Approach:

Dictionary Usage:
  – A dictionary (grade_categories) groups the counts for each grade classification under descriptive keys.

While Loop:
  – A while loop is used to process a known number of inputs (students_count) by maintaining an external counter.

Input, Accumulation, & Conditional Logic:
  – Just like in your original solution, inputs are read, totals are accumulated, and conditions are checked using if-elif-else with chained comparisons.

Post-Processing Calculations:
  – All percentage calculations and the average grade are computed after processing all students, then printed in the required final format.

Output Formatting:
  – f-strings combined with :.2f ensure results are displayed with two decimal precision.

Both versions illustrate valuable Python concepts such as input handling, loops, dictionaries, accumulation, conditional logic, and formatted printing. You can choose the approach that best fits the context or your preference for organizing data.'''