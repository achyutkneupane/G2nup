from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import xml.etree.ElementTree as g2
import effects as ef

window = Tk()
window.title("G2NUP Reader")
# window.configure(background='white')
window.geometry('650x300')
window.resizable(0, 0) 

tree = ttk.Treeview(window)
tree["columns"]=("","","","")
tree.column("#0", width=200,anchor="center")
tree.column("#1", width=150,anchor="center")
tree.column("#2", width=150,anchor="center")
tree.column("#3", width=150,anchor="center")

def callback():
    name= askopenfilename(initialdir = "Downloads",title = "Select G2NuP file",filetypes =[('G2Nu Patch', '*.g2nup')]) 
    getdata(name)

def getdata(file):
    tr = g2.parse(file)
    patch = tr.getroot()
    for i in range(0,len(patch)):
        if(patch[i].tag == "Name"):
            tex = patch[i].text
        if(patch[i].tag == "Module1"):
            n = i
    print("Patch Name: %s" % tex.replace("*"," "))
    

    #Compressor
    if(patch[n][0].text == "0"):
        print("Compressor: OFF")
    else:
        num = int(patch[n][1].text)
        if(patch[n][1].text == "0"):
            if(patch[n][3].text == "1"):
                com2 = "FAST"
            else:
                com2 = "SLOW"
        else:
            com2 = int(patch[n][3].text)
        #tree.insert("", 0,text="Line 2", values=("2A","2b","2c"))
        print("Compressor: %s" % ef.comp[num][0])
        print("\t    %s: %s" %(ef.comp[num][1],patch[n][2].text))
        print("\t    %s: %s" %(ef.comp[num][2],com2))
        print("\t    %s: %s" %(ef.comp[num][3],(int(patch[n][4].text)+1)*2))

    #efx
    num = int(patch[n+1][1].text)
    if(patch[n+1][0].text == "0"):
        print("\nEFX: OFF")
    else:
        print("\nEFX: %s" % ef.efx[num][0])
        print("     %s: %s" %(ef.efx[num][1],int(patch[n+1][2].text)+1))
        print("     %s: %s" %(ef.efx[num][2],patch[n+1][3].text))
        print("     %s: %s" %(ef.efx[num][3],(int(patch[n+1][4].text)+1)*2))

    #znr
    num = int(patch[n+2][1].text)
    if(patch[n+2][0].text == "0"):
        print("\nZNR: OFF")
    else:
        print("\nZNR: %s" % ef.znr[num][0])
        print("     %s: %s" %(ef.znr[num][1],int(patch[n+2][2].text)+1))
    
    #drive
    num = int(patch[n+3][1].text)
    if(patch[n+3][0].text == "0"):
        print("\nDRV: OFF")
    else:
        print("\nDRV: %s" % ef.drv[num][0])
        print("     %s: %s" %(ef.drv[num][1],int(patch[n+3][2].text)))
        print("     %s: %s" %(ef.drv[num][2],patch[n+3][3].text))
        print("     %s: %s" %(ef.drv[num][3],(int(patch[n+3][4].text)+1)))

    #eq
    eql = ['160','400','800','3.2K','6.4K','12K']
    print("\nEQ: ")
    for i in range(0,6):
        print("%sHz : %s" %(eql[i],int(patch[n+4][i+2].text)-12))

    #mod
    num = int(patch[n+6][1].text)
    if(patch[n+6][0].text == "0"):
        print("\nMOD: OFF")
    else:
        print("\nMOD: %s" % ef.mod[num][0])
        print("     %s: %s" %(ef.mod[num][1],int(patch[n+6][2].text)*2))
        print("     %s: %s" %(ef.mod[num][2],int(patch[n+6][3].text)+1))
        print("     %s: %s" %(ef.mod[num][3],(int(patch[n+6][4].text)*2)))

    #Delay
    num = int(patch[n+7][1].text)
    if(patch[n+7][0].text == "0"):
        print("\nDelay: OFF")
    else:
        print("\nDelay: %s" % ef.dly[num][0])
        print("       %s: %s" %(ef.dly[num][1],int(patch[n+7][2].text)+1))
        print("       %s: %s" %(ef.dly[num][2],int(patch[n+7][3].text)*2))
        print("       %s: %s" %(ef.dly[num][3],(int(patch[n+7][4].text)*2)))

    #Reverb
    num = int(patch[n+8][1].text)
    if(patch[n+8][0].text == "0"):
        print("\nReverb: OFF")
    else:
        print("\nReverb: %s" % ef.rev[num][0])
        print("       %s: %s" %(ef.rev[num][1],int(patch[n+8][2].text)+1))
        print("       %s: %s" %(ef.rev[num][2],int(patch[n+8][3].text)))
        print("       %s: %s" %(ef.rev[num][3],(int(patch[n+8][4].text)*2)))
Button(text='Load File', command=callback).pack()

tree.pack()
mainloop()