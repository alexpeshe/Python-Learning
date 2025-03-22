# Get initial team data
team_name = input()           # Team name from user
games = int(input())         # Number of games played
score = 0                    # Initialize points counter
all_goals = 0               # Initialize goals scored
all_goals_received = 0      # Initialize goals conceded

# Process each game's data
for game in range(games):    
    goals = int(input())           # Goals scored this game
    goals_received = int(input())  # Goals conceded this game

    # Update running totals
    all_goals += goals            # Add to total goals scored
    all_goals_received += goals_received  # Add to total goals conceded

    # Calculate points based on game result
    if goals > goals_received:     # Win condition
        score += 3                 # 3 points for a win
    elif goals == goals_received:  # Draw condition
        score += 1                 # 1 point for a draw
                                  # (0 points for loss - implicit)

# Calculate final goal difference
diff = all_goals - all_goals_received    

# Determine team's fate based on goal difference
if all_goals >= all_goals_received:   # Team advances if scored >= conceded
    print(f"{team_name} has finished the phase with {score} points")
    print(f"Goals difference: {diff}")
else:                                 # Team eliminated if scored < conceded
    print(f"{team_name} has been eliminated")
    print(f"Goals difference: {diff}")
