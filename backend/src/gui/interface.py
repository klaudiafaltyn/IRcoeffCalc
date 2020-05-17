from tkinter import *
import tkinter.filedialog
from algorithms.data import load_from_xls
from algorithms.graph import inbreed_calculate, relation_calculate, generate_data, draw_graph

textMain = "\n• First, load the pedigree file in .xlsx or .xls format.\n• To calculate the coefficient of inbreeding, select one person on the list.\n• To calculate the coefficient of relationship, select two person on the list.\n• Finally click the appropriate button.\n\n"
subjects = []

def open_file(window, listbox):
    listbox.delete("0", "end")
    subjects[:] = []
    filename = tkinter.filedialog.askopenfilename(
        title="Select file",
        filetypes=(
            ("xlsx files", "*.xlsx"),
            ("xls files", "*.xls"),
            ("all files", "*.*"),
        ),
    )
    load_from_xls(subjects, filename)
    for i in subjects:
        listbox.insert(END, i.name)
    generate_data(subjects)
    draw_graph()


def open_default_file(window, listbox):
    filename = "/home/michael/licencjat/coefficient-of-inbreeding-thesis/backend/src/algorithms/test.xlsx"
    load_from_xls(subjects, filename)
    for i in subjects:
        listbox.insert(END, i.name)
    generate_data(subjects)


def setText(txt_field, function):
    txt_field.configure(text="Result: ")


def show_inbreed(txt_field, idx):
    if len(idx) != 1:
        txt_field.configure(text=" Error: Select only one person to count its coefficient of inbreeding!")
        return
    txt = "\n• Coefficient of inbreeding for %s: %f.\n• This means that about %.2f%% of the total number of %s loci are pairs of genes identical by origin." % (
        subjects[idx[0]].name,
        round(inbreed_calculate(subjects[idx[0]].name), 6),
        round(inbreed_calculate(subjects[idx[0]].name)*100, 2),
        subjects[idx[0]].name,
    )
    txt_field.configure(text=txt)


def show_relation(txt_field, idx):
    if len(idx) != 2:
        txt_field.configure(text="Error: Select two person to count their coefficient of relationship!")
        return
    txt = "\n• Coefficient of relationship for %s and %s: %f.\n• The probability that the allele at the %s locus is identical to the %s allele at the same locus is %.2f%%. " % (
        subjects[idx[0]].name,
        subjects[idx[1]].name,
        relation_calculate(subjects[idx[0]].name, subjects[idx[1]].name),
        subjects[idx[0]].name,
        subjects[idx[1]].name,
        relation_calculate(subjects[idx[0]].name, subjects[idx[1]].name)*100,
    )
    txt_field.configure(text=txt)


def create_window():
    window = Tk()
    window.title("Inbreed Calc 0.1")
    window.geometry("700x600")

    scrollbar = Scrollbar(window)
    scrollbar.pack(side=LEFT, fill=Y)
    listbox = Listbox(
        window, yscrollcommand=scrollbar.set, width=30, selectmode="multiple"
    )

    listbox.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=listbox.yview)

    mainText = Message(window, text=textMain, anchor=W, width=400)
    mainText.pack()

    resultInbred = Message(window, text="", anchor=W, width=400)
    resultRel = Message(window, text="", anchor=W, width=400)
    button = Button(
        window,
        text="Coefficent of inbreeding",
        width=20,
        command=lambda: show_inbreed(resultInbred, listbox.curselection()),
    )
    button2 = Button(
        window,
        text="Coeffficent of relationship",
        width=20,
        command=lambda: show_relation(resultRel, listbox.curselection()),
    )
    button3 = Button(
        window, text="Load file", width=20, command=lambda: open_file(window, listbox)
    )

    button.pack()
    button2.pack()
    button3.pack()
    resultRel.pack()
    resultInbred.pack()
    label = Label(window, text="Klaudia Faltyn, 2020", anchor=W)
    label.pack(side=BOTTOM, fill=X)

    # open_default_file(window, listbox)
    window.mainloop()
