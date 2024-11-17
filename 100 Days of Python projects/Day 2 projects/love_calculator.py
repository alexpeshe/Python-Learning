# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name_1 = input("What is your name? \n")
name_2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# first thing we do is to use the combine string function and combine names 1 and 2, after that we turn it into a lower cases
combine_string = name_1 + name_2
lower_case_string = combine_string.lower()

#next thing we do is to use the count function for each letter and then add them all up
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

# the final part is to add both as and int and string
love_score = int(str(true)) + int(str(love))

#lastly, we use if/elif/else and the logical operators 
if (love_score <10) or (love_score > 90):
  print("Your score {love_score} makes you go like coke and mentos")
elif (love_score <40) or (love_score <50):
  print("Your score {love_score} means you are alright together")
else:
  print("Your score is {love_score}")