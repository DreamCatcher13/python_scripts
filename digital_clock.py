from tkinter import *
from datetime import datetime

bg_c = "white"
clock_colors = {
	"Monday" : "#e64e0e",
	"Tuesday" : "#f5ae16", 
	"Wednesday" : "#ff904f", 
	"Thursday" : "#19c916",
	"Friday" : "#14dde0",
	"Saturday" : "#1436e0",
	"Sunday" : "#c615ed",
}
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
	c = time.strftime("%A")
	time_label.config(text=hour, fg=clock_colors[c])
	time_label.after(200, clock) # magic
	date_label.config(text=date, fg=clock_colors[c])


# labels config
time_label = Label(text=" ",  font=time_font, bg=bg_c)
time_label.grid(column=1, row=1)

date_label = Label(text=" ", font=date_font, bg=bg_c)
date_label.grid(column=1, row=2)

clock()

window.mainloop()