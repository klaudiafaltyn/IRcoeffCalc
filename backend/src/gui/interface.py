#from tkinter import Tk, Listbox, Scrollbar, RIGHT
from tkinter import *

textMain ='This is our Message'
listbox = 1

def create_window():
    window = Tk()
    window.title("Inbreed Calc 0.1")
    window.geometry("600x600")

    scrollbar = Scrollbar(window) 
    scrollbar.pack( side = LEFT, fill = Y ) 
    listbox = Listbox(window, yscrollcommand = scrollbar.set, width=30) 
    for line in range(100): 
        listbox.insert(END, 'This is line number' + str(line)) 
    listbox.pack( side = LEFT, fill = BOTH ) 
    scrollbar.config( command = listbox.yview )

    mainText = Message(window, text = textMain, anchor = W, width=250) 
    mainText.pack()

    button = Button(window, text='Coefficent of inbreeding', width=20) #command=...
    button2 = Button(window, text='Coeffficent of relationship', width=20) #command=...
    button.pack() 
    button2.pack() 

    label = Label(window, text='Klaudia Faltyn kopirajts', anchor = S ) 
    label.pack() 

    window.mainloop()


#def populateList():
    