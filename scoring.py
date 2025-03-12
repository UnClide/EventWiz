import json

# Initialize data structures with correct keys
data = {
    "teams": {},
    "individuals": [],
    "events": {
        "team_events": {},
        "individual_events": {}
    }
}

# Save data to data.json
def save_data():
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Data saved successfully!")

# Load data from data.json
def load_data():
    try:
        with open("data.json", "r") as f:
            loaded_data = json.load(f)
            # Ensure the structure is correct
            if not isinstance(loaded_data.get("teams", {}), dict):
                loaded_data["teams"] = {}
            if not isinstance(loaded_data.get("individuals", []), list):
                loaded_data["individuals"] = []
            if not isinstance(loaded_data.get("events", {}), dict):
                loaded_data["events"] = {"team_events": {}, "individual_events": {}}
            if not isinstance(loaded_data["events"].get("team_events", {}), dict):
                loaded_data["events"]["team_events"] = {}
            if not isinstance(loaded_data["events"].get("individual_events", {}), dict):
                loaded_data["events"]["individual_events"] = {}
            return loaded_data
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

# Delete team
def delete_team():
    team_name = input("Enter Team name to delete: ")
    if team_name in data["teams"]:
        del data["teams"][team_name]
        print(f"Team {team_name} deleted successfully!")
    else:
        print(f"Team {team_name} not found!")

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

# Delete individual
def delete_individual():
    individual_name = input("Enter Individual name to delete: ")
    if individual_name in data["individuals"]:
        data["individuals"].remove(individual_name)
        print(f"Individual {individual_name} deleted successfully!")
    else:
        print(f"Individual {individual_name} not found!")

# Add event
def add_event():
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
def delete_event():
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

# Assign team to event
def assign_team_to_event():
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

# Assign individual to event
def assign_individual_to_event():
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

# Main program loop
def main():
    global data
    data = load_data()

    while True:
        print("\nTournament Scoring System - EventWiz")
        print("1. Manage Teams")
        print("2. Manage Individuals")
        print("3. Manage Events")
        print("4. View Data")
        print("5. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            while True:
                print("\nManage Teams")
                print("1. Add Team")
                print("2. Delete Team")
                print("3. Assign Team to Event")
                print("4. Back to Main Menu")
                team_choice = input("Enter your choice: ")
                if team_choice == "1":
                    add_team()
                elif team_choice == "2":
                    delete_team()
                elif team_choice == "3":
                    assign_team_to_event()
                elif team_choice == "4":
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == "2":
            while True:
                print("\nManage Individuals")
                print("1. Add Individual")
                print("2. Delete Individual")
                print("3. Assign Individual to Event")
                print("4. Back to Main Menu")
                individual_choice = input("Enter your choice: ")
                if individual_choice == "1":
                    add_individual()
                elif individual_choice == "2":
                    delete_individual()
                elif individual_choice == "3":
                    assign_individual_to_event()
                elif individual_choice == "4":
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == "3":
            while True:
                print("\nManage Events")
                print("1. Add Event")
                print("2. Delete Event")
                print("3. Back to Main Menu")
                event_choice = input("Enter your choice: ")
                if event_choice == "1":
                    add_event()
                elif event_choice == "2":
                    delete_event()
                elif event_choice == "3":
                    break
                else:
                    print("Invalid choice. Please try again.")
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