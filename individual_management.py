# Add individual
def add_individual(data, individual_name, team_name=None):
    if not individual_name:
        return "Individual name cannot be empty!"
    else:
        if team_name:
            if team_name in data["teams"]:
                data["teams"][team_name].append(individual_name)
                return f"Individual {individual_name} added to Team {team_name} successfully!"
            else:
                return f"Team {team_name} not found!"
        else:
            data["individuals"].append(individual_name)
            return f"Participant {individual_name} added successfully as an individual!"

# Delete individual
def delete_individual(data, individual_name):
    if individual_name in data["individuals"]:
        data["individuals"].remove(individual_name)
        return f"Individual {individual_name} deleted successfully!"
    for team, members in data["teams"].items():
        if individual_name in members:
            members.remove(individual_name)
            return f"Individual {individual_name} removed from Team {team} and deleted successfully!"
    return f"Individual {individual_name} not found!"

# Assign individual to event
def assign_individual_to_event(data, individual_name, event_name):
    if individual_name not in data["individuals"]:
        return f"Individual {individual_name} not found!"
    if event_name not in data["events"]["individual_events"]:
        return f"Individual event {event_name} not found!"
    data["events"]["individual_events"][event_name].append(individual_name)
    return f"Individual {individual_name} assigned to Individual event {event_name} successfully!"