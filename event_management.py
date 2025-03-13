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