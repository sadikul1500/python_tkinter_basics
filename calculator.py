from tkinter import *

root = Tk()
root.title("Add me")

first_number = 0
sign = 0

def clickMe():
	myLabel = Label(root, text=e.get())
	myLabel.pack()



e = Entry(root, width= 40, borderwidth=5, 
 bg="skyblue", fg="white")

e.grid(row=0, column=1, columnspan=3, padx=10, pady=10)
#e.pack()
#e.insert(0, "enter your name: ")


def button_click(number):
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))



def button_clear():
	e.delete(0, END)


def f_num():
	global first_number
	first_number = int(e.get())
	e.delete(0, END)


def button_add():
	global sign 
	sign = 0
	f_num()


def button_equal():
	second_number = int(e.get())
	e.delete(0, END)
	
	if sign == 0:
		e.insert(0, str(first_number + second_number))
	elif sign == 1:
		e.insert(0, str(first_number - second_number))
	elif sign == 2:
		e.insert(0, str(first_number * second_number))
	if sign == 3:
		e.insert(0, str(first_number // second_number))


def button_subtract():
	global sign 
	sign = 1
	f_num()


def button_multiply():
	global sign 
	sign = 2
	f_num()


def button_division():
	global sign 
	sign = 3
	f_num()



pad_x = 35
pad_y = 25

button_0 = Button(root, text="0", padx=pad_x, pady=pad_y, 
	command=lambda: button_click(0))
button_1 = Button(root, text="1", padx=pad_x, pady=pad_y, 
	command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=pad_x, pady=pad_y, 
	command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=pad_x, pady=pad_y, 
	command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=pad_x, pady=pad_y, 
	command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=pad_x, pady=pad_y, 
	command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=pad_x, pady=pad_y, 
	command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=pad_x, pady=pad_y, 
	command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=pad_x, pady=pad_y, 
	command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=pad_x, pady=pad_y, 
	command=lambda: button_click(9))

button_add = Button(root, text="+", padx=pad_x, pady=pad_y, 
	command=button_add)

button_clear = Button(root, text="Clear", padx=68, pady=pad_y, 
	command=button_clear)

button_equal = Button(root, text="=", padx=78, pady=pad_y, 
	command=button_equal)


button_subtract = Button(root, text="_", padx=pad_x, pady=pad_y, 
	command=button_subtract)
button_multiply = Button(root, text="x", padx=pad_x, pady=pad_y, 
	command=button_multiply)
button_division = Button(root, text="/", padx=pad_x, pady=pad_y, 
	command=button_division)




button_1.grid(row=3, column=1)
button_2.grid(row=3, column=2)
button_3.grid(row=3, column=3)

button_4.grid(row=2, column=1)
button_5.grid(row=2, column=2)
button_6.grid(row=2, column=3)

button_7.grid(row=1, column=1)
button_8.grid(row=1, column=2)
button_9.grid(row=1, column=3)

button_0.grid(row=4, column=1)
button_clear.grid(row=4, column=2, columnspan=2)

button_add.grid(row=6, column=1)
button_equal.grid(row=6, column=2, columnspan=2)


button_subtract.grid(row=5, column=1)
button_multiply.grid(row=5, column=2)
button_division.grid(row=5, column=3)








#myButton = Button(root, text="enter your name",  
#	padx=5, pady=5, command=clickMe, fg="blue", bg="gray") # state="disabled",

#myButton.pack()

root.mainloop()