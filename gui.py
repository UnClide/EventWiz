import json
import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel, Label, OptionMenu, Button, StringVar
from data_management import load_data, save_data
from team_management import add_team, delete_team
from individual_management import add_individual, delete_individual
from event_management import add_event, delete_event

class TournamentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tournament Scoring System")
        self.data = load_data()

        # Add a title label
        title_label = tk.Label(root, text="Tournament Scoring System", font=("Arial", 16))
        title_label.pack(pady=10)

        # Create buttons for different actions
        self.add_team_button = tk.Button(root, text="Add Team", command=self.add_team, width=20)
        self.add_team_button.pack(pady=5)

        self.add_individual_button = tk.Button(root, text="Add Individual", command=self.add_individual, width=20)
        self.add_individual_button.pack(pady=5)

        self.add_event_button = tk.Button(root, text="Add Event", command=self.add_event, width=20)
        self.add_event_button.pack(pady=5)

        self.save_button = tk.Button(root, text="Save Data", command=self.save_data, width=20)
        self.save_button.pack(pady=5)

        self.view_data_button = tk.Button(root, text="View Data", command=self.view_data, width=20)
        self.view_data_button.pack(pady=5)

    def is_valid_input(self, input_str):
        # Check if the input is empty or consists only of spaces
        return input_str and input_str.strip()

    # Add Team
    def add_team(self):
        team_name = simpledialog.askstring("Add Team", "Enter Team name:")
        if team_name is None: # User clicked Cancel
            return
        if not self.is_valid_input(team_name):
            messagebox.showerror("Error", "Team name cannot be empty!")
            return

        result = add_team(self.data, team_name)
        messagebox.showinfo("Result", result)

    # Add Individual
    def add_individual(self):
        individual_name = simpledialog.askstring("Add Individual", "Enter Individual name:")
        if individual_name is None:
            return
        if not self.is_valid_input(individual_name):
            messagebox.showerror("Error", "Individual name cannot be empty!")
            return

        choice = messagebox.askyesno("Add to Team", "Do you want to add this individual to a team?")
        if choice:
            team_name = simpledialog.askstring("Add to Team", "Enter Team name:")
            if team_name is None:
                return
            if not self.is_valid_input(team_name):
                messagebox.showerror("Error", "Team name cannot be empty!")
                return

            result = add_individual(self.data, individual_name, team_name)
        else:
            result = add_individual(self.data, individual_name)

        messagebox.showinfo("Result", result)

    # Add Event
    def add_event(self):
        # Create a new window for event type selection
        event_window = Toplevel(self.root)
        event_window.title("Add Event")

        # Event name input
        Label(event_window, text="Enter Event name:").pack(pady=5)
        event_name_entry = simpledialog.askstring("Add Event", "Enter Event name:", parent=event_window)
        if event_name_entry is None:
            event_window.destroy()
            return
        if not self.is_valid_input(event_name_entry):
            messagebox.showerror("Error", "Event name cannot be empty!", parent=event_window)
            event_window.destroy()
            return

        # Event type selection
        Label(event_window, text="Select Event type:").pack(pady=5)
        event_type_var = StringVar(event_window)
        event_type_var.set("team")  # Default value
        OptionMenu(event_window, event_type_var, "team", "individual").pack(pady=5)

        # Confirm button
        def confirm_event():
            event_name = event_name_entry
            event_type = event_type_var.get()
            result = add_event(self.data, event_name, event_type)
            messagebox.showinfo("Result", result, parent=event_window)
            event_window.destroy()

        Button(event_window, text="Confirm", command=confirm_event).pack(pady=10)

    # Save Data
    def save_data(self):
        save_data(self.data)
        messagebox.showinfo("Success", "Data saved successfully!")

    # View Data
    def view_data(self):
        data_window = Toplevel(self.root)
        data_window.title("Current Data")
        data_text = tk.Text(data_window, height=20, width=50)
        data_text.pack(padx=10, pady=10)
        data_text.insert(tk.END, json.dumps(self.data, indent=4))
        data_text.config(state=tk.DISABLED)  # Make the text read-only

if __name__ == "__main__":
    root = tk.Tk()
    app = TournamentApp(root)
    root.mainloop()