from tkinter import *

root = Tk()

labelframe = LabelFrame(root,text='this is a label frame')

labelframe.grid(row=1,column=1)

left = Label(labelframe, text='inside the labelframe')
left.pack()

root.mainloop()