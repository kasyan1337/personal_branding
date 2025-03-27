import tkinter as tk
from tkinter import Canvas, Label, ARC
from datetime import datetime
import configparser
import webbrowser
from PIL import Image, ImageTk
import os

config = configparser.ConfigParser()
config.read('config.ini')
project_name = config.get('DEFAULT', 'project_name', fallback='Kasim LaunchPad')
logo_path = config.get('DEFAULT', 'logo_path', fallback='images/cbtlogo.png')
github_url = config.get('DEFAULT', 'github_url', fallback='https://github.com/kasyan1337')

def open_github(event):
    webbrowser.open(github_url)

def show_splash(duration=4000):
    splash = tk.Tk()
    splash.configure(bg="white")
    splash.overrideredirect(True)

    project_label = Label(splash, text=project_name, font=("Helvetica", 24, "bold"), bg="white", fg="#333333")
    project_label.pack(pady=(20, 10))

    try:
        if not os.path.isabs(logo_path):
            logo_path_full = os.path.join(os.getcwd(), logo_path)
        else:
            logo_path_full = logo_path
        original_image = Image.open(logo_path_full)
        max_width, max_height = 150, 150
        ratio = min(max_width / original_image.width, max_height / original_image.height, 1)
        new_width = int(original_image.width * ratio)
        new_height = int(original_image.height * ratio)
        resized_image = original_image.resize((new_width, new_height), Image.LANCZOS)
        logo = ImageTk.PhotoImage(resized_image)
        logo_label = Label(splash, image=logo, bg="white")
        logo_label.image = logo
        logo_label.pack(pady=(10, 10))
    except Exception as e:
        print("Failed to load logo:", e)

    canvas = Canvas(splash, width=50, height=50, highlightthickness=0, bg="white")
    canvas.pack(pady=10)
    arc = canvas.create_arc(5, 5, 45, 45, start=0, extent=90, style=ARC, outline="#1a0dab", width=3)

    angle = 0
    def update_arc():
        nonlocal angle
        angle = (angle + 10) % 360
        canvas.itemconfig(arc, start=angle)
        splash.after(50, update_arc)
    update_arc()

    current_year = datetime.now().year
    bottom_frame = tk.Frame(splash, bg="white")
    bottom_frame.pack(side="bottom", pady=20)
    label_developed = Label(bottom_frame, text="Developed by ", font=("Helvetica", 10), bg="white", fg="#333333")
    label_developed.pack(side="left")
    clickable_label = Label(bottom_frame, text="Kasim Janci", font=("Helvetica", 10, "underline"), fg="#1a0dab", cursor="hand2", bg="white")
    clickable_label.pack(side="left")
    clickable_label.bind("<Button-1>", open_github)
    label_right = Label(bottom_frame, text=f" | © {current_year} All rights reserved", font=("Helvetica", 10), bg="white", fg="#333333")
    label_right.pack(side="left")

    splash.update_idletasks()
    window_width = splash.winfo_width()
    window_height = splash.winfo_height()
    x = (splash.winfo_screenwidth() - window_width) // 2
    y = (splash.winfo_screenheight() - window_height) // 2
    splash.geometry(f"{window_width}x{window_height}+{x}+{y}")

    splash.after(duration, splash.destroy)
    splash.mainloop()

if __name__ == "__main__":
    show_splash()