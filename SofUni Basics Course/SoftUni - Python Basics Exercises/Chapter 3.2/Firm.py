import math

# The Input variables
project_hours = int(input())
available_days = int(input())
overtime_workers = int(input())

# Calculate effective workdays (90% due to training)
work_days = available_days * 0.9
# Calculate total work hours (8 hours per day plus 2 hours of overtime per worker)
overtime_hours = (overtime_workers * 2) * work_days
work_hours = (work_days * 8) + overtime_hours
# Total working hours available (normal work + overtime)
total_workhours = math.floor(work_hours + overtime_hours)

# Check if the total working hours are enough for the project
if total_workhours >= project_hours:
    hours_left = total_workhours - project_hours
    print(f"Yes!{hours_left} hours left." .format(hours_left))
else:
    additional_hours_needed = project_hours - total_workhours
    print(f"Not enough time!{additional_hours_needed} hours needed." .format(additional_hours_needed))
