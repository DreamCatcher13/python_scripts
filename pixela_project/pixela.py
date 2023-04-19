import requests, os, sys
from datetime import datetime
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

### for pyinstaller ###
def resource_path(relative_path):
    try:   
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

### GLOBAL VARIABLES ###
pixela_end = "https://pixe.la/v1/users"
token = ""
username = ""
today = datetime.now().strftime("%Y%m%d")
#font =  !!!

#with open("cred.txt", "r") as f:
#    content = [l.rstrip() for l in f.readlines()]
#    TOKEN, USERNAME = content[0], content[1]

def user_create():
	""" create a user """
	top = Toplevel()
	top.config(padx=5, pady=5)
	top.grab_set()
	
	user_label = Label(top, text="Enter your username", font=("Agency FB", 14))
	token_label = Label(top, text="Enter your secret token", font=("Agency FB", 14))
	user_label.grid(column=1, row=1)
	token_label.grid(column=1, row=2)

	user = Entry(top, width=20)
	token = Entry(top, width=20)
	user.grid(column=2, row=1)
	token.grid(column=2, row=2)
	
	def create():
		user_params = {
			"token": token.get(),
			"username": user.get(),
			"agreeTermsOfService": "yes",
			"notMinor": "yes"
		}
		endpoint = pixela_end
		responce = requests.post(url=endpoint, json=user_params)
		msg = responce.json()
		messagebox.showinfo(title="Responce", message=msg['message'])
		with open(f"{user_params['username']}_cred.txt", "w") as f:
			f.write(f"{user_params['token']}\n{user_params['username']}")	
	
	create_b = Button(top,text="Add a user", width=15, command=create)
	create_b.grid(column=1, row=3, columnspan=2, pady=5)
		
	top.mainloop()
	
def select_file():
	""" select a file with credentials """
	global token, username
	messagebox.showinfo(title="Responce", 
						message="Select *.txt file with your credentials in this format:\ntoken\nusername")
	filetypes = (('text files', '*.txt'), ('All files', '*.*'))
	pixela_cred = filedialog.askopenfilename(title='Select your creds', filetypes=filetypes)
	with open(pixela_cred, "r") as f:
		content = [l.rstrip() for l in f.readlines()]
		token, username = content[0], content[1]
	
def graph_create():
	""" creating a graph for given user """
	select_file()
	top = Toplevel()
	top.config(padx=5, pady=5)
	top.grab_set()
	
	g_id = Label(top, text="Enter graph ID", font=("Agency FB", 14))
	g_name = Label(top, text="Enter graph name", font=("Agency FB", 14))
	g_unit = Label(top, text="Enter graph units", font=("Agency FB", 14))
	g_type = Label(top, text="Enter type of quantity: int OR float", font=("Agency FB", 14)) 
	g_color = Label(top, text="Enter graph color", font=("Agency FB", 14))
	colors = "shibafu (green), momiji (red),\n\t\tsora (blue), ichou (yellow),\n\t\tajisai (purple) and kuro (black)"
	all_colors = Label(top, text="Supported colors: "+colors, font=("Agency FB", 14))
	g_id.grid(column=1, row=1)
	g_name.grid(column=1, row=2)
	g_unit.grid(column=1, row=3)
	g_type.grid(column=1, row=4)
	g_color.grid(column=1, row=5)
	all_colors.grid(column=1, row=6, columnspan=2)
	
	id = Entry(top, width=20)
	name = Entry(top, width=20)
	unit = Entry(top, width=20)
	type = Entry(top, width=20)
	color = Entry(top, width=20)
	type.insert(0, 'int')
	color.insert(0, 'ichou')
	id.grid(column=2, row=1)
	name.grid(column=2, row=2)
	unit.grid(column=2, row=3)
	type.grid(column=2, row=4)
	color.grid(column=2, row=5)
	
	def create():
	
		headers = {
			"X-USER-TOKEN": token
		}
		
		user_params = {
			"id": id.get(),
			"name": name.get(),
			"unit": unit.get(),
			"type": type.get(),
			"color": color.get()
		}
		
		endpoint = f"{pixela_end}/{username}/graphs"
		responce = requests.post(url=endpoint, json=user_params, headers=headers)
		msg = responce.json()
		messagebox.showinfo(title="Responce", message=msg['message'])
		
	create_b = Button(top, text="Add a graph", width=15, command=create)
	create_b.grid(column=1, row=7, columnspan=2, pady=5)
		
	top.mainloop()	
	

# TODO 1 change font
# TODO 2 add some validation	
	
def post_a_pixel():
	""" post a pixel """
	select_file()
	top = Toplevel()
	top.config(padx=5, pady=5)
	top.grab_set()
	
	g_id = Label(top, text="Enter graph ID", font=("Agency FB", 14))
	q = Label(top, text="Enter quantity", font=("Agency FB", 14))
	d = Label(top, text="Enter date", font=("Agency FB", 14))
	g_id.grid(column=1, row=1)
	q.grid(column=1, row=2)
	d.grid(column=1, row=3)
	
	id = Entry(top, width=20)
	quantity = Entry(top, width=20)
	date = Entry(top, width=20)
	date.insert(0, today)
	id.grid(column=2, row=1)
	quantity.grid(column=2, row=2)
	date.grid(column=2, row=3)
	
	def add():
		
		headers = {
			"X-USER-TOKEN": token
		}
		
		user_params = {
			"date": date.get(),
			"quantity": quantity.get(),
		}
		
		endpoint = f"{pixela_end}/{username}/graphs/{id.get()}"
		responce = requests.post(url=endpoint, json=user_params, headers=headers)
		msg = responce.json()
		messagebox.showinfo(title="Responce", message=msg['message'])
		
	add_button = Button(top, text="Add a pixel", width=15, command=add)
	add_button.grid(column=1, row=4, columnspan=2, pady=5)

### MAIN WINDOW ###
window = Tk()
window.title("Pixela habit tracker")
window.config(padx=15, pady=15)

canvas = Canvas(width=480, height=270, highlightthickness=0)
parrot = PhotoImage(file=resource_path("pixela.png"))
canvas_img = canvas.create_image(240, 135, image=parrot)
canvas.grid(column=1, row=1, columnspan=3)

add_pixel = Button(text="Add a pixel", width=15, command=post_a_pixel)
update_pixel = Button(text="Update a pixel", width=15)
add_user = Button(text="Add a user", width=15, command=user_create)
add_graph = Button(text="Add a graph", width=15, command=graph_create)
add_pixel.grid(column=2, row=2, pady=5)
update_pixel.grid(column=2, row=3, pady=5)
add_user.grid(column=1, row=4, pady=5)
add_graph.grid(column=3, row=4, pady=5)


window.mainloop()
