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
    data["teams"][team_name].append(individual_name)
    data["individuals"].remove(individual_name)
    return f"Assigned {individual_name} to Team {team_name} successfully!"

# Utility function for input validation
def is_valid_input(input_str):
    return bool(input_str and input_str.strip())