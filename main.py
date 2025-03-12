import json

from data_management import load_data, save_data
from team_management import add_team, delete_team, assign_team_to_event
from individual_management import add_individual, delete_individual, assign_individual_to_event
from event_management import add_event, delete_event

# Main program loop
def main():
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
                    add_team(data)
                elif team_choice == "2":
                    delete_team(data)
                elif team_choice == "3":
                    assign_team_to_event(data)
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
                    add_individual(data)
                elif individual_choice == "2":
                    delete_individual(data)
                elif individual_choice == "3":
                    assign_individual_to_event(data)
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
                    add_event(data)
                elif event_choice == "2":
                    delete_event(data)
                elif event_choice == "3":
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == "4":
            print("\nCurrent Data:")
            print(json.dumps(data, indent=4))
        elif choice == "5":
            save_data(data)
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()