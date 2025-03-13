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
    else:
        return f"Individual {individual_name} not found!"

# Assign individual to event
def assign_individual_to_event(data):
    individual_name = input("Enter Individual name: ")
    if individual_name not in data["individuals"]:
        print(f"Individual {individual_name} not found!")
        return

    event_name = input("Enter Event name: ")
    if event_name not in data["events"]["individual_events"]:
        print(f"Individual event {event_name} not found!")
        return

    data["events"]["individual_events"][event_name].append(individual_name)
    print(f"Individual {individual_name} assigned to Individual event {event_name} successfully!")