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
def assign_team_to_event(data, team_name, event_name):
    if team_name not in data["teams"]:
        return f"Team {team_name} not found!"
    if event_name not in data["events"]["team_events"]:
        return f"Team event {event_name} not found!"
    data["events"]["team_events"][event_name].append(team_name)
    return f"Team {team_name} assigned to Team event {event_name} successfully!"