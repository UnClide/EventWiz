# Add event
def add_event(data, event_name, event_type):
    if event_type == "team":
        if event_name in data["events"]["team_events"]:
            return "Team event already exists!"
        elif not event_name:
            return "Event name cannot be empty!"
        else:
            data["events"]["team_events"][event_name] = []
            return f"Team event {event_name} added successfully!"
    elif event_type == "individual":
        if event_name in data["events"]["individual_events"]:
            return "Individual event already exists!"
        elif not event_name:
            return "Event name cannot be empty!"
        else:
            data["events"]["individual_events"][event_name] = []
            return f"Individual event {event_name} added successfully!"
    else:
        return "Invalid event type. Please enter 'team' or 'individual'."

# Delete event
def delete_event(data, event_name, event_type):
    if event_type == "team":
        if event_name in data["events"]["team_events"]:
            del data["events"]["team_events"][event_name]
            return f"Team event {event_name} deleted successfully!"
        else:
            return f"Team event {event_name} not found!"
    elif event_type == "individual":
        if event_name in data["events"]["individual_events"]:
            del data["events"]["individual_events"][event_name]
            return f"Individual event {event_name} deleted successfully!"
        else:
            return f"Individual event {event_name} not found!"
    else:
        return "Invalid event type. Please enter 'team' or 'individual'."

# Change event type
def change_event_type(data, event_name, old_event_type, new_event_type):
    if old_event_type == new_event_type:
        return "New event type must be different from the current type!"
    if old_event_type == "team" and event_name in data["events"]["team_events"]:
        event_data = data["events"]["team_events"].pop(event_name)
        data["events"]["individual_events"][event_name] = event_data
        return f"Event {event_name} changed from Team to Individual successfully!"
    elif old_event_type == "individual" and event_name in data["events"]["individual_events"]:
        event_data = data["events"]["individual_events"].pop(event_name)
        data["events"]["team_events"][event_name] = event_data
        return f"Event {event_name} changed from Individual to Team successfully!"
    else:
        return f"Event {event_name} not found in {old_event_type} events!"

# Utility function for input validation
def is_valid_input(input_str):
    return bool(input_str and input_str.strip())

# Utility function to update event names based on event type
def update_event_names(data, event_type):
    if event_type == "team":
        return list(data["events"]["team_events"].keys())
    elif event_type == "individual":
        return list(data["events"]["individual_events"].keys())
    else:
        return []  # Return an empty list if no valid type is selected