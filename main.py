from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import func as zoom

window = Tk()
window.title("G2NUP Reader")
window.configure(background='black')
window.geometry('500x300')
window.resizable(0, 0) 
def callback():
    name= askopenfilename(initialdir = "Downloads",title = "Select G2NuP file",filetypes =[('G2Nu Patch', '*.g2nup')]) 
    zoom.getdata(name)

Button(text='Load File', command=callback).pack()
mainloop()