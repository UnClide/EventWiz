import json

# Initialize data structures with correct keys
initial_data = {
    "teams": {},
    "individuals": [],
    "events": {
        "team_events": {},
        "individual_events": {}
    }
}

# Save data to data.json
def save_data(data):
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
        return initial_data