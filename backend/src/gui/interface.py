from tkinter import *
import tkinter.filedialog
from algorithms.data import load_from_xls

textMain ='To calculate the coefficient of inbreeding, select one person on the list. \nTo calculate the coefficient of relationship, select two person on the list.'
subjects = []

def open_file(window, listbox):
    filename = tkinter.filedialog.askopenfilename(title = "Select file",filetypes =(("xlsx files", "*.xlsx"), ("xls files","*.xls"), ("all files","*.*")))
    load_from_xls(subjects, filename)
    for i in subjects:
        listbox.insert(END, i.name)


def open_default_file(window, listbox):
    filename = "/home/klaudia/git_workspace/coefficient-of-inbreeding-thesis/backend/src/algorithms/test.xlsx"
    load_from_xls(subjects, filename)
    for i in subjects:
        listbox.insert(END, i.name) 


def create_window():
    window = Tk()
    window.title("Inbreed Calc 0.1")
    window.geometry("600x600")

    scrollbar = Scrollbar(window) 
    scrollbar.pack( side = LEFT, fill = Y ) 
    listbox = Listbox(window, yscrollcommand = scrollbar.set, width=30) 

    listbox.pack( side = LEFT, fill = BOTH ) 
    scrollbar.config( command = listbox.yview )

    mainText = Message(window, text = textMain, anchor = W, width=250) 
    mainText.pack()

    button = Button(window, text='Coefficent of inbreeding', width=20)
    button2 = Button(window, text='Coeffficent of relationship', width=20)
    button3 = Button(window, text='Load file', width=20 , command = lambda: open_file(window, listbox))

    button.pack() 
    button2.pack() 
    button3.pack()
    label = Label(window, text='Klaudia Faltyn', anchor = S ) 
    label.pack() 

    open_default_file(window, listbox)
    #window.mainloop()

def send_data():
    return subjects

