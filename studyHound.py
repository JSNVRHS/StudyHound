import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from datetime import datetime
#DZJU2B Atay Eshimbekov

class StudyHound:
    def __init__(self, root, goal, setWork, restsOn, rounds, setRest, mode):
        self.root = root
        self.root.title("StudyHound: " + goal)
        
        # Set up
        self.goal = goal
        self.setWork = setWork * 60  # Work in seconds
        self.setRest = setRest * 60  # Rest in seconds
        self.remaining_time = self.setWork 
        self.currentMode = "Study"
        self.rounds = rounds
        self.currentRounds = 0
        self.skip_rest = restsOn
        self.running = False
        self.study_data = None  # To store study data when rounds start
        
        # Set colors 
        if mode == "dark":
            bg_color = "black"
            bright_bg_color = "gray"
            text_color = "#FBBC5C"
            image_path = r"images\StudyHoundNoBG.png"
            button_bg = "#181818"
        else:
            bg_color = "#FBBC5C"
            bright_bg_color = "#F6C283"
            text_color = "black"
            image_path = r"images\StudyHoundBlackNoBG.png"
            button_bg = "#F6C283"
        
        #  The logo
        self.image_label = tk.Label(root, bg=bg_color)
        self.image = PhotoImage(file=image_path)
        self.image_label.config(image=self.image)
        self.image_label.pack(pady=5)

        # Label for rounds
        self.rounds_label = tk.Label(root, text=f"Round {self.currentRounds}/{self.rounds}", font=("Courier New", 14), bg=bg_color, fg=text_color)
        self.rounds_label.pack(pady=5)

        # Label for timer display
        self.timer_label = tk.Label(root, text=self.format_time(self.remaining_time), font=("Courier New", 48), bg=bg_color, fg=text_color)
        self.timer_label.pack(pady=10)

        # Label for mode indicator
        self.focus_chill_label = tk.Label(root, text="Time to focus!", font=("Courier New", 10), bg=bg_color, fg=text_color)
        self.focus_chill_label.pack(pady=5)

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

        self.start_button = tk.Button(root, text="Start", command=self.start_timer, **button_style)
        self.start_button.pack(pady=10)

        self.pause_button = tk.Button(root, text="Pause", command=self.pause_timer, **button_style, state="disabled")
        self.pause_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Reset", command=self.reset_timer, **button_style)
        self.stop_button.pack(pady=10)

        self.skip_button = tk.Button(root, text="Skip rest rounds", command=self.toggle_skip_rest, **button_style)
        self.skip_button.pack(pady=10)

        self.skip_label = tk.Label(root, text=self.get_skip_status(), font=("Courier New", 10), bg=bg_color, fg=text_color)
        self.skip_label.pack(pady=10)

        # My stuff
        self.footer_label = tk.Label(root, text="Made by Atay Eshimbekov\nDZJU2B\nStudyHound 2024", font=("Courier New", 8), bg=bg_color, fg=text_color)
        self.footer_label.pack(side="bottom", pady=10)

        # background color 
        self.root.configure(bg=bg_color)

        # Handle window close event to save history
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def format_time(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"

    def get_skip_status(self):
        return "Skip rests: ON" if self.skip_rest else "Skip rests: OFF"

    def toggle_skip_rest(self):
        self.skip_rest = not self.skip_rest
        self.skip_label.config(text=self.get_skip_status())
        
        # If we're in rest mode and want to skip, switch to study mode
        if self.currentMode == "Rest":
            self.currentMode = "Study"
            self.remaining_time = self.setWork
            self.focus_chill_label.config(text="Time to focus!")
            self.timer_label.config(text=self.format_time(self.remaining_time))

    def start_timer(self):
        if self.currentRounds == 0:  
            self.study_data = {
                "date": self.get_today_date(),
                "goal": self.goal,
                "rounds_intended": self.rounds,
                "rounds_done": 0
            }
        
        if not self.running:
            self.running = True
            self.start_button["state"] = "disabled"
            self.pause_button["state"] = "normal"
            self.skip_button["state"] = "disabled" 
            self.update_timer()

    def pause_timer(self):
        if self.running:
            self.running = False
            self.start_button["state"] = "normal"
            self.pause_button["state"] = "disabled"
            self.skip_button["state"] = "normal"  

    def reset_timer(self):
        self.running = False
        if self.currentMode == "Study":
            self.remaining_time = self.setWork
        else:
            self.remaining_time = self.setRest
        self.timer_label.config(text=self.format_time(self.remaining_time))
        self.start_button["state"] = "normal"
        self.pause_button["state"] = "disabled"
        self.skip_button["state"] = "normal"  

    def switch_mode(self):
        # Always increment rounds when a round (study or rest) is finished
        if self.currentMode == "Study":
            self.currentRounds += 1
            
            if self.study_data:
                self.study_data["rounds_done"] = self.currentRounds

            # Check if all rounds are completed
            if self.currentRounds == self.rounds:
                self.update_labels()
                messagebox.showinfo("Time's Up!", "Congratulations! You've completed your intended number of rounds. You can continue if you'd like.")
                self.running = False
                self.skip_button["state"] = "normal"  

        # Decide next mode 
        if self.currentMode == "Study":
            if self.skip_rest:
                # Stay in study mode
                self.currentMode = "Study"
                self.remaining_time = self.setWork
                self.focus_chill_label.config(text="Time to focus!")
            else:
                # Switch to rest mode
                self.currentMode = "Rest"
                self.remaining_time = self.setRest
                self.focus_chill_label.config(text="Time to chill!")
        else:
            # If currently in rest -> switch back to Study mode
            self.currentMode = "Study"
            self.remaining_time = self.setWork
            self.focus_chill_label.config(text="Time to focus!")

        self.update_labels()
        self.skip_button["state"] = "normal"  

    def update_labels(self):
        self.rounds_label.config(text=f"Round {self.currentRounds}/{self.rounds}")
        if self.currentMode == "Study":
            self.focus_chill_label.config(text="Time to focus!")
        else:
            self.focus_chill_label.config(text="Time to chill!")

    def update_timer(self):
        if self.running:
            if self.remaining_time > 0:
                self.remaining_time -= 1
                self.timer_label.config(text=self.format_time(self.remaining_time))
                self.root.after(1000, self.update_timer)
            else:
                # Timer reaches zero
                self.running = False
                self.switch_mode()
                self.timer_label.config(text=self.format_time(self.remaining_time))
                self.start_button["state"] = "normal"
                self.pause_button["state"] = "disabled"

    def get_today_date(self):
        return datetime.today().strftime('%d.%m.%Y')

    def on_close(self):
        # Write the study data to history.txt when the app is closed
        if self.study_data:
            history_data = (
                f"Date: {self.study_data['date']}\n"
                f"Purpose: {self.study_data['goal']}\n"
                f"Rounds: {self.study_data['rounds_done']}/{self.study_data['rounds_intended']}\n\n"
            )
            # Save the data
            with open(r"records\history.txt", "a") as file:
                file.write(history_data)

        self.root.destroy()



