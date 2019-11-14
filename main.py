from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import font
from tkinter.filedialog import askopenfilename
import xml.etree.ElementTree as g2
import effects as ef
import urllib.request
import webbrowser

window = Tk()
window.title("G2NUP Reader")
#window.configure(background='black')
window.resizable(0, 0)
window.geometry('500x90')
req = urllib.request.Request("http://cc.amazingcounters.com/counter.php?i=3243893&c=9731992", headers = {"User-Agent": "Mozilla/5.0"})
urllib.request.urlopen(req)

def callback():
    name= askopenfilename(initialdir = "Downloads",title = "Select G2NuP file",filetypes =[('G2Nu Patch', '*.g2nup')]) 
    but.destroy()
    getdata(name)
link = Label(window, text="© Achyut Neupane", fg="blue", cursor="hand2")
link.pack(anchor="e")
link.bind("<Button-1>", lambda e: webbrowser.open_new(r"https://tny.sh/nB6CYUS"))
Label(window, text="G2nup Patch Loader for Zoom G2Nu and G2.1Nu Multi effect processor.\n").pack()
but = Button(text='Load G2NuP', command=callback)
but.pack(anchor="center")

def getdata(file):
    window.geometry('650x350')
    tr = g2.parse(file)
    patch = tr.getroot()
    for i in range(0,len(patch)):
        if(patch[i].tag == "Name"):
            tex = patch[i].text
        if(patch[i].tag == "Module1"):
            n = i
    Label(window, text="Patch Name: ",font = ("Purisa", 9)).pack()
    Label(window, text="%s" % tex.replace("*"," "),font = ("Purisa", 11,"bold")).pack()
    tree = ttk.Treeview(window)
    tree["columns"]=("","","","","","","")
    tree.column("#0", width=200,anchor="center")
    tree.column("#1", width=150,anchor="center")
    tree.column("#2", width=150,anchor="center")
    tree.column("#3", width=150,anchor="center")

    #Compressor
    if(patch[n][0].text == "0"):
        tree.insert("", 1,text="COMPRESSOR: OFF")
    else:
        num = int(patch[n][1].text)
        if(patch[n][1].text == "0"):
            if(patch[n][3].text == "1"):
                com2 = "FAST"
            else:
                com2 = "SLOW"
        else:
            com2 = int(patch[n][3].text)
        tree.insert("", 1,text="COMPRESSOR: %s" % ef.efx[num][0], values=("%s: %s" %(ef.comp[num][1],patch[n][2].text),"%s: %s" %(ef.comp[num][2],com2),"%s: %s" %(ef.comp[num][3],(int(patch[n][4].text)+1)*2)))

    #efx
    num = int(patch[n+1][1].text)
    if(patch[n+1][0].text == "0"):
        tree.insert("", 2,text="EFX: OFF")
    else:
        tree.insert("", 2,text="EFX: %s" % ef.efx[num][0], values=("%s: %s" %(ef.efx[num][1],int(patch[n+1][2].text)+1),"%s: %s" %(ef.efx[num][2],patch[n+1][3].text),"%s: %s" %(ef.efx[num][3],(int(patch[n+1][4].text)+1)*2)))

    #znr
    num = int(patch[n+2][1].text)
    if(patch[n+2][0].text == "0"):
        tree.insert("", 3,text="ZNR: OFF")
    else:
        tree.insert("", 3,text="ZNR: %s" % ef.znr[num][0], values=("%s: %s" %(ef.znr[num][1],int(patch[n+2][2].text)+1),"",""))
    
    #drive
    num = int(patch[n+3][1].text)
    if(patch[n+3][0].text == "0"):
        tree.insert("", 4,text="DRV: OFF")
    else:
        tree.insert("", 4,text="DRV: %s" % ef.drv[num][0], values=("%s: %s" %(ef.drv[num][1],int(patch[n+3][2].text)),"%s: %s" %(ef.drv[num][2],patch[n+3][3].text),"%s: %s" %(ef.drv[num][3],(int(patch[n+3][4].text)+1))))

    #eq
    eql = ['160','400','800','3.2K','6.4K','12K']
    eq = ['0','1','2','3','4','5']
    for i in range(0,6):
        eq[i] = eql[i] + "Hz: " + str(int(patch[n+4][i+2].text)-12)
    tree.insert("", 5,text="EQ LOW", values=(eq[0],eq[1],eq[2]))
    tree.insert("", 6,text="EQ HIGH", values=(eq[3],eq[4],eq[5]))

    #mod
    num = int(patch[n+6][1].text)
    if(patch[n+6][0].text == "0"):
        tree.insert("", 7,text="MOD: OFF")
    else:
        tree.insert("", 7,text="MOD: %s" % ef.mod[num][0], values=("%s: %s" %(ef.mod[num][1],int(patch[n+6][2].text)*2),"%s: %s" %(ef.mod[num][2],int(patch[n+6][3].text)+1),"%s: %s" %(ef.mod[num][3],(int(patch[n+6][4].text)*2))))

    #Delay
    num = int(patch[n+7][1].text)
    if(patch[n+7][0].text == "0"):
        tree.insert("", 8,text="Delay: OFF")
    else:
        tree.insert("", 8,text="Delay: %s" % ef.dly[num][0], values=("%s: %s" %(ef.dly[num][1],int(patch[n+7][2].text)+1),"%s: %s" %(ef.dly[num][2],int(patch[n+7][3].text)*2),"%s: %s" %(ef.dly[num][3],(int(patch[n+7][4].text)*2))))

    #Reverb
    num = int(patch[n+8][1].text)
    if(patch[n+8][0].text == "0"):
        tree.insert("", 9,text="Reverb: OFF")
    else:
        tree.insert("", 9,text="Reverb: %s" % ef.rev[num][0], values=("%s: %s" %(ef.rev[num][1],int(patch[n+8][2].text)+1),"%s: %s" %(ef.rev[num][2],int(patch[n+8][3].text)),"%s: %s" %(ef.rev[num][3],(int(patch[n+8][4].text)*2))))
    tree.pack()
mainloop()