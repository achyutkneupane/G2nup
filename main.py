from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import func as zoom

def callback():
    name= askopenfilename() 
    zoom.getdata(name)

Button(text='Load File', command=callback).pack(fill=X)
mainloop()