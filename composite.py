
import tkinter as tk #, Canvas, Frame, BOTH
from tkinter import ttk

from abc import ABC, abstractmethod


################################### interface class ###################################
class IShape(ABC): #ABC replaced Interface
    def draw(self, canvas): 
        pass
    def build(): #void
    	pass




################################### abstract class extends interface ###################################
class CompositeShape(IShape, ABC):
	def __init__(self):
		self.ishape = []
		#self.canvas = canvas

	def build():
		pass

	def draw(self):
		self.build()
		for shape in self.ishape:
			shape.draw()


	#def add(shape):
	#	self.ishape += [shape]






################################### circle class ###################################
class Circle(IShape):
	def __init__(self, canvas,x1, y1, x2, y2):
		self.canvas = canvas
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2 
	
	def draw(self):
		self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2)
		self.canvas.grid(row=0, column=5)

	def build():
		print('pie')





################################### rectangle class ###################################
class Rectangle(CompositeShape):
	def __init__(self, canvas):
		CompositeShape.__init__(self)
		self.canvas = canvas

	def build(self):
		self.ishape.append(Line(self.canvas, 100, 70, 300, 70))
		self.ishape.append(Line(self.canvas, 100, 190, 100, 70))
		self.ishape.append(Line(self.canvas, 100, 190, 300, 190))
		self.ishape.append(Line(self.canvas, 300, 190, 300, 70))




################################### triangle class ###################################
class Triangle(CompositeShape):
	def __init__(self, canvas):
		CompositeShape.__init__(self)
		self.canvas = canvas

	def build(self):
		self.ishape.append(Line(self.canvas, 200, 50, 100,150))
		self.ishape.append(Line(self.canvas, 100, 150, 300, 150))
		self.ishape.append(Line(self.canvas, 300, 150, 200, 50))




################################### star class ###################################
class Star(CompositeShape):
	def __init__(self, canvas):
		CompositeShape.__init__(self)
		self.canvas = canvas

	def build(self):
		self.ishape.append(Line(self.canvas, 100, 160, 200, 10))
		self.ishape.append(Line(self.canvas, 200, 10, 300, 160))
		self.ishape.append(Line(self.canvas, 300, 160, 80, 50))
		self.ishape.append(Line(self.canvas, 80, 50, 320, 50))
		self.ishape.append(Line(self.canvas, 100, 160, 320, 50))




################################### flag class ###################################
class Flag(CompositeShape):
	def __init__(self, canvas):
		CompositeShape.__init__(self)
		self.canvas = canvas
		self.rectangle = Rectangle(self.canvas)
		self.circle = Circle(self.canvas, 170, 100, 220, 170)

	def build(self):
		self.ishape.append(self.rectangle)
		self.ishape.append(self.circle)






################################### Line class ###################################
class Line(IShape):
	def __init__(self, canvas,x1,y1,x2,y2):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2 
		self.canvas = canvas

	def draw(self):
		#self.canvas.delete('all')
		self.canvas.create_line(self.x1, self.y1, self.x2, self.y2) #(150,50), (850,650)
		self.canvas.grid(row=0,column=5)

	def build():
		print('let me draw a line')








################################### main class ###################################
if __name__ == '__main__':

	#tk._test()

	window = tk.Tk()
	window.title('Shapes')
	window.geometry('900x500')

	f1 = tk.Frame(window, bg='gray')

	canvas = tk.Canvas(window)






	def circle(canvas):
		canvas.delete('all')
		circle1 = Circle(canvas, 60, 60, 200, 200)
		circle1.draw()



	def rectangle(canvas):
		canvas.delete('all')
		rect = Rectangle(canvas)
		rect.draw()



	def triangle(canvas):
		canvas.delete('all')
		triangle1  = Triangle(canvas)
		triangle1.draw()


	def star(canvas):
		canvas.delete('all')
		star1 = Star(canvas)
		star1.draw()


	def flag(canvas):
		canvas.delete('all')
		flag1 = Flag(canvas)
		flag1.draw()



	def line(canvas):
		canvas.delete('all')
		line1 = Line(canvas, 150, 50, 600, 750)
		line1.draw()



	bt = tk.Button(f1, text='Triangle', command= lambda: triangle(canvas)).grid(row=0, column=0,padx=20, pady=20)
	#bt.grid(column=1, row = 15)

	br = tk.Button(f1, text='Rectangle', command= lambda: rectangle(canvas)).grid(row=0, column=1,padx=20, pady=20)
	#br.grid(column=2, row = 15)

	bl = tk.Button(f1, text='Line', command= lambda: line(canvas)).grid(row=0, column=2,padx=20, pady=20)
	#bl.grid(column=3, row = 15)

	bc = tk.Button(f1, text='Circle', command= lambda: circle(canvas)).grid(row=0, column=3,padx=20, pady=20)
	#bc.grid(column=4, row = 15)

	bf = tk.Button(f1, text='Flag', command= lambda: flag(canvas)).grid(row=0, column=4,padx=20, pady=20)
	#bf.grid(column=5, row = 15)

	bs = tk.Button(f1, text='Star', command= lambda: star(canvas)).grid(row=0, column=5,padx=20, pady=20)
	#bs.grid(column=6, row = 15)

	f1.grid(row=50, column=1, columnspan=6) #.grid(row=0, column=0)

	window.mainloop()














'''
bt.pack(side="top")
br.pack(side="top")
bl.pack(side="top")
bc.pack(side="top")
bf.pack(side="top")
bs.pack(side="top")
#bt.pack(side="top")
'''


#bs = tk.Button(f2, text='Sttar', command=click).grid(row=0, column=5,padx=10, pady=10)
#f2.grid(row=0, column=2,columnspan=6)

'''
x = int(input())

if x == 5:
	canvas.delete('all')
'''







#f2 = tk.Frame(window)
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



#canvas.create_line(150, 50, 950, 700)

#canvas.grid(row=0,column=5)



#window.attributes('-fullscreen', True)

#def click():
#	greeting.configure(text='hiiiiii, button was clicked!!!!')
