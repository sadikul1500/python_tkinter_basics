
import tkinter as tk #, Canvas, Frame, BOTH
from tkinter import ttk

#tk._test()
window = tk.Tk()
window.title('Shapes')
#window.geometry('900x500')
f1 = tk.Frame(window)
#window.pack(fill=BOTH, expand=1)

#greeting = tk.Label(text="Hello, Tkinter")
#greeting.grid(column=1, row = 0)
#greeting.pack()

#txt = tk.Entry(window, width=10)
#txt.grid(column=2, row=0)

#combo = ttk.Combobox(window)
#combo['values'] = ('a','b','c','d', "text")
#combo.current(2)
#combo.grid(column=2, row=3)


def click():
	greeting.configure(text='hiiiiii, button was clicked!!!!')

bt = tk.Button(f1, text='Triangle').grid(row=0, column=0,padx=10, pady=10)
#bt.grid(column=1, row = 15)

br = tk.Button(f1, text='Rectangle', command=click).grid(row=0, column=1,padx=10, pady=10)
#br.grid(column=2, row = 15)

bl = tk.Button(f1, text='Line', command=click).grid(row=0, column=2,padx=10, pady=10)
#bl.grid(column=3, row = 15)

bc = tk.Button(f1, text='Circle', command=click).grid(row=0, column=3,padx=10, pady=10)
#bc.grid(column=4, row = 15)

bf = tk.Button(f1, text='Flag', command=click).grid(row=0, column=4,padx=10, pady=10)
#bf.grid(column=5, row = 15)

bs = tk.Button(f1, text='Star', command=click).grid(row=0, column=5,padx=10, pady=10)
#bs.grid(column=6, row = 15)

f1.grid(row=1, column=1, columnspan=6) #.grid(row=0, column=0)

'''
bt.pack(side="top")
br.pack(side="top")
bl.pack(side="top")
bc.pack(side="top")
bf.pack(side="top")
bs.pack(side="top")
#bt.pack(side="top")
'''

canvas = tk.Canvas(window)
canvas.create_line(15, 25, 200, 25)
canvas.grid(column=2, row=0)



window.mainloop()