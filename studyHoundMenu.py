import tkinter as tk
from tkinter import PhotoImage, messagebox
from studyHound import StudyHound  
from datetime import datetime, timedelta
#DZJU2B Atay Eshimbekov
def load_settings():
    settings_path = r"settings.txt"
    settings = {"night_mode": False, "min_study": 50, "min_rest": 10}
    try:
        with open(settings_path, "r") as f:
            for line in f:
                key, value = line.strip().split(": ")
                if key == "NightMode":
                    settings["night_mode"] = True if value == "1" else False
                elif key == "MinStudy":
                    settings["min_study"] = int(value)
                elif key == "MinRest":
                    settings["min_rest"] = int(value)
    except FileNotFoundError:
        pass
    return settings

def save_settings(settings):
    settings_path = r"settings.txt"
    with open(settings_path, "w") as f:
        f.write(f"NightMode: {'1' if settings['night_mode'] else '0'}\n")
        f.write(f"MinStudy: {settings['min_study']}\n")
        f.write(f"MinRest: {settings['min_rest']}\n")


class StudyHoundMenu:
    def __init__(self):
        self.settings = load_settings()
        self.root = tk.Tk()
        self.root.title("StudyHound")
        self.root.geometry("400x690")
        
        self.logo_label = None
        self.streak_label = None
        self.start_button = None
        self.settings_button = None
        self.footer_label = None
        
        self.apply_styling()
        self.root.mainloop()

    def apply_styling(self):
        bg_color = "#000000" if self.settings["night_mode"] else "#fbbc5c"
        text_color = "#fbbc5c" if self.settings["night_mode"] else "black"
        button_bg = "#181818" if self.settings["night_mode"] else "#F6C283"

        button_style = {
            "font": ("Courier New", 14),
            "bd": 5,
            "relief": "solid",
            "highlightbackground": "#FBBC5C",
            "highlightthickness": 1,
            "borderwidth": 0,
            "width": 20,
            "bg": button_bg,
            "fg": text_color
        }

        self.root.configure(bg=bg_color)

        # logo part
        logo_path = r"images\StudyHoundFullLogoBlack.png" if self.settings["night_mode"] else r"images\StudyHoundFullLogoOriginal.png"
        logo = PhotoImage(file=logo_path)
        if self.logo_label:
            self.logo_label.config(image=logo)
            self.logo_label.image = logo
            self.logo_label.configure(bg=bg_color)
        else:
            self.logo_label = tk.Label(self.root, image=logo, bg=bg_color)
            self.logo_label.image = logo
            self.logo_label.pack(pady=20)

        

        # Start button stuff 
        if self.start_button:
            self.start_button.configure(**button_style)
        else:
            self.start_button = tk.Button(self.root, text="Start", command=self.start_popup, **button_style)
            self.start_button.pack(pady=20)

        # Settings button stuff
        if self.settings_button:
            self.settings_button.configure(**button_style)
        else:
            self.settings_button = tk.Button(self.root, text="Settings", command=self.settings_window, **button_style)
            self.settings_button.pack(pady=20)

        # My stuff
        if self.footer_label:
            self.footer_label.configure(bg=bg_color, fg=text_color)
        else:
            self.footer_label = tk.Label(self.root, text="Made by Atay Eshimbekov\nDZJU2B\nStudyHound 2024", 
                                         font=("Courier New", 8), bg=bg_color, fg=text_color)
            self.footer_label.pack(side="bottom", pady=10)

    # Start sesh stuff
    def start_popup(self):
        # Create a new pop-up window
        popup = tk.Toplevel(self.root)
        popup.title("StudyHound start session")
        popup.geometry("300x300")
        
        # Set background color
        bg_color = "#000000" if self.settings["night_mode"] else "#fbbc5c"
        text_color = "#fbbc5c" if self.settings["night_mode"] else "black"
        button_bg = "#181818" if self.settings["night_mode"] else "#F6C283"

        button_style = {
            "font": ("Courier New", 14),
            "bd": 5,
            "relief": "solid",
            "highlightbackground": "#FBBC5C",
            "highlightthickness": 1,
            "borderwidth": 0,
            "width": 20,
            "bg": button_bg,
            "fg": text_color
        }

        popup.configure(bg=bg_color)
        
        # rounds
        tk.Label(popup, text="Rounds:", bg=bg_color, fg=text_color).pack(pady=10)
        rounds_entry = tk.Entry(popup, bg="white", fg="black")
        rounds_entry.insert(0, "3")  # Default value
        rounds_entry.pack()

        # purpose
        tk.Label(popup, text="Purpose:", bg=bg_color, fg=text_color).pack(pady=10)
        purpose_entry = tk.Entry(popup, bg="white", fg="black")
        purpose_entry.insert(0, "Study")  # Default value
        purpose_entry.pack()

        # Validate and start session
        def start_session():
            try:
                rounds = int(rounds_entry.get())
                if rounds < 1 or rounds > 99:
                    raise ValueError("Rounds must be between 1 and 99.")
            except ValueError as e:
                messagebox.showerror("Invalid Input", str(e))
                return

            purpose = purpose_entry.get()
            if len(purpose) > 15:
                messagebox.showerror("Invalid Input", "Purpose must be 15 characters or less.")
                return

   
            set_work = self.settings["min_study"]  
            set_rest = self.settings["min_rest"]  

    # Determine mode 
    # 1 dark 0 original
            mode = "dark" if self.settings["night_mode"] else "original"
    
    # Create StudyHound with all parameters
            studyHound_app = StudyHound(
                tk.Toplevel(self.root),  
                purpose,                 
                set_work,                
                True, #(always true)
                rounds,                  
                set_rest,                
                mode                     
            )
    
            popup.destroy()  

        start_button = tk.Button(popup, text="Start Session", command=start_session, **button_style)
        start_button.pack(pady=20)

   
    # Apply styling to the settings popup window
    def apply_popup_styling(self, popup, night_mode_var, study_entry, rest_entry):
        bg_color = "#000000" if self.settings["night_mode"] else "#fbbc5c"
        text_color = "#fbbc5c" if self.settings["night_mode"] else "black"
        button_bg = "#181818" if self.settings["night_mode"] else "#F6C283"

        button_style = {
            "font": ("Courier New", 14),
            "bd": 5,
            "relief": "solid",
            "highlightbackground": "#FBBC5C",
            "highlightthickness": 1,
            "borderwidth": 0,
            "width": 20,
            "bg": button_bg,
            "fg": text_color
        }

        popup.configure(bg=bg_color)
        for widget in popup.winfo_children():
            if isinstance(widget, tk.Label):
                widget.configure(bg=bg_color, fg=text_color)
            elif isinstance(widget, tk.Entry):
                widget.configure(bg="white", fg="black")
            elif isinstance(widget, tk.Checkbutton):
                widget.configure(bg=bg_color, fg=text_color, selectcolor=bg_color)
            elif isinstance(widget, tk.Button):
                widget.configure(**button_style)

    # Settings window
    def settings_window(self):
        popup = tk.Toplevel(self.root)
        popup.title("StudyHound settings")
        popup.geometry("300x300")
        
        # Set background color
        bg_color = "#000000" if self.settings["night_mode"] else "#fbbc5c"
        text_color = "#fbbc5c" if self.settings["night_mode"] else "black"
        button_bg = "#181818" if self.settings["night_mode"] else "#F6C283"

        button_style = {
            "font": ("Courier New", 14),
            "bd": 5,
            "relief": "solid",
            "highlightbackground": "#FBBC5C",
            "highlightthickness": 1,
            "borderwidth": 0,
            "width": 20,
            "bg": button_bg,
            "fg": text_color
        }
        
        popup.configure(bg=bg_color)
        
        # Night mode checkbox
        night_mode_var = tk.BooleanVar(value=self.settings["night_mode"])
        night_mode_check = tk.Checkbutton(popup, text="Night Mode", variable=night_mode_var, bg=bg_color, fg=text_color, selectcolor=bg_color)
        night_mode_check.pack(pady=20)
        
        # Input fields for study and rest durations
        tk.Label(popup, text="Study Round Duration (minutes):", bg=bg_color, fg=text_color).pack()
        study_entry = tk.Entry(popup, bg="white", fg="black")
        study_entry.insert(0, str(self.settings["min_study"]))
        study_entry.pack()
        
        tk.Label(popup, text="Rest Round Duration (minutes):", bg=bg_color, fg=text_color).pack()
        rest_entry = tk.Entry(popup, bg="white", fg="black")
        rest_entry.insert(0, str(self.settings["min_rest"]))
        rest_entry.pack()
        
        # Save button
        def save():
            study_value = study_entry.get()
            rest_value = rest_entry.get()
            
            if not (study_value.isdigit() and 1 <= int(study_value) <= 99):
                messagebox.showerror("Error", "Study Round Duration must be between 1 and 99.")
                return
            
            if not (rest_value.isdigit() and 1 <= int(rest_value) <= 99):
                messagebox.showerror("Error", "Rest Round Duration must be between 1 and 99.")
                return
            
            self.settings = {
                "night_mode": night_mode_var.get(),
                "min_study": int(study_value),
                "min_rest": int(rest_value)
            }
            save_settings(self.settings)
            self.apply_styling()
            self.apply_popup_styling(popup, night_mode_var, study_entry, rest_entry)
        
        save_button = tk.Button(popup, text="Save", command=save, **button_style)
        save_button.pack(pady=20)

if __name__ == "__main__":
    StudyHoundMenu()