import tkinter as tk
from tkinter import messagebox
import time, os, platform, psutil, keyboard
window = tk.Tk()
def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)
def close(data=""):
    _conf = messagebox.askokcancel(title="Close window confirm", message="Close Control Panel window?")
    if _conf:
        time.sleep(0.25)
        window.destroy()
    else:
        pass
def unfullscreen():
    window.attributes("-fullscreen", False)
def fullscreen():
    window.attributes("-fullscreen", True)
def taskmgr():
    os.system("taskmgr")
def ctrlpn():
    os.system("control")
def osinfo():
    messagebox.showinfo(title="OS info", message=f"Platform: {platform.platform()}")
def batinfo():
    battery = psutil.sensors_battery()
    messagebox.showinfo(title="Battery info", message=f"Percentage: {battery.percent}\nPlugged: {battery.power_plugged}\Time left: {convertTime(battery.secsleft)}")
def shutdown10():
    _conf = messagebox.askokcancel(title="System shutdown confirm", message="Shutdown system?")
    if _conf:
        os.system("shutdown -s -t 10")
    else:
        pass
def cancshutdown():
    os.system("shutdown -a")
    messagebox.showinfo(title="Shutdown canceled", message="Shutdown has been canceled")
def run():
    keyboard.press("Windows")
    keyboard.press("r")
    keyboard.release("Windows")
    keyboard.release("r")
def lock():
    _conf = messagebox.askokcancel(title="Control Panel lock confirm", message="Lock Control Panel window?")
    if _conf:
        os.system("pause")
    else:
        pass
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

show_os_button = tk.Button(text="Show OS info", bg="yellow", fg="black", width=12, height=2, command=osinfo)
show_os_button.config(font=("Arial", 12))
show_os_button.pack()
show_os_button.place(x=10, y=384)

show_battery_button = tk.Button(text="Show battery info", bg="yellow", fg="black", width=14, height=2, command=batinfo)
show_battery_button.config(font=("Arial", 12))
show_battery_button.pack()
show_battery_button.place(x=10, y=464)
"""
_button = tk.Button(text="???", bg="yellow", fg="black", width=14, height=2, command=???)
_button.config(font=("Arial", 12))
_button.pack()
_button.place(x=0, y=0)
"""
shutdown10s_button = tk.Button(text="Shutdown (10s)", bg="yellow", fg="black", width=16, height=2, command=shutdown10)
shutdown10s_button.config(font=("Arial", 12))
shutdown10s_button.pack()
shutdown10s_button.place(x=10, y=544)

shutdowncan_button = tk.Button(text="Cancel shutdown", bg="yellow", fg="black", width=16, height=2, command=cancshutdown)
shutdowncan_button.config(font=("Arial", 12))
shutdowncan_button.pack()
shutdowncan_button.place(x=10, y=624)

control_button = tk.Button(text="Control Panel", bg="yellow", fg="black", width=14, height=2, command=ctrlpn)
control_button.config(font=("Arial", 12))
control_button.pack()
control_button.place(x=208, y=304)

run_button = tk.Button(text="Run", bg="yellow", fg="black", width=14, height=2, command=run)
run_button.config(font=("Arial", 12))
run_button.pack()
run_button.place(x=208, y=384)

lock_button = tk.Button(text="Lock", bg="Red", fg="white", width=8, height=2, command=lock)
lock_button.config(font=("Arial", 12))
lock_button.pack()
lock_button.place(x=208, y=144)
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
