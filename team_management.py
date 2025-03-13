# Add team
def add_team(data, team_name):
    if team_name in data["teams"]:
        return "Team already exists!"
    elif not team_name:
        return "Team name cannot be empty!"
    else:
        data["teams"][team_name] = []
        return f"Team {team_name} added successfully!"

# Delete team
def delete_team(data, team_name):
    if team_name in data["teams"]:
        del data["teams"][team_name]
        return f"Team {team_name} deleted successfully!"
    else:
        return f"Team {team_name} not found!"

# Assign team to event
def assign_team_to_event(data):
    team_name = input("Enter Team name: ")
    if team_name not in data["teams"]:
        print(f"Team {team_name} not found!")
        return

    event_name = input("Enter Event name: ")
    if event_name not in data["events"]["team_events"]:
        print(f"Team event {event_name} not found!")
        return

    data["events"]["team_events"][event_name].append(team_name)
    print(f"Team {team_name} assigned to Team event {event_name} successfully!")