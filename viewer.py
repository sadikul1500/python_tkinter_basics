from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("image icon")

root.iconbitmap('cup512.ico')

myImage1 = ImageTk.PhotoImage(Image.open("images/1.jpg"))
myImage2 = ImageTk.PhotoImage(Image.open("images/2.jpg"))
myImage3 = ImageTk.PhotoImage(Image.open("images/3.jpg"))
myImage4 = ImageTk.PhotoImage(Image.open("images/4.jpg"))
myImage5 = ImageTk.PhotoImage(Image.open("images/5.jpg"))
myImage6 = ImageTk.PhotoImage(Image.open("images/6.jpg"))
myImage7 = ImageTk.PhotoImage(Image.open("images/7.jpg"))

imageList = [myImage1, myImage2, myImage3, myImage4,
myImage5, myImage6, myImage7]

myLabel = Label(image=myImage1)
#myLabel.pack()
myLabel.grid(row=1, column=0, columnspan=3)



def change(image_index):
	global myLabel
	global button_forward
	global button_back

	myLabel.grid_forget()
	
	myLabel = Label(image=imageList[image_index])
	
	if image_index == 0:

		button_back = Button(root, text="<<", 
			command=lambda: change(len(imageList)-1))
	else:
		button_back = Button(root, text="<<", 
			command=lambda: change(image_index-1))
	
	myLabel.grid(row=1, column=0, columnspan=3)

	if image_index == len(imageList)-1:
		button_forward = Button(root, text=">>", state=DISABLED)
	else:
		button_forward = Button(root, text=">>", 
		command=lambda: change(image_index+1))
		

	button_forward.grid(row=0, column=2)
	button_back.grid(row=0, column=0)



def forward(image_index):
	global myLabel
	global button_forward
	global button_back

	myLabel.grid_forget()
	
	myLabel = Label(image=imageList[image_index])
	
	button_back = Button(root, text="<<", 
		command=lambda: forward(image_index-1))
	
	myLabel.grid(row=1, column=0, columnspan=3)

	if image_index == len(imageList)-1:
		button_forward = Button(root, text=">>", state=DISABLED)
	else:
		button_forward = Button(root, text=">>", 
		command=lambda: forward(image_index+1))
		

	button_forward.grid(row=0, column=2)
	button_back.grid(row=0, column=0)


def previous(image_index):
	global myLabel
	global button_forward
	global button_back

	myLabel.grid_forget()
	
	myLabel = Label(image=imageList[image_index])
	
	if image_index == 0:

		button_back = Button(root, text="<<", 
			command=lambda: previous(len(imageList)-1))
	else:
		button_back = Button(root, text="<<", 
			command=lambda: previous(image_index-1))
	
	myLabel.grid(row=1, column=0, columnspan=3)

	if image_index == len(imageList)-1:
		button_forward = Button(root, text=">>", state=DISABLED)
	else:
		button_forward = Button(root, text=">>", 
		command=lambda: forward(image_index+1))
		

	button_forward.grid(row=0, column=2)
	button_back.grid(row=0, column=0)




button_forward = Button(root, text=">>", 
	command=lambda:change(1))
button_back = Button(root, text="<<", 
	command=lambda:change(len(imageList)-1)) #previous
button_exit = Button(root, text="exit", command=root.quit)


button_forward.grid(row=0, column=2)
button_back.grid(row=0, column=0)
button_exit.grid(row=0, column=1)

#button_quit = Button(root, text="exit", command=root.quit)
#button_quit.pack()



root.mainloop()