# Football Team Performance Calculator

"""
This program calculates a football team's performance in a tournament, tracking points earned and goal difference. Let me explain the code with detailed comments:
"""

# Get input from the user
team = input()  # Name of the football team
games_played = int(input())  # Number of games the team played
score = 0  # Initialize the team's score (points) to 0

# Initialize counters for goals
all_goals = 0  # Total goals scored by the team
all_goals_received = 0  # Total goals received by the team

# Loop through each game to calculate statistics
for games in range(0, games_played):
    goals_scored = int(input())  # Goals scored by the team in this game
    goals_received = int(input())  # Goals received by the team in this game
    
    # Update the total goals
    all_goals += goals_scored
    all_goals_received += goals_received
    
    # Calculate points based on the result
    if goals_scored > goals_received:
        score += 3  # Win: team gets 3 points
    elif goals_scored == goals_received:
        score =+ 1  # IMPORTANT: This is a bug! Should be "score += 1" for a draw
        # The current code assigns 1 to score instead of adding 1 to it

# Calculate the goal difference
diff = all_goals - all_goals_received

# Display the results based on whether the team was eliminated
if all_goals >= all_goals_received:
    print(f"{team} has finished with {score} points.")
    print(f"Goal difference: {diff}.")
else:
    print(f"{team} has been eliminated in the group phase!")
    print(f"Goal difference: {diff}.")

# Concepts Learned

"""
Input Processing: The program takes user input for the team name, number of games, and the goals for each game.

Loop Iteration: A for loop is used to process each game's statistics.

Conditional Logic: if-elif-else statements are used to determine points based on game results and to display different messages based on the team's performance.

Accumulation Pattern: The program uses variables (all_goals, all_goals_received, score) to accumulate values across multiple iterations.

Arithmetic Operations: Addition and subtraction are used to calculate totals and differences.

String Formatting: F-strings are used to create readable output messages that include variable values.

Bug Identification: There's a critical bug in the code: score =+ 1 should be score += 1. The current code assigns 1 to the score variable instead of adding 1 to it, which means draws are not correctly counted.

Sports Scoring System: The program implements a standard football scoring system:

3 points for a win

1 point for a draw (though this is incorrectly implemented)

0 points for a loss

Logical Condition for Elimination: The program uses the condition all_goals >= all_goals_received to determine if the team advances or is eliminated, which is a simplified rule (typically advancement would be based on points and position in the group).

This program demonstrates how to track and calculate sports statistics across multiple games, though it contains a bug in the draw scoring that would need to be fixed for accurate results"""

