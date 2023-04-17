import requests, os, sys
from datetime import datetime
from tkinter import *
from tkinter import messagebox

### for pyinstaller ###
def resource_path(relative_path):
    try:   
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#with open("token.txt", "r") as f:
#    content = [l.rstrip() for l in f.readlines()]
#    TOKEN, USERNAME = content[0], content[1]



""" posting a pixel """
def post_a_pixel():
    username = user.get()
    graph_id = graph.get()
    GRAPH_PARAMS['quantity'] = quantity.get()
    if len(username) == 0 or len(graph_id) == 0 or len( GRAPH_PARAMS['quantity']) == 0:
        messagebox.showinfo(title="Error", message="You should fill all the fields")
    else:
        endpoint = f"{PIXELA}/{username}/graphs/{graph_id}"
        responce = requests.post(url=endpoint, json=GRAPH_PARAMS, headers=HEADERS)
        msg = responce.json()
        messagebox.showinfo(title="Responce", message=msg['message'])

### GUI ###
window = Tk()
window.title("Pixela habit tracker")
window.config(padx=15, pady=15)

canvas = Canvas(width=480, height=270, highlightthickness=0)
parrot = PhotoImage(file=resource_path("pixela.png"))
canvas_img = canvas.create_image(240, 135, image=parrot)
canvas.grid(column=1, row=1, columnspan=3)

add_pixel = Button(text="Add a pixel", width=15)
update_pixel = Button(text="Update a pixel", width=15)
add_user = Button(text="Add a user", width=15)
add_graph = Button(text="Add a graph", width=15)
add_pixel.grid(column=2, row=2, pady=5)
update_pixel.grid(column=2, row=3, pady=5)
add_user.grid(column=1, row=4, pady=5)
add_graph.grid(column=3, row=4, pady=5)


window.mainloop()
