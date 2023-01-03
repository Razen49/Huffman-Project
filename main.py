from tkinter import*
import sys
import Encrypt


#SET WINDOW
root= Tk()
root.attributes('-fullscreen', True)
root.bind('<Escape>',lambda e: root.destroy())

h= root.winfo_screenheight()
w= root.winfo_screenwidth()

#SET LEFT SIDE
left= Frame(root, width= w/2, height= h, bg= 'red')


#SET RIGHT SIDE
right= Frame(root, width= w/2, height= h)
KeyFrame= Frame(right, width= w/2, height= h/2, bg= 'blue')
TextFrame= Frame(right, width= w/2, height= h/2, bg= 'yellow')

left.pack(side= LEFT)

right.pack(side= RIGHT)

KeyFrame.pack(side= TOP)
KeyFrame.pack_propagate(FALSE)

y= 0
for i in Encrypt.Dic:
    if i[1] != 0:        
        Label(KeyFrame, text= i[0], anchor= "w", width= int(KeyFrame.winfo_width()/3)).grid(row= y, column= 0)#chara
        Label(KeyFrame, text= Encrypt.key[i[0]], anchor= "w", width= int(KeyFrame.winfo_width()/3)).grid(row= y, column= 1)#code
        Label(KeyFrame, text= "apparait "+ str(i[1])+" fois", anchor= "w", width= int(KeyFrame.winfo_width()/3)).grid(row= y, column= 2)  #occurence
    y+=1


TextFrame.pack(side= BOTTOM)

root.mainloop()