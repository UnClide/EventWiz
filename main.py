import tkinter as tk
from gui import TournamentApp

print("Starting GUI...")

# Main program loop
def main():
    root = tk.Tk()
    app = TournamentApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()