import json
import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel, StringVar, Text
from tkinter import ttk
from data_management import load_data, save_data
from team_management import add_team, delete_team
from individual_management import add_individual, delete_individual
from event_management import add_event, delete_event

class TournamentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tournament Scoring System")
        self.root.geometry("450x550")
        self.root.configure(bg="#E3E3E3")
        
        # Load data from data.json
        self.data = load_data()
        
        # Configure styles for the UI elements
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", font=("Segoe UI", 10), padding=6, borderwidth=0, relief="flat", background="#C0C0C0", foreground="black")
        style.map("TButton", background=[("active", "#A9A9A9")])
        style.configure("TLabel", font=("Segoe UI", 12), background="#E3E3E3")
        
        # Title label
        title_label = ttk.Label(root, text="Tournament Scoring System", font=("Segoe UI", 16, "bold"))
        title_label.pack(pady=10)
        
        # Frame for buttons
        button_frame = ttk.Frame(root)
        button_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        # Buttons for various actions
        buttons = [
            ("Add Team", self.add_team),
            ("Add Individual", self.add_individual),
            ("Add Event", self.add_event),
            ("Save Data", self.save_data),
            ("View Data", self.view_data)
        ]
        
        # Create and pack buttons
        for text, command in buttons:
            btn = ttk.Button(button_frame, text=text, command=command, width=25)
            btn.pack(pady=5)

    def is_valid_input(self, input_str):
        # Check if the input string is valid (not empty and not just whitespace)
        return bool(input_str and input_str.strip())

    def add_team(self):
        # Prompt user to enter team name
        team_name = simpledialog.askstring("Add Team", "Enter Team name:")
        if team_name is None:
            return
        if self.is_valid_input(team_name):
            result = add_team(self.data, team_name)
            messagebox.showinfo("Result", result)
        else:
            messagebox.showerror("Error", "Team name cannot be empty!")
    
    def add_individual(self):
        # Prompt user to enter individual name
        individual_name = simpledialog.askstring("Add Individual", "Enter Individual name:")
        if individual_name is None:
            return
        if self.is_valid_input(individual_name):
            # Ask if the individual should be added to a team
            choice = messagebox.askyesno("Add to Team", "Do you want to add this individual to a team?")
            if choice:
                team_name = simpledialog.askstring("Add to Team", "Enter Team name:")
                if team_name is None:
                    return
                if self.is_valid_input(team_name):
                    result = add_individual(self.data, individual_name, team_name)
                else:
                    messagebox.showerror("Error", "Team name cannot be empty!")
                    return
            else:
                result = add_individual(self.data, individual_name)
            messagebox.showinfo("Result", result)
        else:
            messagebox.showerror("Error", "Individual name cannot be empty!")
    
    def add_event(self):
        # Create a new window for adding an event
        event_window = Toplevel(self.root)
        event_window.title("Add Event")
        event_window.geometry("300x200")
        
        # Event name input
        ttk.Label(event_window, text="Enter Event name:").pack(pady=5)
        event_name_var = StringVar()
        event_entry = ttk.Entry(event_window, textvariable=event_name_var)
        event_entry.pack(pady=5)
        
        # Event type selection
        ttk.Label(event_window, text="Select Event type:").pack(pady=5)
        event_type_var = StringVar(event_window)
        event_type_var.set("team")
        event_dropdown = ttk.Combobox(event_window, textvariable=event_type_var, values=["team", "individual"], state="readonly")
        event_dropdown.pack(pady=5)
        
        def confirm_event():
            # Confirm and add the event
            event_name = event_name_var.get()
            if not self.is_valid_input(event_name):
                messagebox.showerror("Error", "Event name cannot be empty!", parent=event_window)
                return
            result = add_event(self.data, event_name, event_type_var.get())
            messagebox.showinfo("Result", result, parent=event_window)
            event_window.destroy()
        
        # Confirm button
        ttk.Button(event_window, text="Confirm", command=confirm_event).pack(pady=10)
    
    def save_data(self):
        # Save data to data.json
        save_data(self.data)
        messagebox.showinfo("Success", "Data saved successfully!")
    
    def view_data(self):
        # Create a new window to display current data
        data_window = Toplevel(self.root)
        data_window.title("Current Data")
        data_window.geometry("400x400")
        
        # Text widget to display data
        data_text = Text(data_window, height=20, width=50)
        data_text.pack(padx=10, pady=10)
        data_text.insert(tk.END, json.dumps(self.data, indent=4))
        data_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = TournamentApp(root)
    root.mainloop()