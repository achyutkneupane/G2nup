import xml.etree.ElementTree as g2
import effects as ef

tr = g2.parse('test.g2nup')
root = tr.getroot()

def getdata(patch):
    print("Patch Name: %s" % patch[1].text)
    if(patch[2].text == "None"):
        print("Tool Tip: %s" % patch[2].text)

    #Compressor
    if(patch[6][0].text == "0"):
        print("Compressor: OFF")
    else:
        num = int(patch[6][1].text)
        if(patch[6][1].text == "0"):
            if(patch[6][3].text == "1"):
                com2 = "FAST"
            else:
                com2 = "SLOW"
        else:
            com2 = int(patch[6][3].text)
        print("Compressor: %s" % ef.comp[num][0])
        print("\t    %s: %s" %(ef.comp[num][1],patch[6][2].text))
        print("\t    %s: %s" %(ef.comp[num][2],com2))
        print("\t    %s: %s" %(ef.comp[num][3],(int(patch[6][4].text)+1)*2))

        #efx
        num = int(patch[7][1].text)
        if(patch[7][0].text == "0"):
            print("\nEFX: OFF")
        else:
            print("\nEFX: %s" % ef.efx[num][0])
            print("     %s: %s" %(ef.efx[num][1],int(patch[7][2].text)+1))
            print("     %s: %s" %(ef.efx[num][2],patch[7][3].text))
            print("     %s: %s" %(ef.efx[num][3],(int(patch[7][4].text)+1)*2))

        #znr
        num = int(patch[8][1].text)
        if(patch[8][0].text == "0"):
            print("\nZNR: OFF")
        else:
            print("\nZNR: %s" % ef.znr[num][0])
            print("     %s: %s" %(ef.znr[num][1],int(patch[8][2].text)+1))
        
        #drive
        num = int(patch[9][1].text)
        if(patch[9][0].text == "0"):
            print("\nDRV: OFF")
        else:
            print("\nDRV: %s" % ef.drv[num][0])
            print("     %s: %s" %(ef.drv[num][1],int(patch[9][2].text)))
            print("     %s: %s" %(ef.drv[num][2],patch[9][3].text))
            print("     %s: %s" %(ef.drv[num][3],(int(patch[9][4].text)+1)))

        #eq
        eql = ['160','400','800','3.2K','6.4K','12K']
        print("\nEQ: ")
        for i in range(0,6):
            print("%sHz : %s" %(eql[i],int(patch[10][i+2].text)-12))

        #mod
        num = int(patch[12][1].text)
        if(patch[12][0].text == "0"):
            print("\nMOD: OFF")
        else:
            print("\nMOD: %s" % ef.mod[num][0])
            print("     %s: %s" %(ef.mod[num][1],int(patch[12][2].text)*2))
            print("     %s: %s" %(ef.mod[num][2],int(patch[12][3].text)+1))
            print("     %s: %s" %(ef.mod[num][3],(int(patch[12][4].text)*2)))

        #Delay
        num = int(patch[13][1].text)
        if(patch[13][0].text == "0"):
            print("\nDelay: OFF")
        else:
            print("\nDelay: %s" % ef.mod[num][0])
            print("       %s: %s" %(ef.mod[num][1],int(patch[13][2].text)+1))
            print("       %s: %s" %(ef.mod[num][2],int(patch[13][3].text)*2))
            print("       %s: %s" %(ef.mod[num][3],(int(patch[13][4].text)*2)))

        #Reverb
        num = int(patch[14][1].text)
        if(patch[14][0].text == "0"):
            print("\nReverb: OFF")
        else:
            print("\nReverb: %s" % ef.mod[num][0])
            print("       %s: %s" %(ef.mod[num][1],int(patch[14][2].text)+1))
            print("       %s: %s" %(ef.mod[num][2],int(patch[14][3].text)))
            print("       %s: %s" %(ef.mod[num][3],(int(patch[14][4].text)*2)))
getdata(root)
