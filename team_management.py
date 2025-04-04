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

# Assign individual to team
def assign_individual_to_team(data, individual_name, team_name):
    if team_name not in data["teams"]:
        return f"Team {team_name} not found!"
    if individual_name not in data["individuals"]:
        return f"Individual {individual_name} not found!"

    # Check if the individual is already in another team
    for other_team, members in data["teams"].items():
        if individual_name in members:
            if other_team == team_name:
                return f"Individual {individual_name} is already in Team {team_name}!"
            else:
                return f"Individual {individual_name} is already in Team {other_team}. Remove them first before assigning to Team {team_name}."

    # Assign the individual to the team
    data["teams"][team_name].append(individual_name)
    return f"Assigned {individual_name} to Team {team_name} successfully!"

# Remove individual from team
def remove_individual_from_team(data, individual_name):
    for team_name, members in data["teams"].items():
        if individual_name in members:
            members.remove(individual_name)
            return f"Individual {individual_name} removed from Team {team_name} successfully!"
    return f"Individual {individual_name} is not assigned to any team!"

# Utility function for input validation
def is_valid_input(input_str):
    return bool(input_str and input_str.strip())