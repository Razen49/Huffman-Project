from tkinter import *
import txtGen

def test():
    print("it works")
    return 0

######################
#LOREM IPSUM
######################


def UpdateChoice():
    var= v.get()
    if var == 1:
        TextEntry.delete("1.0","end")
    if var == 2:
        TextEntry.delete("1.0","end")
    if var == 3:
        TextEntry.delete("1.0","end")
        TextEntry.insert("1.0", txtGen.genLorem())

def start():
    text=  TextEntry.get('1.0', 'end')
    print(text)
    root.quit()
    return text







###########################################################################################
root= Tk()
root.geometry("800x600")
root.resizable(width=False, height=False)
root.update()
#SET MAIN
main= PanedWindow(root)


#SET TITLE
Ftitle= Frame(main, height= root.winfo_height()/6, width= root.winfo_width(), bg= 'red')
Ftitle.pack_propagate(False)
title = Label(Ftitle, text="Welcome to Huffman Compression!", anchor= "center")


#SET WRITTER
Fwriter= Frame(main, height= root.winfo_height()*4/6, width= root.winfo_width(), bg='yellow')
Fwriter.pack_propagate(False)
LeftWriter=Frame(Fwriter, height= root.winfo_height()*4/6, width= root.winfo_width()/2)
LeftWriter.pack_propagate(False)
RightWriter=Frame(Fwriter, height= root.winfo_height()*4/6, width= root.winfo_width()/2)
RightWriter.pack_propagate(False)
LabelEntry= Label(RightWriter, text="Enter your text",anchor= "center")
TextEntry= Text(RightWriter, height= 40)

scroll = Scrollbar(RightWriter)
TextEntry.configure(yscrollcommand= scroll.set)
scroll.config(command= TextEntry.yview)
scroll.pack(side= RIGHT, fill= Y)

v= IntVar()
v.set('1')
values = {"Enter a text" : '1',
          "Generate a random sentence" : '2',
          "Generate a Lorem Ipsum" : '3',
        }
for (text, value) in values.items():
    Radiobutton(LeftWriter, text = text, variable = v, value = value, indicator = 0, background = "light blue", command=UpdateChoice).pack(fill = X, ipady = 5,)

#SET PLAY
Fplay= Frame(main, height= root.winfo_height()/6, width= root.winfo_width(), bg= 'blue')
Fplay.pack_propagate(False)
play= Button(Fplay, text= "Generate", command= start)
quit= Button(Fplay,text= "quit", command= root.quit)


#DISPLAY
main.pack()
Ftitle.pack()
title.pack()

Fwriter.pack()
RightWriter.pack(side= RIGHT)
LeftWriter.pack(side= LEFT)
LabelEntry.pack()
TextEntry.pack()
Fplay.pack()
play.pack()
quit.pack()
root.mainloop()

#text= TextEntry.get('1.0','end')

