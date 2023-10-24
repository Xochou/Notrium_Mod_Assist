import tkinter as tk
import customtkinter as ctk

from tkinter import filedialog


# System Settings
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


# Frame: Start
start_frame = ctk.CTk()
start_frame.geometry("720x480")
start_frame.title("Notrium Mod Assist")

# Frame: Game Dir
game_dir_frame = ctk.CTkFrame(start_frame, width=400, height=40)
game_dir_frame.pack(side="top")

game_dir_label = ctk.CTkLabel(game_dir_frame, text="Notrium Directory:")
game_dir_box = ctk.CTkTextbox(game_dir_frame, width=400, height=40)

game_dir_label.pack(side="left", padx=10)
game_dir_box.pack(side="left")

def _browse_dir(set_target):
    dir_n = tk.filedialog.askdirectory()

    if isinstance(set_target, ctk.CTkTextbox):
        set_target.delete("1.0", "end")
        set_target.insert("1.0", dir_n)
    elif isinstance(set_target, ctk.CTkLabel):
        set_target.configure(text=dir_n)
        set_target.update()


game_dir_browse_button = ctk.CTkButton(game_dir_frame, width=140, height=40, text="Browse", command=lambda: _browse_dir(game_dir_box))
game_dir_browse_button.pack(side="right")



