from tkinter import *

root = Tk()

myLabel1 = Label(root, text="Practicing Muslim")
myLabel2 = Label(root, text="Madam")
myLabel3 = Label(root, text="      ")

#myLabel.pack()
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=3)
myLabel3.grid(row=1, column=1)

root.mainloop()