import json

data = {
    "teams": {},
    "individuals": {},
    "events": {},
}

# Save data to data.json
def save_data():
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Data saved successfully!")

#Load data from data.json
def load_data():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("No data found. Starting with empty data.")
        return data

# Add team
def add_team():
    team_name = input("Enter Team name: ")
    if team_name in data["teams"]:
        print("Team already exists!")
    elif not team_name:
        print("Team name cannot be empty!")
    else:
        data["teams"][team_name] = []
        print(f"Team {team_name} added successfully!")

# Add individual
def add_individual():
    individual_name = input("Enter Individual name: ")
    if not individual_name:
        print("Individual name cannot be empty!")
    else:
        choice = input("Do you want to add this individual to a team? (y/n): ").lower()
        if choice == "y":
            team_name = input("Enter Team name: ")
            if team_name in data["teams"]:
                data["teams"][team_name].append(individual_name)
                print(f"Individual {individual_name} added to Team {team_name} successfully!")
            else:
                print(f"Team {team_name} not found!")
        else:
            data["individuals"].append(individual_name)
            print(f"Participant {individual_name} added successfully as an individual!")

# Add event
def add_event():
    event_name = input("Enter Event name: ")
    if event_name in data["events"]:
        print("Event already exists!")
    elif not event_name:
        print("Event name cannot be empty!")
    else:
        data["events"][event_name] = {}
        print(f"Event {event_name} added successfully!")

# Main program loop
def main():
    global data
    data = load_data()

    while True:
        print("\nToutnament Scoring System - EventWiz")
        print("1. Add Team")
        print("2. Add Individual")
        print("3. Add Event")
        print("4. View Data")
        print("5. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_team()
        elif choice == "2":
            add_individual()
        elif choice == "3":
            add_event()
        elif choice == "4":
            print("\nCurrent Data:")
            print(json.dumps(data, indent=4))
        elif choice == "5":
            save_data()
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

#Old part of the code
"""teams = []
participants = []
events = []

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
    print(f"{participant}: {score} points")"""