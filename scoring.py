import json

teams = []
participants = []
events = []
individuals = []

# Add teams 
teams.append(input("Enter Team 1 name: "))
teams.append(input("Enter Team 2 name: "))
teams.append(input("Enter Team 3 name: "))
teams.append(input("Enter Team 4 name: "))

# Add participants 
for i in range(20):
    participants.append(input(f"Enter Participant {i+1} name: "))

# Input event results 
event_results = {
    "Event 1": {"Team 1": 1, "Team 2": 2},
    "Event 2": {"Participant1": 1, "Participant2": 2},
}

# Calculate scores
scores = {}
for event, rankings in event_results.items():
    for participant, rank in rankings.items():
        if participant not in scores:
            scores[participant] = 0
        if rank == 1:
            scores[participant] += 10
        elif rank == 2:
            scores[participant] += 7
        elif rank == 3:
            scores[participant] += 5

# Display leaderboard
print("Leaderboard:")
for participant, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
    print(f"{participant}: {score} points")