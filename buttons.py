from tkinter import *

root = Tk()

def clickMe():
	myLabel = Label(root, text=e.get())
	myLabel.pack()


e = Entry(root, width= 50, borderwidth=5,
 bg="skyblue", fg="white")
e.pack()
e.insert(0, "enter your name: ")


myButton = Button(root, text="enter your name",  
	padx=5, pady=5, command=clickMe, fg="blue", bg="gray") # state="disabled",

myButton.pack()

root.mainloop()