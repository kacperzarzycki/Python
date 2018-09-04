from tkinter import *
from tkinter import ttk


# Function returns speed value from input box
def calculate_speed():
	s = float(distancebox.get())
	t = float(timebox.get())
	speed = round( s / t, 4)
	return speed

# Function returns distance value from input box
def calculate_distance():
	v = float(speedbox.get())
	t = float(timebox.get())
	distance = round(v * t, 4)
	return distance

# Function returns time value from input box
def calculate_time():
	s = float(distancebox.get())
	v = float(speedbox.get())
	time = round(s / v, 4)
	return time


# Function inserts answer into speed box
def insert_speed():
	answer = calculate_speed()
	speedbox.delete(0, END)
	speedbox.insert(0, answer)

# Function inserts answer into distance box
def insert_distance():
	answer = calculate_distance()
	distancebox.delete(0, END)
	distancebox.insert(0, answer)

# Function inserts answer into time box
def insert_time():
	answer = calculate_time()
	timebox.delete(0, END)
	timebox.insert(0, answer)


box = Tk()
box.title("V S T calculator")

# speed label and input box
speedlabel1 = Label(box, text="speed")
speedlabel1.grid(row=0, column=0, sticky=W)
speedbox = Entry(box, width=8)
speedbox.grid(row=0,column=1, sticky=W)
speedlabel2 = Label(box, text="km/h")
speedlabel2.grid(row=0, column=2, sticky=W)

# distance label and input box
distancelabel1 = Label (box, text="distance")
distancelabel1.grid(row=1, column=0, sticky=W)
distancebox = Entry(box, width=8)
distancebox.grid(row=1,column=1, sticky=W)
distancelabel2 = Label (box, text="km")
distancelabel2.grid(row=1, column=2, sticky=W)

# time label and input box
timelabel1 = Label(box, text="time")
timelabel1.grid(row=2, column=0, sticky=W)
timebox = Entry(box, width=8)
timebox.grid(row=2,column=1, sticky=W)
timelabel2 = Label(box, text="h")
timelabel2.grid(row=2, column=2, sticky=W)

# Buttons for each calculation
button1 = Button(box, text="speed", command=insert_speed, width=6)
button1.grid(row=4, column=0, sticky=W+E)
button2 = Button(box, text="distance", command=insert_distance, width=6)
button2.grid(row=4, column=1, sticky=N)
button3 = Button(box, text="time", command=insert_time, width=6)
button3.grid(row=4, column=2, sticky=W+E)

box.mainloop()
