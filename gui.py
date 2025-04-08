import json
import tkinter as tk
from tkinter import messagebox, StringVar, Text, simpledialog, filedialog
from tkinter import ttk
from data_management import load_data, save_data
from team_management import add_team, delete_team, assign_team_to_event, is_valid_input, assign_individual_to_team, remove_individual_from_team
from individual_management import add_individual, delete_individual, assign_individual_to_event
from event_management import add_event, delete_event, change_event_type, update_event_names, remove_individual_from_event
from scoring_management import assign_individual_score, assign_team_member_score, determine_winners, export_results

class TournamentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EventWiz")
        self.root.geometry("450x550")
        self.root.configure(bg="#E3E3E3")

        # Restrict size of the program window
        self.root.minsize(300, 480)
        
        # Load data from data.json
        self.data = load_data()
        
        # Ensure 'scores' key is initialized in the data structure
        if "scores" not in self.data:
            self.data["scores"] = {"individual_scores": {}, "team_scores": {}}
        
        # Configure styles for the UI elements
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", font=("Segoe UI", 10), padding=6, borderwidth=0, relief="flat", background="#C0C0C0", foreground="black")
        style.map("TButton", background=[("active", "#A9A9A9")])
        style.configure("TLabel", font=("Segoe UI", 12), background="#E3E3E3")
        
        # Title label
        self.title_label = ttk.Label(root, text="Tournament Scoring System", font=("Segoe UI", 16, "bold"))
        self.title_label.pack(pady=10)
        
        # Frame for buttons
        self.button_frame = ttk.Frame(root)
        self.button_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        # Buttons for various actions
        self.main_buttons = [
            ("Manage Teams", self.manage_teams),
            ("Manage Individuals", self.manage_individuals),
            ("Manage Events", self.manage_events),
            ("Manage Scores", self.manage_scores),
            ("View Data", self.view_data),
            ("Save Data", self.save_data)
        ]
        
        # Create and pack buttons
        for text, command in self.main_buttons:
            btn = ttk.Button(self.button_frame, text=text, command=command, width=25)
            btn.pack(pady=5)

    def clear_frame(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()

    def show_main_menu(self):
        self.clear_frame()
        for text, command in self.main_buttons:
            btn = ttk.Button(self.button_frame, text=text, command=command, width=25)
            btn.pack(pady=5)

    def add_team(self):
        team_name = simpledialog.askstring("Add Team", "Enter Team name:")
        if team_name is None:
            return
        if is_valid_input(team_name):  # Updated to use the imported function
            result = add_team(self.data, team_name)
            messagebox.showinfo("Result", result)
        else:
            messagebox.showerror("Error", "Team name cannot be empty!")

    def add_individual(self):
        self.clear_frame()
        ttk.Label(self.button_frame, text="Enter Individual name:").pack(pady=5)
        individual_name_var = StringVar()
        individual_entry = ttk.Entry(self.button_frame, textvariable=individual_name_var)
        individual_entry.pack(pady=5)

        ttk.Label(self.button_frame, text="Select Team (optional):").pack(pady=5)
        team_name_var = StringVar()
        team_dropdown = ttk.Combobox(self.button_frame, textvariable=team_name_var, values=list(self.data["teams"].keys()), state="readonly")
        team_dropdown.pack(pady=5)

        def confirm_add_individual():
            individual_name = individual_name_var.get()
            team_name = team_name_var.get()
            if not is_valid_input(individual_name):  # Updated to use the imported function
                messagebox.showerror("Error", "Individual name cannot be empty!")
                return
            if team_name:
                result = add_individual(self.data, individual_name, team_name)
            else:
                result = add_individual(self.data, individual_name)
            messagebox.showinfo("Result", result)
            self.show_main_menu()

        ttk.Button(self.button_frame, text="Confirm", command=confirm_add_individual).pack(pady=10)
        ttk.Button(self.button_frame, text="Back to Main Menu", command=self.show_main_menu).pack(pady=5)

    def add_event(self):
        self.clear_frame()
        ttk.Label(self.button_frame, text="Enter Event name:").pack(pady=5)
        event_name_var = StringVar()
        event_entry = ttk.Entry(self.button_frame, textvariable=event_name_var)
        event_entry.pack(pady=5)

        ttk.Label(self.button_frame, text="Select Event type:").pack(pady=5)
        event_type_var = StringVar()
        event_type_var.set("team")
        event_dropdown = ttk.Combobox(self.button_frame, textvariable=event_type_var, values=["team", "individual"], state="readonly")
        event_dropdown.pack(pady=5)

        def confirm_event():
            event_name = event_name_var.get()
            if not is_valid_input(event_name):  # Updated to use the imported function
                messagebox.showerror("Error", "Event name cannot be empty!")
                return
            result = add_event(self.data, event_name, event_type_var.get())
            messagebox.showinfo("Result", result)
            self.show_main_menu()

        ttk.Button(self.button_frame, text="Confirm", command=confirm_event).pack(pady=10)
        ttk.Button(self.button_frame, text="Back to Main Menu", command=self.show_main_menu).pack(pady=5)

    def save_data(self):
        save_data(self.data)
        messagebox.showinfo("Success", "Data saved successfully!")

    def view_data(self):
        self.clear_frame()
        data_text = Text(self.button_frame, height=20, width=50)
        data_text.pack(padx=10, pady=10)
        data_text.insert(tk.END, json.dumps(self.data, indent=4))
        data_text.config(state=tk.DISABLED)
        ttk.Button(self.button_frame, text="Back to Main Menu", command=self.show_main_menu).pack(pady=5)

    def manage_teams(self):
        self.clear_frame()
        buttons = [
            ("Add Team", self.add_team),
            ("Delete Team", self.delete_team),
            ("Edit Team Assignments", self.edit_team_assignments),
            ("Back to Main Menu", self.show_main_menu)
        ]
        for text, command in buttons:
            btn = ttk.Button(self.button_frame, text=text, command=command, width=25)
            btn.pack(pady=5)

    def manage_individuals(self):
        self.clear_frame()
        buttons = [
            ("Add Individual", self.add_individual),
            ("Delete Individual", self.delete_individual),
            ("Edit Individual Assignments", self.edit_individual_assignments),
            ("Back to Main Menu", self.show_main_menu)
        ]
        for text, command in buttons:
            btn = ttk.Button(self.button_frame, text=text, command=command, width=25)
            btn.pack(pady=5)

    def manage_events(self):
        self.clear_frame()
        buttons = [
            ("Add Event", self.add_event),
            ("Delete Event", self.delete_event),
            ("Edit Event Assignments", self.edit_event_assignments),
            ("Back to Main Menu", self.show_main_menu)
        ]
        for text, command in buttons:
            btn = ttk.Button(self.button_frame, text=text, command=command, width=25)
            btn.pack(pady=5)

    def delete_team(self):
        self.clear_frame()
        ttk.Label(self.button_frame, text="Select Team to delete:").pack(pady=5)
        team_name_var = StringVar()
        team_dropdown = ttk.Combobox(self.button_frame, textvariable=team_name_var, values=list(self.data["teams"].keys()), state="readonly")
        team_dropdown.pack(pady=5)

        def confirm_delete_team():
            team_name = team_name_var.get()
            if team_name:
                result = delete_team(self.data, team_name)
                messagebox.showinfo("Result", result)
            self.show_main_menu()

        ttk.Button(self.button_frame, text="Confirm", command=confirm_delete_team).pack(pady=10)
        ttk.Button(self.button_frame, text="Back to Main Menu", command=self.show_main_menu).pack(pady=5)

    def delete_individual(self):
        self.clear_frame()
        ttk.Label(self.button_frame, text="Select Individual to delete:").pack(pady=5)
        all_individuals = self.data["individuals"] + [ind for team in self.data["teams"].values() for ind in team]
        individual_name_var = StringVar()
        individual_dropdown = ttk.Combobox(self.button_frame, textvariable=individual_name_var, values=all_individuals, state="readonly")
        individual_dropdown.pack(pady=5)

        def confirm_delete_individual():
            individual_name = individual_name_var.get()
            if individual_name:
                result = delete_individual(self.data, individual_name)
                messagebox.showinfo("Result", result)
            self.show_main_menu()

        ttk.Button(self.button_frame, text="Confirm", command=confirm_delete_individual).pack(pady=10)
        ttk.Button(self.button_frame, text="Back to Main Menu", command=self.show_main_menu).pack(pady=5)

    def delete_event(self):
        self.clear_frame()
        ttk.Label(self.button_frame, text="Select Event type:").pack(pady=5)
        event_type_var = StringVar()
        event_type_var.set("")  # Set to empty initially to avoid pre-selection
        event_type_dropdown = ttk.Combobox(self.button_frame, textvariable=event_type_var, values=["team", "individual"], state="readonly")
        event_type_dropdown.pack(pady=5)

        ttk.Label(self.button_frame, text="Select Event to delete:").pack(pady=5)
        event_name_var = StringVar()
        event_name_dropdown = ttk.Combobox(self.button_frame, textvariable=event_name_var, state="readonly")
        event_name_dropdown.pack(pady=5)

        def update_event_names(*args):
            event_type = event_type_var.get()
            if event_type == "team":
                event_name_dropdown["values"] = list(self.data["events"]["team_events"].keys())
            elif event_type == "individual":
                event_name_dropdown["values"] = list(self.data["events"]["individual_events"].keys())
            else:
                event_name_dropdown["values"] = []  # Clear dropdown if no type is selected

        event_type_var.trace("w", update_event_names)

        def confirm_delete_event():
            event_name = event_name_var.get()
            event_type = event_type_var.get()
            if event_name and event_type:
                result = delete_event(self.data, event_name, event_type)
                messagebox.showinfo("Result", result)
            self.show_main_menu()

        ttk.Button(self.button_frame, text="Confirm", command=confirm_delete_event).pack(pady=10)
        ttk.Button(self.button_frame, text="Back to Main Menu", command=self.show_main_menu).pack(pady=5)

    def change_event_type(self):
        self.clear_frame()
        ttk.Label(self.button_frame, text="Select Event type to change:").pack(pady=5)
        event_type_var = StringVar()
        event_type_var.set("")  # Set to empty initially to avoid pre-selection
        event_type_dropdown = ttk.Combobox(self.button_frame, textvariable=event_type_var, values=["team", "individual"], state="readonly")
        event_type_dropdown.pack(pady=5)

        ttk.Label(self.button_frame, text="Select Event to change:").pack(pady=5)
        event_name_var = StringVar()
        event_name_dropdown = ttk.Combobox(self.button_frame, textvariable=event_name_var, state="readonly")
        event_name_dropdown.pack(pady=5)

        def on_event_type_change(*args):
            event_type = event_type_var.get()
            event_name_dropdown["values"] = update_event_names(self.data, event_type)  # Use the imported function

        event_type_var.trace("w", on_event_type_change)

        ttk.Label(self.button_frame, text="Select New Event type:").pack(pady=5)
        new_event_type_var = StringVar()
        new_event_type_dropdown = ttk.Combobox(self.button_frame, textvariable=new_event_type_var, values=["team", "individual"], state="readonly")
        new_event_type_dropdown.pack(pady=5)

        def confirm_change_event_type():
            event_name = event_name_var.get()
            old_event_type = event_type_var.get()
            new_event_type = new_event_type_var.get()
            if event_name and old_event_type and new_event_type:
                result = change_event_type(self.data, event_name, old_event_type, new_event_type)
                messagebox.showinfo("Result", result)
            else:
                messagebox.showerror("Error", "All fields must be selected!")
            self.show_main_menu()

        ttk.Button(self.button_frame, text="Confirm", command=confirm_change_event_type).pack(pady=10)
        ttk.Button(self.button_frame, text="Back to Main Menu", command=self.show_main_menu).pack(pady=5)

    def edit_individual_assignments(self):
        self.clear_frame()
        ttk.Label(self.button_frame, text="Select Individual:").pack(pady=5)
        individual_name_var = StringVar()
        individual_dropdown = ttk.Combobox(self.button_frame, textvariable=individual_name_var, values=self.data["individuals"], state="readonly")
        individual_dropdown.pack(pady=5)

        current_team_var = StringVar()
        current_event_var = StringVar()

        def load_assignments(*args):
            individual_name = individual_name_var.get()
            if not individual_name:
                return

            # Find current team
            for team_name, members in self.data["teams"].items():
                if individual_name in members:
                    current_team_var.set(team_name)
                    break
            else:
                current_team_var.set("")

            # Find current event
            for event_type, events in self.data["events"].items():
                for event_name, participants in events.items():
                    if individual_name in participants:
                        current_event_var.set(event_name)
                        break
                else:
                    continue
                break
            else:
                current_event_var.set("")

        individual_name_var.trace("w", load_assignments)

        ttk.Label(self.button_frame, text="Select Team:").pack(pady=5)
        team_dropdown = ttk.Combobox(self.button_frame, textvariable=current_team_var, values=list(self.data["teams"].keys()), state="readonly")
        team_dropdown.pack(pady=5)

        ttk.Label(self.button_frame, text="Select Event:").pack(pady=5)
        event_dropdown = ttk.Combobox(self.button_frame, textvariable=current_event_var, values=list(self.data["events"]["team_events"].keys()) + list(self.data["events"]["individual_events"].keys()), state="readonly")
        event_dropdown.pack(pady=5)

        def confirm_edit_assignments():
            individual_name = individual_name_var.get()
            new_team = current_team_var.get()
            new_event = current_event_var.get()

            if not individual_name:
                messagebox.showerror("Error", "Please select an individual!")
                return

            # Remove from current team and event
            remove_individual_from_team(self.data, individual_name)
            remove_individual_from_event(self.data, individual_name)

            # Assign to new team
            if new_team:
                assign_individual_to_team(self.data, individual_name, new_team)

            # Assign to new event
            if new_event:
                assign_individual_to_event(self.data, individual_name, new_event)

            messagebox.showinfo("Success", f"Assignments for {individual_name} updated successfully!")
            self.show_main_menu()

        def remove_from_team():
            individual_name = individual_name_var.get()
            if not individual_name:
                messagebox.showerror("Error", "Please select an individual!")
                return
            result = remove_individual_from_team(self.data, individual_name)
            messagebox.showinfo("Result", result)
            load_assignments()

        def remove_from_event():
            individual_name = individual_name_var.get()
            if not individual_name:
                messagebox.showerror("Error", "Please select an individual!")
                return
            result = remove_individual_from_event(self.data, individual_name)
            messagebox.showinfo("Result", result)
            load_assignments()

        ttk.Button(self.button_frame, text="Update Assignments", command=confirm_edit_assignments).pack(pady=10)
        ttk.Button(self.button_frame, text="Remove from Team", command=remove_from_team).pack(pady=5)
        ttk.Button(self.button_frame, text="Remove from Event", command=remove_from_event).pack(pady=5)
        ttk.Button(self.button_frame, text="Back to Main Menu", command=self.show_main_menu).pack(pady=5)

    def edit_event_assignments(self):
        self.clear_frame()
        ttk.Label(self.button_frame, text="Select Event Type:").pack(pady=5)
        event_type_var = StringVar()
        event_type_dropdown = ttk.Combobox(self.button_frame, textvariable=event_type_var, values=["team", "individual"], state="readonly")
        event_type_dropdown.pack(pady=5)

        ttk.Label(self.button_frame, text="Select Event:").pack(pady=5)
        event_name_var = StringVar()
        event_name_dropdown = ttk.Combobox(self.button_frame, textvariable=event_name_var, state="readonly")
        event_name_dropdown.pack(pady=5)

        def update_event_names(*args):
            event_type = event_type_var.get()
            if event_type == "team":
                event_name_dropdown["values"] = list(self.data["events"]["team_events"].keys())
            elif event_type == "individual":
                event_name_dropdown["values"] = list(self.data["events"]["individual_events"].keys())
            else:
                event_name_dropdown["values"] = []

        event_type_var.trace("w", update_event_names)

        ttk.Label(self.button_frame, text="Assigned Teams/Individuals:").pack(pady=5)
        assigned_listbox = tk.Listbox(self.button_frame, height=10, width=40)
        assigned_listbox.pack(pady=5)

        def load_assignments(*args):
            event_type = event_type_var.get()
            event_name = event_name_var.get()
            assigned_listbox.delete(0, tk.END)
            if event_type and event_name:
                participants = self.data["events"]["team_events" if event_type == "team" else "individual_events"].get(event_name, [])
                for participant in participants:
                    assigned_listbox.insert(tk.END, participant)

        event_name_var.trace("w", load_assignments)

        ttk.Label(self.button_frame, text="Add Team/Individual:").pack(pady=5)
        participant_var = StringVar()
        participant_dropdown = ttk.Combobox(self.button_frame, textvariable=participant_var, state="readonly")
        participant_dropdown.pack(pady=5)

        def update_participant_dropdown(*args):
            event_type = event_type_var.get()
            if event_type == "team":
                participant_dropdown["values"] = list(self.data["teams"].keys())
            elif event_type == "individual":
                participant_dropdown["values"] = self.data["individuals"]
            else:
                participant_dropdown["values"] = []

        event_type_var.trace("w", update_participant_dropdown)

        def add_participant():
            event_type = event_type_var.get()
            event_name = event_name_var.get()
            participant = participant_var.get()
            if not event_type or not event_name or not participant:
                messagebox.showerror("Error", "All fields must be selected!")
                return
            if event_type == "team":
                result = assign_team_to_event(self.data, participant, event_name)
            else:
                result = assign_individual_to_event(self.data, participant, event_name)
            messagebox.showinfo("Result", result)
            load_assignments()

        def remove_participant():
            event_type = event_type_var.get()
            event_name = event_name_var.get()
            selected = assigned_listbox.get(tk.ACTIVE)
            if not event_type or not event_name or not selected:
                messagebox.showerror("Error", "Please select a participant to remove!")
                return
            if event_type == "team":
                self.data["events"]["team_events"][event_name].remove(selected)
            else:
                self.data["events"]["individual_events"][event_name].remove(selected)
            messagebox.showinfo("Success", f"Removed {selected} from {event_name}.")
            load_assignments()

        ttk.Button(self.button_frame, text="Add Team/Individual", command=add_participant).pack(pady=5)
        ttk.Button(self.button_frame, text="Remove Team/Individual", command=remove_participant).pack(pady=5)
        ttk.Button(self.button_frame, text="Back to Main Menu", command=self.show_main_menu).pack(pady=5)

    def edit_team_assignments(self):
        self.clear_frame()
        ttk.Label(self.button_frame, text="Select Team:").pack(pady=5)
        team_name_var = StringVar()
        team_dropdown = ttk.Combobox(self.button_frame, textvariable=team_name_var, values=list(self.data["teams"].keys()), state="readonly")
        team_dropdown.pack(pady=5)

        ttk.Label(self.button_frame, text="Assigned Individuals:").pack(pady=5)
        assigned_listbox = tk.Listbox(self.button_frame, height=10, width=40)
        assigned_listbox.pack(pady=5)

        def load_assignments(*args):
            team_name = team_name_var.get()
            assigned_listbox.delete(0, tk.END)
            if team_name:
                members = self.data["teams"].get(team_name, [])
                for member in members:
                    assigned_listbox.insert(tk.END, member)

        team_name_var.trace("w", load_assignments)

        ttk.Label(self.button_frame, text="Add Individual:").pack(pady=5)
        individual_var = StringVar()
        individual_dropdown = ttk.Combobox(self.button_frame, textvariable=individual_var, values=self.data["individuals"], state="readonly")
        individual_dropdown.pack(pady=5)

        def add_member():
            team_name = team_name_var.get()
            individual = individual_var.get()
            if not team_name or not individual:
                messagebox.showerror("Error", "Both Team and Individual must be selected!")
                return
            result = assign_individual_to_team(self.data, individual, team_name)
            messagebox.showinfo("Result", result)
            load_assignments()

        def remove_member():
            team_name = team_name_var.get()
            selected = assigned_listbox.get(tk.ACTIVE)
            if not team_name or not selected:
                messagebox.showerror("Error", "Please select a member to remove!")
                return
            self.data["teams"][team_name].remove(selected)
            messagebox.showinfo("Success", f"Removed {selected} from {team_name}.")
            load_assignments()

        ttk.Label(self.button_frame, text="Assign Team to Event:").pack(pady=5)
        event_name_var = StringVar()
        event_dropdown = ttk.Combobox(self.button_frame, textvariable=event_name_var, values=list(self.data["events"]["team_events"].keys()), state="readonly")
        event_dropdown.pack(pady=5)

        def assign_team_to_event():
            team_name = team_name_var.get()
            event_name = event_name_var.get()
            if not team_name or not event_name:
                messagebox.showerror("Error", "Both Team and Event must be selected!")
                return
            result = assign_team_to_event(self.data, team_name, event_name)
            messagebox.showinfo("Result", result)

        ttk.Button(self.button_frame, text="Add Individual", command=add_member).pack(pady=5)
        ttk.Button(self.button_frame, text="Remove Individual", command=remove_member).pack(pady=5)
        ttk.Button(self.button_frame, text="Assign to Event", command=assign_team_to_event).pack(pady=5)
        ttk.Button(self.button_frame, text="Back to Main Menu", command=self.show_main_menu).pack(pady=5)

    # Add a button to remove scores in 'Manage Scores'
    def manage_scores(self):
        self.clear_frame()

        # Add live leaderboard
        leaderboard_frame = ttk.Frame(self.button_frame)
        leaderboard_frame.pack(side=tk.LEFT, padx=10, pady=10, fill="y")
        ttk.Label(leaderboard_frame, text="Leaderboard", font=("Segoe UI", 12, "bold")).pack()

        leaderboard_listbox = tk.Listbox(leaderboard_frame, height=20, width=30)
        leaderboard_listbox.pack()

        # Populate leaderboard with scores
        def refresh_leaderboard():
            leaderboard_listbox.delete(0, tk.END)
            leaderboard_listbox.insert(tk.END, "Individual Scores:")
            for individual, score in self.data["scores"]["individual_scores"].items():
                leaderboard_listbox.insert(tk.END, f"{individual}: {score}")

            leaderboard_listbox.insert(tk.END, "")
            leaderboard_listbox.insert(tk.END, "Team Scores:")
            for team, total in self.data["scores"]["team_scores"].items():
                leaderboard_listbox.insert(tk.END, f"{team}: {total}")

        refresh_leaderboard()

        # Add buttons for score management
        buttons_frame = ttk.Frame(self.button_frame)
        buttons_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill="both", expand=True)

        def remove_selected_score():
            selected = leaderboard_listbox.get(tk.ACTIVE)
            if selected.startswith("Individual Scores") or selected.startswith("Team Scores") or not selected.strip():
                messagebox.showerror("Error", "Please select a valid score to delete!")
                return

            if ":" in selected:
                name, _ = selected.split(":", 1)
                name = name.strip()
                if name in self.data["scores"]["individual_scores"]:
                    del self.data["scores"]["individual_scores"][name]
                    messagebox.showinfo("Success", f"Score for individual {name} removed successfully!")
                elif name in self.data["scores"]["team_scores"]:
                    del self.data["scores"]["team_scores"][name]
                    messagebox.showinfo("Success", f"Score for team {name} removed successfully!")
                else:
                    messagebox.showerror("Error", "Selected score not found!")
                refresh_leaderboard()

        buttons = [
            ("Assign Individual Scores", self.assign_individual_scores),
            ("Assign Team Member Scores", self.assign_team_member_scores),
            ("Remove Selected Score", remove_selected_score),
            ("Calculate Results", self.calculate_results),
            ("Back to Main Menu", self.show_main_menu)
        ]
        for text, command in buttons:
            btn = ttk.Button(buttons_frame, text=text, command=command, width=25)
            btn.pack(pady=5)

    # Add leaderboard to 'Assign Individual Scores' and update button functionality
    def assign_individual_scores(self):
        self.clear_frame()

        # Add live leaderboard for individual scores
        leaderboard_frame = ttk.Frame(self.button_frame)
        leaderboard_frame.pack(side=tk.LEFT, padx=10, pady=10, fill="y")
        ttk.Label(leaderboard_frame, text="Individual Leaderboard", font=("Segoe UI", 12, "bold")).pack()

        leaderboard_text = Text(leaderboard_frame, height=20, width=30, state=tk.DISABLED)
        leaderboard_text.pack()

        # Populate leaderboard with individual scores
        leaderboard_text.config(state=tk.NORMAL)
        leaderboard_text.delete(1.0, tk.END)
        leaderboard_text.insert(tk.END, "Individual Scores:\n")
        for individual, score in self.data["scores"]["individual_scores"].items():
            leaderboard_text.insert(tk.END, f"{individual}: {score}\n")
        leaderboard_text.config(state=tk.DISABLED)

        # Add input fields and buttons
        input_frame = ttk.Frame(self.button_frame)
        input_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill="both", expand=True)

        ttk.Label(input_frame, text="Select Individual:").pack(pady=5)
        individual_name_var = StringVar()
        individual_dropdown = ttk.Combobox(input_frame, textvariable=individual_name_var, values=self.data["individuals"], state="readonly")
        individual_dropdown.pack(pady=5)

        ttk.Label(input_frame, text="Enter Score (0-100):").pack(pady=5)
        score_var = StringVar()
        score_entry = ttk.Entry(input_frame, textvariable=score_var)
        score_entry.pack(pady=5)

        def confirm_assign_score():
            individual_name = individual_name_var.get()
            try:
                score = int(score_var.get())
                result = assign_individual_score(self.data, individual_name, score)
                messagebox.showinfo("Result", result)
            except ValueError:
                messagebox.showerror("Error", "Score must be a number between 0 and 100!")
            self.manage_scores()

        ttk.Button(input_frame, text="Confirm", command=confirm_assign_score).pack(pady=10)
        ttk.Button(input_frame, text="Back to Manage Scores", command=self.manage_scores).pack(pady=5)

    # Add leaderboard to 'Assign Team Member Scores' and update button functionality
    def assign_team_member_scores(self):
        self.clear_frame()

        # Add live leaderboard for team scores
        leaderboard_frame = ttk.Frame(self.button_frame)
        leaderboard_frame.pack(side=tk.LEFT, padx=10, pady=10, fill="y")
        ttk.Label(leaderboard_frame, text="Team Leaderboard", font=("Segoe UI", 12, "bold")).pack()

        leaderboard_text = Text(leaderboard_frame, height=20, width=30, state=tk.DISABLED)
        leaderboard_text.pack()

        # Populate leaderboard with team scores
        leaderboard_text.config(state=tk.NORMAL)
        leaderboard_text.delete(1.0, tk.END)
        leaderboard_text.insert(tk.END, "Team Scores:\n")
        for team, total in self.data["scores"]["team_scores"].items():
            leaderboard_text.insert(tk.END, f"{team}: {total}\n")
        leaderboard_text.config(state=tk.DISABLED)

        # Add input fields and buttons
        input_frame = ttk.Frame(self.button_frame)
        input_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill="both", expand=True)

        ttk.Label(input_frame, text="Select Team:").pack(pady=5)
        team_name_var = StringVar()
        team_dropdown = ttk.Combobox(input_frame, textvariable=team_name_var, values=list(self.data["teams"].keys()), state="readonly")
        team_dropdown.pack(pady=5)

        ttk.Label(input_frame, text="Select Member:").pack(pady=5)
        member_name_var = StringVar()
        member_dropdown = ttk.Combobox(input_frame, textvariable=member_name_var, state="readonly")
        member_dropdown.pack(pady=5)

        def update_members(*args):
            team_name = team_name_var.get()
            member_dropdown["values"] = self.data["teams"].get(team_name, [])

        team_name_var.trace("w", update_members)

        ttk.Label(input_frame, text="Enter Score (0-100):").pack(pady=5)
        score_var = StringVar()
        score_entry = ttk.Entry(input_frame, textvariable=score_var)
        score_entry.pack(pady=5)

        def confirm_assign_score():
            team_name = team_name_var.get()
            member_name = member_name_var.get()
            try:
                score = int(score_var.get())
                result = assign_team_member_score(self.data, team_name, member_name, score)
                messagebox.showinfo("Result", result)
            except ValueError:
                messagebox.showerror("Error", "Score must be a number between 0 and 100!")
            self.manage_scores()

        ttk.Button(input_frame, text="Confirm", command=confirm_assign_score).pack(pady=10)
        ttk.Button(input_frame, text="Back to Manage Scores", command=self.manage_scores).pack(pady=5)

    # Rename the local function to avoid conflict with the global export_results function
    def calculate_results(self):
        if not self.data["scores"]["individual_scores"] and not self.data["scores"]["team_scores"]:
            messagebox.showerror("Error", "No scores entered yet!")
            return

        results_window = tk.Toplevel(self.root)
        results_window.title("Results")
        results_window.geometry("400x400")

        results = determine_winners(self.data)

        result_text = Text(results_window, height=20, width=50)
        result_text.pack(padx=10, pady=10)
        result_text.insert(tk.END, "Individual Scores:\n")
        for individual, score in results["individual_scores"].items():
            result_text.insert(tk.END, f"{individual}: {score}\n")

        result_text.insert(tk.END, "\nTeam Scores:\n")
        for team, total in results["team_totals"].items():
            result_text.insert(tk.END, f"{team}: {total['average_score']}\n")
            for member, score in total["members"].items():
                result_text.insert(tk.END, f"  {member}: {score}\n")

        result_text.insert(tk.END, "\nWinners:\n")
        result_text.insert(tk.END, f"Individual Winner: {results['individual_winner']}\n")
        result_text.insert(tk.END, f"Team Winner: {results['team_winner']}\n")
        result_text.config(state=tk.DISABLED)

        def save_results():
            file_path = filedialog.asksaveasfilename(
                initialfile="EventWiz-results.txt",
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt")]
            )
            if file_path:
                result = export_results(self.data, file_path)
                messagebox.showinfo("Export Results", result)

        ttk.Button(results_window, text="Export Results", command=save_results).pack(pady=10)
        ttk.Button(results_window, text="Close", command=results_window.destroy).pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = TournamentApp(root)
    root.mainloop()