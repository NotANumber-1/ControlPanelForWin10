import tkinter as tk
import time, os, subprocess
from tkinter.constants import ALL
window = tk.Tk()
def close(data=""):
    time.sleep(0.25)
    window.destroy()
def unfullscreen():
    window.attributes("-fullscreen", False)
def fullscreen():
    window.attributes("-fullscreen", True)
def taskmgr():
    os.system("taskmgr")


window.geometry("1024x512")
window.title("Control Panel")
window.iconbitmap("app.ico")
window.attributes("-fullscreen", True)
name_text = tk.Label(text="Control Panel")
name_text.config(font=("Arial", 20))
name_text.pack()
name_text.place(x=10, y=10)
quit_button = tk.Button(text="Close", bg="red", fg="white", width=8, height=2, command=close)
quit_button.config(font=("Arial", 12))
quit_button.pack()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
quit_button.place(x=10, y=64)

unfulls_button = tk.Button(text="Unfullscreen", bg="blue", fg="white", width=12, height=2, command=unfullscreen)
unfulls_button.config(font=("Arial", 12))
unfulls_button.pack()
unfulls_button.place(x=10, y=144)

fulls_button = tk.Button(text="Fullscreen", bg="green", fg="white", width=12, height=2, command=fullscreen)
fulls_button.config(font=("Arial", 12))
fulls_button.pack()
fulls_button.place(x=10, y=224)

task_button = tk.Button(text="Task manager", bg="yellow", fg="black", width=12, height=2, command=taskmgr)
task_button.config(font=("Arial", 12))
task_button.pack()
task_button.place(x=10, y=304)

command_entry = tk.Entry(window, font="Arial")
command_entry.config(font=("Arial", 12))
command_entry.place(x=256, y=64)

command_message = tk.Label(text="Command line")
command_message.config(font=("Arial", 16))
command_message.pack()
command_message.place(x=256, y=32)
def command(data=""):
    print("Command:")
    command_line = command_entry.get()
    if command_line != "" or " ":
        os.system(command_line)
    print("# End \n")
    command_entry.insert(0, "Done: ")
    time.sleep(0.25)
    command_entry.delete(0, "end")
window.bind("<Return>", command)
window.bind("<Escape>", close)
window.mainloop()