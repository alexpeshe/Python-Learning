print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))
bill = 0
#the height's number has to be inputed as integer
# in order to add aditional money to their ticket we create a new value of bill = 0 
if height >= 120:
  print("You can ride on the rollercoaster")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child ticket is: $5")
  elif age <= 18:
    bill = 7
    print("Youth ticket is: $7")
  elif age >= 45 and age <= 50:
    print("Everything is gonna be okay. Have a free ride on us.")
    #in order to achive this we use the and statement where both conditions need to be true.
  else: 
    bill = 12
    print("Adult ticket is: $12")

  wants_photo = input("Do you want a photo taken? Y or N ")
  if wants_photo == "Y":
    bill += 3
  # this is the shorter way of writing this type of addition to the bill instead of bill = bill + 3
# it is also important to note that all the lines from 6 to 21 are part of the same block
  print(f"Your final bill is {bill}")

else: 
  print("Sorry you'll have to grow up before you can ride.")

#when inserting the if and else functions the print functions underneath must be written with two indented spaces infron of them. In order for this code to work indentation matters most!!