Password Generator
The password generator is a simple tool that generates a random password based on the user's input. The
password generator takes the length of the password as input and generates a random password of that
length. The password is a combination of uppercase and lowercase letters, digits, and special characters.
The password generator uses the `random` module to generate random characters.

Instructions
The program will ask:

How many letters would you like in your password?
How many symbols would you like?
How many numbers would you like?
The objective is to take the inputs from the user to these questions and then generate a random password. Use your knowledge about Python lists and loops to complete the challenge.

Easy Version (Step 1)
Generate the password in sequence. If the user wants

4 letters
2 symbols and
3 numbers
then the password might look like this:

fgdx$*924
You can see that all the letters are together. All the symbols are together and all the numbers follow each other as well. Try to solve this problem first.

Hard Version (Step 2)
When you've completed the easy version, you're ready to tackle the hard version. In the advanced version of this project the final password does not follow a pattern. So the example above might look like this:

x$d24g*f9
And every time you generate a password, the positions of the symbols, numbers, and letters are different.

Solution