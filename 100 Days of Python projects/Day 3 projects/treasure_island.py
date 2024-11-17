print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print('Welcome to the Trasure Island!')
print('Your mission is to find the treasure!!!')

#Check this link: https://medium.com/paul-zhao-projects/python-100-projects-in-100-days-learning-journal-17c913e5a6f9


#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choice1 = input('You are at a cross road. You have an important choice ahead of you? Type "left" or "right" ')
choice1_lowercase = choice1.lower()
# It is very important to use the input() functionin order to be able to execute the player's answer
# The second important thing to be taken is the use of the .lower() ( question.lower()) function in order to make the code accept any type of answer e.g. Left/Left/LEFT etc. Also the questions to be asked in the game can be simply inputed as question1 or anything for it to matter followed by the input function. 
if choice1_lowercase == "left":
  choice2 = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across ')
  choice2_lowercase = choice2.lower()
  if choice2_lowercase == "wait":
   choice3 = input('You arrive at the island unharmed. There is a castle with 3 doors. First one is red, the second yellow and the last is blue. Which door do you choose? Type "red", "yellow" or "blue" ')
   choice3_lowercase = choice3.lower()
   if choice3_lowercase == "yellow":
      print("You foud the trasure! You Win!")
   elif choice3_lowercase == "blue":
      print("Game Over. You get bitten by the Basilisks!")
   elif choice3_lowercase == "red":
    print("Game Over. You face the Minotaur!")
else:
  print("Game Over. You get eaten by Cerberus!")


# another important thing to take a note of is the logical flow!
# in thos case the first question wraps up the other two, where they become more indented the further you expand.


  
# With my original code it was wrong to combine print and input functions 
# Secondly, I didn't start correctly with choice1/2/3 = input() followed by choice = choice.lower()
# in regard to the blocks of code, it was wrong trying to separate them like I did here check the proper code below.
'''print(input('Where do you go? Left or Right?: ')
	if choice1 == Right:
		print('Very sad, Game Over!)
	elif choice2 == Left:
		print('Very good, you may continue)

print(input('Do you Swim or Wait?: ')
	if choice3 == 'Swim':
		print('Too bad, you get eaten by a shark!)
	elif choice4 == 'Wait':
print('Very nice, you may continue to the doors')

print(input('Which door do you pick?:') 
	if choice 5 == 'Yellow':
		print('You found the treasure')
	elif choice6 == 'Red':
		print('So sad, Game Over!')
	else:
		print('Wrong again! Game Over!!!') '''
