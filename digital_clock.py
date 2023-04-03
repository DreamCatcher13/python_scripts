from tkinter import *
from datetime import datetime

bg_c = "white"
clock_c = "#ff904f"
time_font = ('Arial', 80)
date_font = ('Arial', 30)

# window config
window = Tk()
window.title("My Digital Clock")
#window.geometry('460x200')
window.resizable(width=False, height=False)
window.config(padx=15, pady=15, bg=bg_c)

def clock():
	time = datetime.now()
	hour = time.strftime("%H:%M:%S")
	date = time.strftime("%A, %d / %B / %Y")
	time_label.config(text=hour)
	time_label.after(200, clock)
	date_label.config(text=date)


# labels config
time_label = Label(text=" ", fg=clock_c, font=time_font, bg=bg_c)
time_label.grid(column=1, row=1)

date_label = Label(text=" ", fg=clock_c, font=date_font, bg=bg_c)
date_label.grid(column=1, row=2)

clock()

window.mainloop()