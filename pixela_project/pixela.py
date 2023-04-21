import requests, os, sys
from datetime import datetime
from tkinter import *
from tkinter import filedialog, messagebox, font

### for pyinstaller ###
def resource_path(relative_path):
    try:   
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

### GLOBAL VARIABLES ###
PIXELA_END = "https://pixe.la/v1/users"
TOKEN = ""
USERNAME = ""
TODAY = datetime.now().strftime("%Y%m%d")
FONT =  ("Times New Roman",12)
B_FONT = ("Helvetica 12 bold")
BG="#b8f78d"
BG2 = "#c5ccfa"

def user_create():
	""" create a user """
	top = Toplevel()
	top.config(padx=5, pady=5, bg=BG2)
	top.grab_set()
	
	user_label = Label(top, bg=BG2, text="Enter your username",  font=FONT)
	token_label = Label(top, bg=BG2, text="Enter your secret token", font=FONT)
	user_label.grid(column=1, row=1, padx=2)
	token_label.grid(column=1, row=2, padx=2)

	user = Entry(top, width=20)
	tkn = Entry(top, width=20)
	user.grid(column=2, row=1)
	tkn.grid(column=2, row=2)
	
	def create():
		user_params = {
			"token": tkn.get(),
			"username": user.get(),
			"agreeTermsOfService": "yes",
			"notMinor": "yes"
		}
		
		if len(user_params['token']) == 0 or len(user_params['username']) == 0:
			messagebox.showinfo(title="Error", message="You should fill all the fields")
		else:
			endpoint = PIXELA_END
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
	global TOKEN, USERNAME
	messagebox.showinfo(title="Responce", message="Select *.txt file with your credentials in this format:\ntoken\nusername")
	filetypes = (('text files', '*.txt'), ('All files', '*.*'))
	pixela_cred = filedialog.askopenfilename(title='Select your creds', filetypes=filetypes)
	with open(pixela_cred, "r") as f:
		content = [l.rstrip() for l in f.readlines()]
		TOKEN, USERNAME = content[0], content[1]
	
def graph_create():
	""" creating a graph for given user """
	select_file()
	top = Toplevel()
	top.config(padx=5, pady=5, bg=BG2)
	top.grab_set()
	
	g_id = Label(top, text="Enter graph ID", bg=BG2, font=FONT)
	g_name = Label(top, text="Enter graph name", bg=BG2, font=FONT)
	g_unit = Label(top, text="Enter graph units", bg=BG2, font=FONT)
	g_type = Label(top, text="Enter type of quantity:\nint OR float", bg=BG2, font=FONT) 
	g_color = Label(top, text="Enter graph color", bg=BG2, font=FONT)
	colors = "shibafu (green), momiji (red),\n\t\tsora (blue), ichou (yellow),\n\t\tajisai (purple) and kuro (black)"
	all_colors = Label(top, text="Supported colors: "+colors, bg=BG2, font=FONT)
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
			"X-USER-TOKEN": TOKEN
		}
		user_params = {
			"id": id.get(),
			"name": name.get(),
			"unit": unit.get(),
			"type": type.get(),
			"color": color.get()
		}
		# is where any way to make it better?
		if len(user_params['id']) == 0 or len(user_params['name']) == 0 or len(user_params['unit']) == 0 or len(user_params['type']) == 0 or len(user_params['color']) == 0:
			messagebox.showinfo(title="Error", message="You should fill all the fields")
		else:
			endpoint = f"{PIXELA_END}/{USERNAME}/graphs"
			responce = requests.post(url=endpoint, json=user_params, headers=headers)
			msg = responce.json()
			messagebox.showinfo(title="Responce", message=msg['message'])
		
	create_b = Button(top, text="Add a graph", width=15, command=create)
	create_b.grid(column=1, row=7, columnspan=2, pady=5)
		
	top.mainloop()	
	
def post_update_pixel():
	""" post a pixel """
	select_file()
	top = Toplevel()
	top.config(padx=5, pady=5, bg=BG2)
	top.grab_set()
	
	g_id = Label(top, text="Enter graph ID", bg=BG2, font=FONT)
	q = Label(top, text="Enter quantity", bg=BG2, font=FONT)
	d = Label(top, text="Enter date", bg=BG2, font=FONT)
	g_id.grid(column=1, row=1)
	q.grid(column=1, row=2)
	d.grid(column=1, row=3)
	
	id = Entry(top, width=20)
	quantity = Entry(top, width=20)
	date = Entry(top, width=20)
	date.insert(0, TODAY)
	id.grid(column=2, row=1)
	quantity.grid(column=2, row=2)
	date.grid(column=2, row=3)
	
	def add():
		headers = {
			"X-USER-TOKEN": TOKEN
		}
		user_params = {
			"date": date.get(),
			"quantity": quantity.get(),
		}
		if len(user_params['date']) == 0 or len(user_params['quantity']) == 0 or len(id.get()) == 0:
			messagebox.showinfo(title="Error", message="You should fill all the fields")
		else:
			endpoint = f"{PIXELA_END}/{USERNAME}/graphs/{id.get()}"
			responce = requests.post(url=endpoint, json=user_params, headers=headers)
			msg = responce.json()
			messagebox.showinfo(title="Responce", message=msg['message'])
		
	def update():
		headers = {
			"X-USER-TOKEN": TOKEN
		}
		user_params = {
			"quantity": quantity.get(),
		}
		
		if len(date.get()) == 0 or len(user_params['quantity']) == 0 or len(id.get()) == 0:
			messagebox.showinfo(title="Error", message="You should fill all the fields")
		else:
			endpoint = f"{PIXELA_END}/{USERNAME}/graphs/{id.get()}/{date.get()}"
			responce = requests.put(url=endpoint, json=user_params, headers=headers)
			msg = responce.json()
			messagebox.showinfo(title="Responce", message=msg['message'])
		
	add_button = Button(top, text="Add a pixel", width=15, command=add)
	update_button = Button(top, text="Update a pixel", width=15, command=update)
	add_button.grid(column=1, row=4, pady=5)
	update_button.grid(column=2, row=4, pady=5)
	
	top.mainloop()
	
### MAIN WINDOW ###
window = Tk()
window.title("Pixela habit tracker")
window.config(padx=15, pady=15, bg=BG)

canvas = Canvas(width=480, height=270, highlightthickness=0)
parrot = PhotoImage(file=resource_path("pixela.png"))
canvas_img = canvas.create_image(240, 135, image=parrot)
canvas.grid(column=1, row=1, columnspan=3)

pixel_button = Button(text="Add or update a pixel", relief="ridge", borderwidth=3, bg="#fff242", width=20, font=B_FONT, command=post_update_pixel)
add_user = Button(text="Add a user", relief="ridge", borderwidth=3, bg="#fff242", width=15, font=B_FONT, command=user_create)
add_graph = Button(text="Add a graph", relief="ridge", borderwidth=3,  bg="#fff242", width=15, font=B_FONT, command=graph_create)
pixel_button.grid(column=2, row=2, pady=5)
add_user.grid(column=1, row=3, pady=5)
add_graph.grid(column=3, row=3, pady=5)


window.mainloop()
