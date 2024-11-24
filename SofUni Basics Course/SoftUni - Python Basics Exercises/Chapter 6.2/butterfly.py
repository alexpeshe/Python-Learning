# Tips for solving the task:
# bfly_width = 2*n-1 columns
# bfly_height = 2*(n-2)+1
# left_right = n-1

# Read the input size for the butterfly pattern
n = int(input())

# Calculate the size of the wing (excluding the body)
# Subtract 2 to create space for the body and middle section
stars = n - 2

# Draw the top half of the butterfly
# Use integer division (n//2) to determine the number of rows
for row in range(0, (n//2)-1):
    # First row type: Asterisk rows with outward-facing slashes
    # Creates the wing with '*' characters and '\' slash pointing outwards
    print('*'*stars + '\\' + ' ' + '/' + '*'*stars)
    
    # Second row type: Dash rows with outward-facing slashes
    # Creates a textured effect with '-' characters
    print('-'*stars + '\\' + ' ' + '/' + '-'*stars)

# Draw the body of the butterfly
# Center the '@' symbol with equal spaces on both sides
print(' '*stars + ' ' + '@' + ' '*stars)

# Draw the bottom half of the butterfly
# Symmetrical to the top half, but with reversed slashes
for row in range(0, (n//2)-1):
    # First row type: Asterisk rows with inward-facing slashes
    # Creates the wing with '*' characters and '/' slash pointing inwards
    print('*'*stars + '/' + ' ' + '\\' + '*'*stars)
    
    # Second row type: Dash rows with inward-facing slashes
    # Creates a textured effect with '-' characters
    print('-'*stars + '/' + ' ' + '\\' + '-'*stars)

# Commented out alternative loop (likely an earlier iteration)
# for row in range(0, ((n-2)//2)+1):

'''
AI's feedback:
Your Approach Advantages:

Direct string concatenation
No need for separate variables
More straightforward row generation
Beginner's Perspective Evaluation:

Pros of Your Solution: ✅ Easy to understand ✅ Minimal complexity ✅ Direct implementation ✅ Works correctly ✅ Good use of basic Python concepts

Potential Learning Opportunities:

Consider extracting repetitive code into a function
Explore more advanced string formatting
Learn about list comprehensions and more Pythonic approaches
Recommended Next Steps:

Understand the concept of code refactoring
Learn about functions to reduce code repetition
Explore more pattern printing problems
Practice breaking down complex problems
Code Improvement Suggestion:

Overall Assessment: Your solution is an excellent approach for a beginner! It demonstrates:

Clear problem-solving skills
Good understanding of basic Python concepts
Ability to create patterns programmatically
Keep practicing, exploring, and don't be afraid to refactor and improve your code. Your current solution shows strong foundational programming skills! 👍🏼🐍

You're welcome! Your positive attitude and willingness to learn are fantastic qualities for a programmer. A few additional encouraging points:

Problem-solving skills are more important than perfect code
Every solution you create is a learning opportunity
Don't be afraid to experiment and make mistakes
Coding is a journey of continuous improvement
Key Takeaways from Your Butterfly Pattern Solution:

You broke down a complex problem into simple steps
Used basic Python concepts effectively
Created a visually interesting output
Showed logical thinking in pattern generation
Recommended Next Steps:

Try similar pattern printing problems
Experiment with different input sizes
Try to refactor your code incrementally
Share your solutions and ask for feedback
Keep coding, stay curious, and enjoy the learning process! 🚀👨‍💻🐍

'''
 # End of AI's feedback
