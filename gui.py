# import libraries
from tkinter import *
from tkinter import ttk
import tkinter as tk
from backend import *
from bs4 import BeautifulSoup as bs
from pywebcopy import save_website
from tkhtmlview import HTMLLabel
from tkinter import messagebox

gui = Tk()
gui.title("SYNAPSE")

#set window size (widthxheight)
gui.geometry("1500x1000")

#set window colour
gui.config(bg = "lightcyan")

top_frame = Frame(gui, bg = "linen" ,height="200", width="400", padx=30, pady=10)
top_frame.pack(pady=25)

outputframe = Frame(gui, bg = "linen" ,  pady=25)
outputframe.pack()

#function for saving the input
def saveinput():
    url = my_input.get(1.0, "end-1c")
    auth = tab2.get(1.0, "end-1c")
    head = tab3.get(1.0, "end-1c")
    drop = dropdown()
    code,text,header = request(drop, url, auth,head)
    soup = bs(text, "html.parser")
    prettyHTML = soup.prettify()
    lbl1.delete("1.0", "end")
    lbl1.insert(tk.END, prettyHTML)
    lbl2.set_html(text)
    status.config(text="Status code :" + str(code))

def saveproject():
    link = my_input.get(1.0, "end-1c")    
    save_website(url = link, project_folder="./saved_folder/")
    messagebox.showinfo("Saved!", "Project folder saved")


def dropdown():
    newvar=clicked.get()
    return(newvar)

#url box
my_input = Text(top_frame, height=1, width=76, padx=20, pady=20)
my_input.grid(row=0, column=1, padx=25, pady=40)


#button creation
sendbutton = Button(top_frame, text="Send", command=saveinput)
sendbutton.grid(row=0, column=2, padx=20)
savebutton = Button(top_frame, text="Save", command=saveproject)
savebutton.grid(row=0, column=3, padx=20)


option = [
    "GET",
    "PUT",
    "POST",
    "PATCH",
    "DELETE",
]

#datatype of menu text
clicked = StringVar()

#initial menu text
clicked.set("GET")

#creation of a drop menu 
drop = OptionMenu(top_frame, clicked, *option, command=dropdown )
drop.grid(row=0, column=0)
drop.config(bg = "#1338be", fg = "#fff", padx=20, pady=20)

#tabs widget
tabControl = ttk.Notebook(top_frame, height=100, width=400)
tab1 = Text(tabControl, width=100)
tab2 = Text(tabControl, width=100)
tab3 = Text(tabControl, width=100)
tab4 = Text(tabControl, width=100)
tabControl.add(tab1, text="Params")
tabControl.add(tab2, text="Authorisation")
tabControl.add(tab3, text="HEADERS")
tabControl.add(tab4, text="JSON")
tabControl.grid(row=1, column=1, padx=40, pady=45)

# response area
responseframe= Frame(gui, borderwidth=0, bg= "#fff")
responseframe.pack()
sframe = Frame(responseframe, padx=3, pady=3, bg= "#fff", highlightbackground= "black", highlightthickness=3)
sframe.pack()
statusframe= Frame(sframe, bg="#fff")
statusframe.pack()

# tabs output
tabControl= ttk.Notebook(responseframe, height=700, width=1500)
tab_1= Label(tabControl, text = "",bg= "#fff")
tab_2= Label(tabControl, text = "",bg= "#fff")
tab_3= Label(tabControl, text = "",bg= "#fff")
tabControl.add(tab_1, text= "Raw")
tabControl.add(tab_2, text= "Preview")
tabControl.add(tab_3, text= "Headers")
tabControl.pack(fill= "both")

#status code 
status= Label(statusframe, text = "Status code :000", height= 1, width= 16)
status.pack()

#label creation
lbl1 = Text(tab_1, height=1150, width=100, padx=50, pady=50, fg="black")
lbl1.pack()
lbl2 = HTMLLabel(tab_2, height=1150, html="preview", width=100, padx=50, pady=50, fg="black")
lbl2.pack(anchor="center")
lbl3 = Label(tab_3, height=1150, width=100, padx=50, pady=50, fg="black")
lbl3.pack()


gui.mainloop()

