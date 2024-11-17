# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill +=25
#the else statement at the end of this block isn't really needed, if it's easeier to read it can be replaced by elif
if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill +=3

if extra_cheese == "Y":
  bill += 1

print(f"Yor bill is $ {bill}")
# do not forget to use the f before the string  
  