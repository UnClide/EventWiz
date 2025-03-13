# Add event
def add_event(data):
    event_name = input("Enter Event name: ")
    event_type = input("Is this a team event or an individual event? (team/individual): ").lower()
    if event_type == "team":
        if event_name in data["events"]["team_events"]:
            print("Team event already exists!")
        elif not event_name:
            print("Event name cannot be empty!")
        else:
            data["events"]["team_events"][event_name] = []
            print(f"Team event {event_name} added successfully!")
    elif event_type == "individual":
        if event_name in data["events"]["individual_events"]:
            print("Individual event already exists!")
        elif not event_name:
            print("Event name cannot be empty!")
        else:
            data["events"]["individual_events"][event_name] = []
            print(f"Individual event {event_name} added successfully!")
    else:
        print("Invalid event type. Please enter 'team' or 'individual'.")

# Delete event
def delete_event(data):
    event_name = input("Enter Event name to delete: ")
    event_type = input("Is this a team event or an individual event? (team/individual): ").lower()
    if event_type == "team":
        if event_name in data["events"]["team_events"]:
            del data["events"]["team_events"][event_name]
            print(f"Team event {event_name} deleted successfully!")
        else:
            print(f"Team event {event_name} not found!")
    elif event_type == "individual":
        if event_name in data["events"]["individual_events"]:
            del data["events"]["individual_events"][event_name]
            print(f"Individual event {event_name} deleted successfully!")
        else:
            print(f"Individual event {event_name} not found!")
    else:
        print("Invalid event type. Please enter 'team' or 'individual'.")