# on_time_for_the_exam.py

# Get input from user for exam time and arrival time
exam_hour = int(input())
exam_minute = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())

# Define status constants
late = 'Late'
on_time = 'Ontime'
early = 'Early'

# Convert both times to minutes for easier comparison
exam_time = (exam_hour*60) + exam_minute  # Convert exam time to total minutes
arrival_time = (hour_of_arrival*60) + minute_of_arrival  # Convert arrival time to total minutes
total_difference = arrival_time - exam_time  # Calculate time difference (negative means early, positive means late)

# Set default status as late
student_arrival = late

# Determine if student is early, on time, or late
if total_difference < -30:  # If student arrived more than 30 minutes early
    student_arrival = early
elif total_difference <= 0:  # If student arrived up to 30 minutes early or exactly on time
    student_arrival = on_time

# Initialize empty result string for time difference message
result = ""

# Calculate and format the time difference message
if total_difference != 0:  # If student didn't arrive exactly on time
    # Calculate hours and minutes from the total time difference
    hours_difference = abs(total_difference) // 60  # Get whole hours
    minutes_difference = abs(total_difference) % 60  # Get remaining minutes

    # Format the time difference string
    if hours_difference > 0:  # If difference is 1 hour or more
        result = f"{hours_difference}:{minutes_difference:02} hours"
    else:  # If difference is less than 1 hour
        result = f"{minutes_difference} minutes"

    # Add appropriate suffix based on whether student was early or late
    if total_difference < 0:
        result += " before the start"
    else:
        result += "after the start"
    
    # Print the final results
    print(student_arrival)  # Print arrival status (Early, On time, or Late)
    if result:  # Print time difference if there is one
        print(result)


'''
Original program:

exam_hour = int(input())
exam_minute = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())

late = 'Late'
on_time = 'Ontime'
early = 'Early'

exam_time = (exam_hour*60) + exam_minute
arrival_time = (hour_of_arrival*60) + minute_of_arrival
total_difference = arrival_time - exam_time

student_arrival = late

if total_difference < -30:
    student_arrival = early
elif total_difference <= 0:
    student_arrival = on_time


result = ""

if total_difference != 0:
    hours_difference = abs(total_difference) // 60
    minutes_difference = abs(total_difference) % 60

    if hours_difference > 0:
        result = \
        f"{hours_difference}:{minutes_difference:02} hours"
    else:
        result = f"{minutes_difference} minutes"

    if total_difference < 0:
        result += " before the start"
    else:
        result += "after the start"
    
    print(student_arrival)
    if result:
        print(result)
'''